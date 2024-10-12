import os
import sys
import pytz
import lxml.etree
import phonenumbers
from pathlib import Path


class LanguageTimezoneExtractor:
    def __init__(self):
        self.territory_languages = self._load_territory_languages()

    def _load_territory_languages(self):
        """
        Loads the territory languages from the XML file.
        """
        this_dir, this_filename = os.path.split(__file__)
        DATA_PATH = os.path.join(this_dir, "supplementalData.xml")
        if not os.path.exists(DATA_PATH):
            raise FileNotFoundError(f"XML file supplementalData.xml not found.")
        
        try:
            with open(DATA_PATH, "rb") as f:
                langtree = lxml.etree.XML(f.read(), parser=None)
        except Exception as e:
            raise ValueError(f"Error parsing XML file: {e}")
        
        territory_languages = {}
        try:
            for t in langtree.find('territoryInfo').findall('territory'):
                langs = {}
                for l in t.findall('languagePopulation'):
                    langs[l.get('type')] = {
                        'percent': float(l.get('populationPercent')),
                        'official': bool(l.get('officialStatus'))
                    }
                territory_languages[t.get('type')] = langs
        except Exception as e:
            raise ValueError(f"Error processing XML data: {e}")
        
        return territory_languages

    def get_official_locale_ids(self, country_code):
        """
        Returns the official locale IDs for a given country code.
        """
        country_code = country_code.upper()
        if country_code not in self.territory_languages:
            raise ValueError(f"Country code '{country_code}' not found in the territory languages data.")
        
        langs = self.territory_languages[country_code].items()
        official_langs = [
            '{lang}_{terr}'.format(lang=lang, terr=country_code)
            for lang, spec in langs if spec['official']
        ]
        return official_langs[0] if official_langs else None

    def get_language_and_timezone(self, country_code):
        """
        Returns the language and timezone for a given country code.
        """
        try:
            # Get region code from country code (e.g., 'IR' for Iran)
            country = phonenumbers.region_code_for_country_code(country_code)
            if not country:
                raise ValueError(f"Invalid or unsupported country code '{country_code}'.")
            
            # Get timezone
            timezone = pytz.country_timezones.get(country.upper(), ['UTC'])[0]
            
            # Get official language locale
            lang = self.get_official_locale_ids(country)
            if not lang:
                lang = "en"  # Default language if no official language is found
                system_lang_code = "en-" + country.lower()
            else:
                system_lang_code = lang.replace("_", "-").lower()
            
            return {
                "lang_code": lang.split("_")[0],
                "system_lang_code": system_lang_code,
                "timezone": timezone
            }
        
        except Exception as e:
            return {
                "error": str(e)
            }
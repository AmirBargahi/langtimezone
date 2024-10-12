# LangTimezone

LangTimezone is a Python library to extract language and timezone based on country code.

## Installation

You can install this package using pip:

```bash
pip install langtimezone
```

#How to Use
Here's a simple example of how to use the LanguageTimezoneExtractor class to get the language and timezone based on a country code:

```python
from langtimezone import LanguageTimezoneExtractor

# Create an instance of the extractor
extractor = LanguageTimezoneExtractor()

# Get language and timezone for a given country code
result = extractor.get_language_and_timezone(98)  # 98 is the country code for Iran

# Print the results
print(f"Language Code: {result['lang_code']}")
print(f"System Language Code: {result['system_lang_code']}")
print(f"Timezone: {result['timezone']}")
```

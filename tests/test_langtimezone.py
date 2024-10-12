import unittest
from langtimezone.langtimezone import LanguageTimezoneExtractor

class TestLanguageTimezoneExtractor(unittest.TestCase):

    def test_get_language_and_timezone(self):
        extractor = LanguageTimezoneExtractor()
        result = extractor.get_language_and_timezone(98)
        self.assertIn('lang_code', result)
        self.assertIn('timezone', result)
        self.assertEqual(result['lang_code'], 'fa')
        self.assertEqual(result['timezone'], 'Asia/Tehran')

if __name__ == '__main__':
    unittest.main()
import unittest
from app.watson import translate


class test_translator(unittest.TestCase):
  
  def test_english_to_dutch(self):
    self.assertEqual(translate('Newspaper', 'en-nl'), 'Krant')
    self.assertEqual(translate('Powerful', 'en-nl'), 'Krachtig')
    
  def test_dutch_to_english(self):
    self.assertEqual(translate('Hallo wereld', 'nl-en'), 'Hello World')
    self.assertEqual(translate('Jongens', 'nl-en'), 'Boys')
    
  def test_english_to_french(self):
    self.assertEqual(translate('Hand', 'en-fr'), 'Main')
    self.assertEqual(translate('Work', 'en-fr'), 'Travail')
    
  def test_french_to_english(self):
    self.assertEqual(translate('Fille', 'fr-en'), 'Daughter')
    self.assertEqual(translate('Personnes', 'fr-en'), 'People')

  def test_french_to_german(self):
    self.assertEqual(translate('Mon amour', 'fr-de'), 'Meine Liebe')
    self.assertEqual(translate('beauté', 'fr-de'), 'Schönheit')
    
  def test_german_to_italian(self):
    self.assertEqual(translate('Schönheit', 'de-it'), 'Bellezza')
    self.assertEqual(translate('Krankenhaus', 'de-it'), 'Hospital')
  
  def test_spanish_to_english(self):
    self.assertEqual(translate('amor', 'es-en'), 'love')
    self.assertEqual(translate('Loco', 'es-en'), 'Crazy')
    
if __name__ == '__main__':
  unittest.main()

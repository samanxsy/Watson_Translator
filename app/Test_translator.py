import unittest
from eng_dutch_translator import english_to_dutch


class test_translator(unittest.TestCase):
  
  def test_english_to_dutch(self):
    self.assertEqual(english_to_dutch('Newspaper'), 'Krant')
    self.assertEqual(english_to_dutch('Powerful'), 'Krachtig')
    
  def test_dutch_to_english(self):
    self.assertEqual(english_to_dutch('Hallo wereld'), 'Hello world')
    self.assertEqual(english_to_dutch('Jongens'), 'Boys')

if __name__ == '__main__':
  unittest.main()
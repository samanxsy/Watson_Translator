import unittest
from unittest.mock import patch, Mock
from app.common import status
from flask import Flask
from app.server import home, toTranslate

class BaseTest(unittest.TestCase):
  def setUp(self):
    self.app = Flask('Watson Translator', static_folder="./app/static")
    self.app.add_url_rule('/', 'home', home)
    self.app.add_url_rule('/translate', 'toTranslate', toTranslate)


class TestHome(BaseTest):
  def test_home(self):
    """Should return 200_OK upon visiting home page"""

    with self.app.test_client() as client:
      response = client.get("/")
      self.assertEqual(response.status_code, status.HTTP_200_OK)


class TestTranslator(BaseTest):
  def test_translation_success(self):
    """Should return translated text upon successful translation"""
    with self.app.test_client() as client:
      response = client.get("/translate?text_to_translate=hello&text_model=en&translate_model=es")
      self.assertEqual(response.status_code, status.HTTP_200_OK)
      
    
  def test_invalid_pair(self):
    """Should return error message when translation fails"""
    with self.app.test_client() as client:
      response = client.get("/translate?text_to_translate=hello&text_model=pr&translate_model=hu")
      self.assertIn(b"Sorry!\nTranslation is not available for this pair!", response.data)


  def test_empty_input(self):
    """Should return error message when text to translate is empty"""
    with self.app.test_client() as client:
      response = client.get("/translate?text_to_translate=&text_model=en&translate_model=es")
      self.assertIn(b"Please enter some text to translate!", response.data)

    
if __name__ == '__main__': 
  unittest.main()
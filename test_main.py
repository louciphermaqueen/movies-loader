import unittest
import json

class TestJSONLoaderMethods(unittest.TestCase):
  movies = []
  
  @classmethod
  def setUpClass(cls):
    with open('movies.json') as json_file:
      cls.movies = json.load(json_file)
  
  def test_rank(self):
    self.assertEqual(self.movies[0]['rank'], '1')
  
  def test_title(self):
    self.assertEqual(self.movies['title'], 'The Shawshank Redemption')
    
  def test_id(self):
    self.assertEqual(self.movies[0]['id'], 'tt0111161')
    
if __name__ == '__main__':
  unittest.main()
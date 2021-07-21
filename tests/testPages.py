import unittest, sys

sys.path.append('../Week4Project') # imports python file from parent directory
from routes import app #imports flask app object

class BasicTests(unittest.TestCase):

    # executed prior to each test
    def setUp(self):
        self.app = app.test_client()

    ###############
    #### tests ####
    ###############

    def test_home_page(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
    
    def test_animals_page(self):
        response = self.app.get('/animals', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
    
    def test_organizations_page(self):
        response = self.app.get('/organizations', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()
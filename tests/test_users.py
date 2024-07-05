import unittest, sys, os

sys.path.append('../change-to-your-repo-name') # imports python file from parent directory
from main_py_file_name import app, db #imports flask app object and db app object

class UsersTests(unittest.TestCase):
    def setUp(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
        self.app = app.test_client()
        with app.app_context():
            db.drop_all()
            db.create_all()

    def compare(self, player1, player2):
        return self.app.post('/', data=dict(player1=player1, player2=player2), follow_redirects=True)

    def test_valid_player_compare(self):
        response = self.compare('lionel messi', 'cristiano ronaldo')
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
 unittest.main()
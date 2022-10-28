
from unittest import TestCase
from app import app
from flask import session

#set app config to true so we know we're testing
app.config['TESTING'] = True


app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']


class ForexAppTest(TestCase):
    """Forex Flask App Test"""

    def test_root_route(self):
        with app.test_client() as client:
            # verify root tout 
            resp = client.get('/')
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('<h1> What would you like to convert? </h1>', html)

    def test_currency_submit(self):
        with app.test_client() as client:
            resp = client.post('/conversion',
                           data={'currency_from': 'USD', 'currency_to': 'EUR', 'amount' : 75})
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 302)
            self.assertIn('<h1> Here is your result </h1>', html)



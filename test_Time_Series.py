import unittest
from pandas import DataFrame as df
from alpha import *
import json
import requests
import urllib

class Mytest(unittest.TestCase):

    def test_API_key(self):
        self.assertEqual(API_key,'ASWJAF02A51KK5QQ')

    def test_Intraday(self):
        data= Time_series('MSFT','15min','full','Intraday')
        self.assertIsInstance(data,dict,'Should return a DataFrame')
        url = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=MSFT&interval=15min&outputsize=full&apikey=demo"
        response = urllib.request.urlopen(url)
        html = response.read()
        m_data = json.loads(html)
        #print(data)
        self.assertEqual(data,m_data['Time Series (15min)'])

if __name__ == '__main__':
    unittest.main()

import unittest
from alpha import *

class Mytest(unittest.TestCase):

    def test_API_key(self):
        self.assertEqual(API_key,'ASWJAF02A51KK5QQ')

if __name__ == '__main__':
    unittest.main()

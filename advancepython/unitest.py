import unittest
class Testexample(unittest.TestCase):
    def test_upper(self):
        self.assertEqual('andre'.upper(),"ANDRE")
if __name__=="__main__":
    unittest.main()

import unittest

import demo

class TestDemo(unittest.TestCase):

    def test_checkemail_ok(self):
        donnee_ok= 'toto@gmail.com'
        # Premier test mail ok
        result_ok= demo.check_email(donnee_ok)
        self.assertEqual(result_ok,'OK')

    def test_checkemail_ko(self):
        donne_ko = 'totofdhkgsfhjfs.com'
        # Deux test email KO
        result_ko = demo.check_email(donne_ko)
        self.assertEqual(result_ko, 'KO')

    # Test inutile : ne teste rien 
    def testDemo(self):
        self.assertEqual('toto','toto')

if __name__ == '__main__':
	unittest.main()
import unittest
from chapter15 import common

class CommonTestCase(unittest.TestCase):

    def test_email_validation_check_false(self):

        self.assertFalse(common.email_validation_check('isi.cho@gmail*om'))

    def test_email_validation_check_true(self):
        self.assertTrue(common.email_validation_check('jongwon208@gmail.com'))


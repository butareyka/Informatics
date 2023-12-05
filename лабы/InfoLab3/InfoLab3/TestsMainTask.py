import unittest
from MainTask import *

class MainTaskTest(unittest.TestCase):
    def test_only_letters(self):
        res = smile('AfnklAKsmdkksnfdnfBJNDS')
        self.assertEqual(res, 0)
    def test_only_numbers(self):
        res = smile('17653926634939347858686')
        self.assertEqual(res, 0)
    def test_only_sings(self):
        res = smile('!$@IU%@I$@O#PO%U@_---$@')
        self.assertEqual(res, 0)
    def test_empty_string(self):
        res = smile('')
        self.assertEqual(res, 0)
    def test_random_string(self):
        res = smile('X-OsdlfjXPXD:OX-OX-oX-O')
        self.assertEqual(res, 3)
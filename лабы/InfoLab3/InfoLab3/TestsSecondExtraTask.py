import unittest
from SecondExtraTask import *

class SecondExtraTask(unittest.TestCase):
    def test_Vowels_Basic(self):
        res = Vowels('Классное слово – обороноспособность, которое должно идти после слов: трава и молоко.')
        self.assertEqual(res, [['и'], ['идти'], ['слов'], ['слово'], ['трава'], ['должно'], ['молоко'], ['обороноспособность']])
    def test_Vowels_Change_N_D(self):
        res = Vowels('Классное слово – обороноспособность, которое нолжно идти после слов: трава и молоко.')
        self.assertEqual(res, [['и'], ['идти'], ['слов'], ['слово'], ['трава'], ['молоко'], ['нолжно'], ['обороноспособность']])
    def test_Vowels_Basic_Second_Var(self):
        res = Vowels('Мама мыла раму, папа ел горох')
        self.assertEqual(res, [['ел'], ['мама'], ['папа'], ['горох']])
    def test_Vowels_Empty(self):
        res = Vowels('Яма была глубокая. Таня, упалав туда, сломала ногу')
        self.assertEqual(res, [])
    def test_Vowels_Without_Words(self):
        res = Vowels('!!! %$# &&& <3, I love Informatics')
        self.assertEqual(res, [])

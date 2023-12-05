import unittest
from FirstExtraTask import *

class FirstExtraTask(unittest.TestCase):
    def test_VT_Empty_ITMO(self):
        res = VTITMO('ВТ ИТМО мама овыарвжоарп валфоы')
        self.assertEqual(res, [])
    def test_VT_One_Word_ITMO(self):
        res = VTITMO('ВТ хахахаха ИТМО мама овыарвжоарп валфоы')
        self.assertEqual(res,['ВТ хахахаха ИТМО'] )
    def test_VT_More_Than_Four_ITMO(self):
        res = VTITMO('ВТ z в в    о в ИТМО мама овыарвжоарп валфоы')
        self.assertEqual(res, [])
    def test_VT_Other_Sings_ITMO(self):
        res = VTITMO('ВТ 12ава    323 45324   (.;, ИТМО мама овыарвжоарп валфоы')
        self.assertEqual(res, ['ВТ 12ава    323 45324    ИТМО'])
    def test_VT_Random_ITMO(self):
        res = VTITMO('ВТ _ 1 в фыатлыsdjfsdijosd1243__ ИТМО мама овыарвжоарп валфоы ВТ ИТМО ВТ фыв ваы ыва ффффф    ИМТО')
        self.assertEqual(res, ['ВТ _ 1 в фыатлыsdjfsdijosd1243__ ИТМО'])
    def test_VT_Special_ITMO(self):
        res = VTITMO('ВТ ИТМО ИТМО ИТМО ИТМО ИТМО ИТМО ИТМО ВТ ВТ ВТ ВТ ВТ ИТМО ИТМО ИТМО ИТМО ИТМО ИТМО ИТМО')
        self.assertEqual(res, ['ВТ ИТМО ИТМО ИТМО ИТМО ИТМО', 'ВТ ВТ ВТ ВТ ВТ ИТМО'])

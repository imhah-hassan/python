# -*- coding: utf-8 -*-
# Illustration du fonctionnement de unitest et difference entre setUp et setUpClass, tearDown et tearDownClass
import unittest
from CalculCredit import *

class testMensualite(unittest.TestCase):
    def setUp(self):
        # print('setUp')
        self.credit1 = Credit(100000, 7)
        self.credit2 = Credit(100000, 10)
        self.credit3 = Credit(100000, 15)
        self.credit4 = Credit(100000, 20)

    def test_mesnualite11(self):
        self.assertEqual(self.credit1.mensualite(), 1229.68)
        self.assertEqual(self.credit1.cout_total(), 3293.12)

    def test_mensualite2(self):
        self.assertEqual(self.credit2.mensualite(), 880.39)
        self.assertEqual(self.credit2.cout_total(), 5646.8)

    def test_mensualite3(self):
        self.assertEqual(self.credit3.mensualite(), 615.36)
        self.assertEqual(self.credit3.cout_total(), 10764.8)

    def test_mensualite4(self):
        self.assertEqual(self.credit4.mensualite(), 487.16)
        self.assertEqual(self.credit4.cout_total(), 16918.4)

    def tearDown(self):
        # print ('tearDown')
        pass

if __name__ == "__main__":
    unittest.main()

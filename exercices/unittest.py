# -*- coding: utf-8 -*-
# Illustration du fonctionnement de unitest et difference entre setUp et setUpClass, tearDown et tearDownClass
import unittest
class illustration(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print ('Setup\n')

    def test_a_login(self):
        print ('test_login')

    def test_b_add_employee(self):
        print ('test_add_employee')

    def test_c_search_employee(self):
        print ('test_search_employee')

    def test_d_del_employee(self):
        print ('test_del_employee')

    def test_z_logout(self):
        print ('test_logout')

    @classmethod
    def tearDownClass(cls):
        print ('tearDown')

if __name__ == "__main__":
    unittest.main()

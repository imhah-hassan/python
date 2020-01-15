# pip install xmlrunner
import unittest
import xmlrunner

# import your test modules
import selenium_login_logout
import selenium_add_employee
import selenium_dataprovider
# initialize the test suite
loader = unittest.TestLoader()
suite = unittest.TestSuite()    

# add tests to the test suite
suite.addTests(loader.loadTestsFromModule(selenium_login_logout))
suite.addTests(loader.loadTestsFromModule(selenium_add_employee))
suite.addTests(loader.loadTestsFromModule(selenium_dataprovider))

# initialize a runner, pass it your suite and run it
# runner = unittest.TextTestRunner(verbosity=3)
runner = xmlrunner.XMLTestRunner(verbosity=3, output="D:\\APPS\\Jenkins\\workspace\\Python-Sample\\")
result = runner.run(suite)
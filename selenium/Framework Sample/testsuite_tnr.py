# pip install xmlrunner
import unittest
import xmlrunner

# import your test modules
import test_login
import test_employee
import test_configuration

# initialize the test suite
loader = unittest.TestLoader()
suite = unittest.TestSuite()

# add tests to the test suite
suite.addTests(loader.loadTestsFromModule(test_login))
suite.addTests(loader.loadTestsFromModule(test_configuration))
suite.addTests(loader.loadTestsFromModule(test_employee))

# initialize a runner, pass it your suite and run it
# runner = unittest.TextTestRunner(verbosity=3)
runner = xmlrunner.XMLTestRunner(verbosity=3, output="D:/APPS/Jenkins/workspace/OrangePy/")
result = runner.run(suite)

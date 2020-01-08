# tests/runner.py
import unittest
import xmlrunner

# import your test modules
import exercice10

# initialize the test suite
loader = unittest.TestLoader()
suite  = unittest.TestSuite()

# add tests to the test suite
suite.addTests(loader.loadTestsFromModule(exercice10))

# initialize a runner, pass it your suite and run it
# runner = unittest.TextTestRunner(verbosity=3)
runner = xmlrunner.XMLTestRunner(verbosity=3)

result = runner.run(suite)
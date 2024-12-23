# Домашнее задание по теме "Систематизация и пропуск тестов".

import unittest

# import by absolute paths
from modules.module_12_1 import RunnerTest
from modules.module_12_2 import TournamentTest

if __name__ == '__main__':
    testSuite = unittest.TestSuite()
    testLoader = unittest.TestLoader()  # to avoid using deprecated unittest.makeSuite(RunnerTest)
    testSuite.addTest(testLoader.loadTestsFromTestCase(RunnerTest.lockTests()))
    testSuite.addTest(testLoader.loadTestsFromTestCase(TournamentTest))
    runner = unittest.TextTestRunner(verbosity=3)
    runner.run(testSuite)


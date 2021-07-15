from unittest import TestLoader, TestSuite, TextTestRunner
from loginpageLogs import loginpage
from ZipcodeLogs import zipcodepage

import testtools as testtools

if __name__ == '__main__':

    loader = TestLoader
    suite = TestSuite((
        loader.loadTestsFromTestCase(loginpage),
        loader.loadTestsFromTestCase(zipcodepage)
        ))

#run test sequentially using simple text_test_runner

    runner = TextTestRunner(verbosity=2)
    runner.run(suite)

#run test parallel using concurrent suite

    concurrent_suite = testtools.ConcurrentStreamTestSuite(lambda: ((case,None) for case in suite))
    concurrent_suite.run(testtools.StreamResult())


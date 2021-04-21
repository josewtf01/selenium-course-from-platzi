from unittest import TestLoader, TestSuite
from pyunitreport import HTMLTestRunner
from assertions import AssertionsTest
from searchtests2 import SearchTests

assetions_test  = TestLoader().loadTestsFromTestCase(AssertionsTest)
search_test = TestLoader().loadTestsFromTestCase(SearchTests)

smoke_test = TestSuite([assetions_test,search_test])

kwargs = {
    "output":"smoke-report"

}

runner = HTMLTestRunner(**kwargs)
runner.run(smoke_test)

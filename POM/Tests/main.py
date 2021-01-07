import unittest
import HtmlTestRunner
from Tests.login import LoginTest


test_class = LoginTest()
unittest.main(module=test_class, 
testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/320084928/Documents/Work Folder/Dev/Python/Selenium/Selenium/POM/reports'))

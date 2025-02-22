
import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils import init_and_login

# globals normally would be put in a separate python module
# **** login credentials need to be somewhere secure for a real project
TEST_EMAIL = ""
TEST_PASSWORD = ""
NEW_SPACE_NAME_TEXT = "name"


class NewSpaceAndRStudioProjectTest(unittest.TestCase):
        
    @classmethod
    def setUpClass(cls):
        """
            Setup for all tests in the class.  Test cases will not run if there are exceptions in 
            this method.  
            
            Setup:  initialize web driver, go to the URI and login
        """
        
        cls.driver = webdriver.Firefox()
        
        try:
            init_and_login(cls.driver, TEST_EMAIL, TEST_PASSWORD)
        except Exception as exc:
            print(f'Exception initializing web page and logging in. Exception: {exc}')
            
            # tearDownClass is not executed if there is an exception in setUpClass so ensure driver is closed
            cls.driver.quit()
            raise exc
                
    
    def test_create_new_space(self):
        """
            Test case to create a new space
        """
        
        print('*** Starting test case: Create new Space')
        
        wait = WebDriverWait(self.driver, timeout=5)
        space_name='SpaceForAutomatedTest'
            
        # verify New Space button exists
        # xpath can be fragile, with more time look for a better way to get this button
        
        # **** It fails here not finding the New Space button, I ran out of time ****
        try:
            self.driver.find_element(By.XPATH, '//span[text()="New Space"]').click()
            element_exists = True
        except NoSuchElementException:
            element_exists = False           
        self.assertTrue(element_exists, "Button 'New Space' does not exist")

        # click the New Space button
        self.driver.find_element(By.XPATH, '//span[text()="New Space"]').click()
        print('Clicked New Space')
        
        # wait for pop-up with name field to exist
        try:
            wait.until(EC.element_to_be_clickable((By.ID, NEW_SPACE_NAME_TEXT)))
            element_exists = True
        except NoSuchElementException:
            element_exists = False
        self.assertTrue(element_exists, "Pop-up dialog with 'name' field does not exist")
        
        try:
            self.driver.find_element(By.ID, NEW_SPACE_NAME_TEXT).send_keys(space_name)
            send_text_succeeded = True
        except Exception:  # there are multiple possible exceptions, so using general Exception
            send_text_succeeded = False
        self.assertTrue(send_text_succeeded, "Setting value of pop-up dialog 'name' field failed")
        print('Entered new space name')
        
        
        
    def test_create_new_rstudio(self):
        """
            Test case to create a new RStudio project in the space created by the previous test.
            Normally it's better to have test cases be independent.
        """
        print('*** Starting test case: Create new Space')
        
    
    @classmethod
    def tearDownClass(cls):
        """
            Perform class tear down functions, such as closing the webdriver
        """
        cls.driver.quit()
        

if __name__ == '__main__':
    unittest.main()
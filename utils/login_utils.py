
import unittest
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# globals normally would be put in a separate python module
POSIT_URL = "http://posit.cloud"

LOG_IN_LINK = "Log In"
LOG_IN_EMAIL_TEXT = "email"
LOG_IN_PASSWORD_TEXT = "password"
HEADER_ID = "rStudioHeader"


def init_and_login(webdriver=None, user_email=None, user_password=None):
    """
        Go to the URI and login.
    """
    
    if not webdriver:
        print('Error: can not init and login without webdriver')
        raise TypeError('Arguement webdriver is required')
        
    if not user_email:
        print('Error: can not login without user_email')
        raise TypeError('Arguement user_email is required')
        
    if not webdriver:
        print('Error: can not login without user_password')
        raise TypeError('Arguement user_password is required')
    
    print('*** Opening website and logging in')
    
    # go to the Posit Cloud webpage
    print(f'Open url {POSIT_URL}')
    webdriver.get(POSIT_URL)
    
    # wait for the Log In link to be visible then click the link
    wait = WebDriverWait(webdriver, timeout=5)
    try:
        wait.until(EC.element_to_be_clickable((By.LINK_TEXT, LOG_IN_LINK)))
    except TimeoutException as timeExc:
        print(f'Error: Timed out waiting for link {LOG_IN_LINK} to be visible')
        raise timeExc
    except Exception as exc:
        print(f'Exception waiting for link {LOG_IN_LINK} to be visible. Exception: {exc}')
        raise exc
    
    webdriver.find_element(By.LINK_TEXT, LOG_IN_LINK).click()
    print('Clicked Log In')
    
    # wait for the email text box to be available then enter user email in the field and click Continue
    wait.until(EC.element_to_be_clickable((By.NAME, LOG_IN_EMAIL_TEXT)))
    webdriver.find_element(By.NAME, LOG_IN_EMAIL_TEXT).send_keys(user_email)
    print('Entered user email')
    
    # xpath can be fragile, with more time look for a better way to get this button
    webdriver.find_element(By.XPATH, '//span[text()="Continue"]').click()
    print('Clicked Continue')
    
    # wait for the password text box to be available then enter password in the field and click Log in
    wait.until(EC.element_to_be_clickable((By.NAME, LOG_IN_PASSWORD_TEXT)))
    webdriver.find_element(By.NAME, LOG_IN_PASSWORD_TEXT).send_keys(user_password)
    print('Entered password')
    
    # xpath can be fragile, with more time look for a better way to get this button
    webdriver.find_element(By.XPATH, '//span[text()="Log in"]').click()
    print('Clicked Log in')
    
    # wait for a control to confirm login is complete
    wait.until(EC.element_to_be_clickable((By.ID, HEADER_ID)))
    print('Log in complete')


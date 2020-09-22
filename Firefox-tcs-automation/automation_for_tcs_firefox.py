#import dependencies
from selenium import webdriver
import time   # sleep() to give the browser time to load.
import requests
import os
import pyspeedtest

class SpeedTest:
    try:
        st = pyspeedtest.SpeedTest()
        good_speed = False
        if st.ping() <= 30:
            good_speed = True
            print('yay')
        else:
            print('slow internet connection, automatically waiting ')
    except AttributeError:
        pass
    except Exception:
        pass
class TargetSiteURL:
    target_site = 'https://www.tcsion.com/LX/login'
    res = requests.get(target_site)
    subject_input = str(input('enter keyword for subject: '))


class BrowserInterfacing:
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    browser = webdriver.Firefox(executable_path = os.path.join(BASE_DIR, 'geckodriver.exe') , service_log_path = os.path.join(BASE_DIR,'Firefox_driver.log')) # The exe is not added to environment variables, keep the executable driver file in the same dir. 
    print('get request: {}'.format(TargetSiteURL.target_site))
    browser.get(TargetSiteURL.target_site)

    if browser.find_element_by_css_selector('#Usrname').is_displayed():
        username_elem = browser.find_element_by_css_selector('#Usrname')
        username_elem.send_keys('LOGIN-CREDENTIALS HERE ') # the argument for this function is fixed at the time of writing for "automation".

        password_elem = browser.find_element_by_css_selector('#Passwd')
        password_elem.send_keys('LOGIN-CREDENTIALS HERE ') ## the argument for this function is fixed at the time of writing for "automation".
        password_elem.submit()
        if not SpeedTest.good_speed:
            time.sleep(15)
        else:
            time.sleep(10)
    else:
        pass

    # course tab selection...
    print('selecting the courses tab... ')
    courses_tab = browser.find_element_by_css_selector('.mng_invoice')
    courses_tab.click()
    print('waiting for 5s ... ')
    time.sleep(5)

    if TargetSiteURL.subject_input == 'enz':
        print('clicking {} '.format(TargetSiteURL.subject_input))
        enz = browser.find_element_by_css_selector('div.accordion:nth-child(6) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > span:nth-child(1) > span:nth-child(1) > a:nth-child(1)')
        enz.click()
    elif TargetSiteURL.subject_input == 'bioinfo':
        print('clicking {} '.format(TargetSiteURL.subject_input))
        bioinfo = browser.find_element_by_css_selector('div.accordion:nth-child(7) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > span:nth-child(1) > span:nth-child(1) > a:nth-child(1)')
        bioinfo.click()
    elif TargetSiteURL.subject_input == 'BCE':
        print('clicking {} '.format(TargetSiteURL.subject_input))
        BCE = browser.find_element_by_css_selector('div.accordion:nth-child(9) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > span:nth-child(1) > span:nth-child(1) > a:nth-child(1)')
        BCE.click()
    elif TargetSiteURL.subject_input == 'HAP':
        print('clicking {} '.format(TargetSiteURL.subject_input))
        HAP = browser.find_element_by_css_selector('div.accordion:nth-child(8) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > span:nth-child(1) > span:nth-child(1) > a:nth-child(1)')
        HAP.click()
    elif TargetSiteURL.subject_input == 'java':
        print('clicking {} '.format(TargetSiteURL.subject_input))
        java = browser.find_element_by_css_selector('div.accordion:nth-child(11) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > span:nth-child(1) > span:nth-child(1) > a:nth-child(1)')
        java.click()
    elif TargetSiteURL.subject_input == 'mol':
        print('clicking {} '.format(TargetSiteURL.subject_input))
        mol = browser.find_element_by_css_selector('div.accordion:nth-child(10) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > span:nth-child(1) > span:nth-child(1) > a:nth-child(1)')
        mol.click()
    elif TargetSiteURL.subject_input == 'german':
        print('clicking {} '.format(TargetSiteURL.subject_input))
        german = browser.find_element_by_css_selector('div.accordion:nth-child(5) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > span:nth-child(1) > span:nth-child(1) > a:nth-child(1)')
        german.click()
    else:
        print('no subject found.')

def site_checking():
    if 'tcs' in TargetSiteURL.target_site:
        TargetSiteURL.target_site = 'target variable value destroyed... '
        print(TargetSiteURL.target_site)

site_checking()

import time

import pytest
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.core import driver

from utils.driver_factory import get_driver
from Pages.guvi_page import GuviPage


@pytest.fixture(scope="function")
def setup():
    driver = get_driver()
    Page = GuviPage(driver)
    Page.open_site()
    yield driver, Page
    driver.quit()


#Test case 1 - URL launch
def test_url_launch(setup):
    driver, Page = setup
    WebDriverWait(driver,10).until(lambda d: "guvi.in" in driver.current_url)
    assert "guvi.in" in driver.current_url

#Test case 2 - verify page title
def test_title(setup):
    driver, Page = setup
    WebDriverWait(driver,10).until(lambda d: d.title != "")
    expected = "HCL GUVI | Learn to code in your native language"
    assert driver.title.strip() == expected

#Test case 3  - Login button visibility
def test_login_button(setup):
    driver, Page = setup
    login_btn = WebDriverWait(driver,10).until(EC.visibility_of_element_located(Page.login_button))
    assert login_btn.is_displayed()
    #click the login button
    login_btn.click()
    WebDriverWait(driver, 10).until(EC.url_contains("/sign-in"))


#Test case 4 - Signup button
def test_signup_button(setup):
    driver, Page = setup
    Page.signup_button = (By.XPATH, "//button[text()='Sign up']")

    try:
        #Ensure page is loaded completely
        WebDriverWait(driver,15).until(lambda d: d.execute_script("return document.readyState")=="complete")
        #if we are on login page , go back to main page
        if "/sign-in" in driver.current_url:
            driver.back()
            WebDriverWait(driver, 10).until(lambda d: d.execute_script("return document.readyState")=="complete")
        #wait for signup button to appear and be clickable
        signup_btn = WebDriverWait(driver, 15).until(EC.element_to_be_clickable(Page.signup_button))
        #scroll into view and click
        driver.execute_script("arguments[0].scrollIntoView(true);", signup_btn)
        driver.execute_script("arguments[0].click();", signup_btn)
        #wait for navigation to sign-up page
        WebDriverWait(driver, 10).until(EC.url_contains("/register"))
    except TimeoutException:
        assert False, "Sign-up button or page did not appear as expected"

#Test Case 5 - Signup button Navigation
def test_signup_navigation(setup):
    driver, Page = setup
    Page.click_signup()
    time.sleep(5)
    assert "register" in driver.current_url
    driver.back()

#Test case 6 - Login with valid credentials
def test_login_valid(setup):
    driver, Page = setup
    Page.click_login()
    time.sleep(5)
    Page.login("vidhyamoorthy2011@gmail.com", "Vidhya@1990")
    time.sleep(5)
    assert "Courses" in driver.page_source

#Test Case 7 - Login with Invalid credentials
def test_login_invalid(setup):
    driver, Page = setup
    Page.click_login()
    time.sleep(5)
    Page.login("abcd@gmail.com", "new123")
    time.sleep(5)
    assert "error" in driver.page_source

#Test case 8 - Menu Validation
def test_menu_items(setup):
    driver, Page = setup

    live_classes = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Page.Live_classes_menu))
    courses = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Page.Courses_menu))
    practice = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Page.Practices_menu))
    time.sleep(5)
    assert live_classes.is_displayed() and live_classes.is_enabled()
    assert courses.is_displayed() and courses.is_enabled()
    assert practice.is_displayed() and practice.is_displayed()

#Test case 9 - chatbox presence
def test_chatbox_presence(setup):
    driver, Page = setup
    chatbot = WebDriverWait(driver, 20).until(EC.visibility_of_element_located(Page.dobby_chatbot))
    assert chatbot.is_displayed()


#Test case 10 - Logout
def test_logout(setup):
    driver, Page = setup
    Page.click_login()
    driver.refresh()
    Page.login("vidhyamoorthy2011@gmail.com", "Vidhya@1990")

    #wait for profile icon appear
    profile = WebDriverWait(driver, 15).until(EC.element_to_be_clickable(Page.profile_icon))
    profile.click()

    #wait for dropdown to fully open
    WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, "account-boxheader")))

    #click on signout button
    logout = WebDriverWait(driver, 15).until(EC.presence_of_element_located(Page.logout_button))
    driver.execute_script("arguments[0].click();", logout)













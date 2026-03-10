from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class GuviPage:

    login_button = (By.ID, "login-btn")
    signup_button = (By.XPATH, "//button[text()='Sign up']")

    email = (By.ID, "email")
    password = (By.ID, "password")
    login_submit = (By.ID, "login-btn")

    Live_classes_menu = (By.XPATH, "//p[text()='LIVE Classes']")
    Courses_menu = (By.XPATH, "//p[text()='Courses']")
    Practices_menu = (By.XPATH, "//p[text()='Practice']")
    dobby_chatbot = (By.XPATH, "//span[@id='zs_fl_chat']")
    profile_icon = (By.XPATH, "//img[contains(@class, 'gravatar')]//parent::div")
    logout_button = (By.XPATH, "(//p[normalize-space()='Sign Out']/ancestor::div[@id='signout'])[1]")



    def __init__(self, driver):
        self.driver = driver

    def open_site(self):
        self.driver.get("https://www.guvi.in/")


    def click_login(self):
        self.driver.find_element(*self.login_button).click()

    def click_signup(self):
        self.driver.find_element(*self.signup_button).click()

    def login(self, email, password):
        self.driver.find_element(*self.email).send_keys(email)
        self.driver.find_element(*self.password).send_keys(password)
        self.driver.find_element(*self.login_submit).click()
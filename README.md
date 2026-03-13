**GUVI Website Automation Testing**

**Project Title:**

Automated Testing of GUVI Web application using Selenium & Python.

--------------------------------------------------------------------
**PROJECT Description:**

This Project automates end to end functional test cases for the GUVI platform including:

1. URL & Title validation.
2. Login & Signup flows
3. Menu navigation
4. Chatbox presence
5. Logout functionality

The framework is built with scalability, readability and maintainability in mind.

------------------------------------------------------------------------------------------
**Project Objective:**
* Automate functional testing of the GUVI website
* Validate important UI elements and workflows
* Implement a structured automation framework.
* Generate HTML test execution reports
* Demonstrate automation testing best practices

---------------------------------------------------------------------------
**Tools & Technologies Used:**

1.Python

2.Selenium Webdriver

3.Pytest

4.Page Object Model

5.HTML Test reports

6.Github

7.Chrome driver

---------------------------------------------------------------------
**Project Structure:**

Automation-Testing-GUVI

Pages
* guvi_page.py

Tests

   *test_url_launch.py

   *test_title.py 

   *test_login.py

   *test_menu.py

   *test_chatbot.py

   *test_logout.py

**Reports**

report.html

requirements.txt

README.md

------------------------------------------------------------------------


**Test case Implemented:**

Test case 1 - Verify Application URL Launch

Scenario: Validate that the GUVI website loads successfully.

Expected Result : The homepage should open without errors.

---------------------------------------------------------------------
Test case 2 - Validate page Title

Scenario: Verify the title of the webpage.

Expected Result: The title should match the expected GUVI website title.

----------------------------------------------------------------------------
Test case 3 - Verify Login Button

Scenario: Validate that the login button is visible and clickable.

Expected Result: User should be able to click the Login button.

------------------------------------------------------------------------
Test case 4 - Verify Signup button

Scenario : Validate that the signup button is visible and clickable.

Expected Result: User should be able to click the signup button.

---------------------------------------------------------------------------------
Test case 5 - Verify Signup Navigation

Scenario: Verify Navigation to the sign-in page via Sign-up button

Expected Result : User should be able to navigate to the sign in page using sign up button.

---------------------------------------------------------------------------------------------

Test case 6 - Verify Login with valid credentials

Scenario: Validate Login with valid credentials.

Expected Result : User should successfully log into the account.

---------------------------------------------------------------------------------------

Test case 7 - Invalid Login Validation

Scenario: Attempt login with invalid credentials.

Expected Result : Error message should be displayed

---------------------------------------------------------------------------
Test case 8 - Menu Items validation

Scenario: verify navigation menu items.

Expected Result : All menu items should be visible and accessible.

---------------------------------------------------------------------------
Test case 9 - Validate Dobby chatbot

Scenario: Verify the presence of the GUVI Dobby chatbot

Expected Result : Chat assistant widget should be displayed.

--------------------------------------------------------------------------------------
Test case 10 - Logout Functionality

Scenario: validate User logout

Expected Result : User should be redirected to the login page

--------------------------------------------------------------------------------

**How to Run the Project:**

step 1: Install required packages

pip install -r requirements.txt

step 2: Run the test cases

pytest -v

Step 3: To Generate HTML test report

pytest --html=report.html

--------------------------------------------------------------
**Test Execution Report:**

The HTML report can be accessed using the following Google drive link:


-------------------------------------------------------------------------------


**Author**

Vidhya.M

Automation Testing Project Submission



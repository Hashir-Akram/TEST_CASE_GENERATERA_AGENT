# Login Page Automation Test Suite

## 1. Test Scenarios

### Test Case 1: Valid Login
- **Description**: Verify that a user can successfully log in with valid credentials
- **Steps**:
  1. Navigate to the login page
  2. Enter valid username
  3. Enter valid password
  4. Click the login button
- **Expected Result**: User is redirected to the dashboard page

### Test Case 2: Invalid Login
- **Description**: Verify that login fails with invalid credentials
- **Steps**:
  1. Navigate to the login page
  2. Enter invalid username
  3. Enter invalid password
  4. Click the login button
- **Expected Result**: Error message is displayed, user remains on login page

### Test Case 3: Empty Username/Password
- **Description**: Verify that login fails when username or password fields are empty
- **Steps**:
  1. Navigate to the login page
  2. Leave username field empty, enter password
  3. Click the login button
  4. Enter username, leave password field empty
  5. Click the login button
- **Expected Result**: Appropriate error messages are displayed for empty fields

### Test Case 4: Dashboard Redirection After Login
- **Description**: Verify that after successful login, user is redirected to the dashboard
- **Steps**:
  1. Navigate to the login page
  2. Enter valid credentials
  3. Click the login button
  4. Verify the current URL and page elements
- **Expected Result**: User is redirected to the dashboard page with expected elements visible

## 2. Pytest Selenium Automation Script

### Project Structure
```
login_tests/
├── pages/
│   ├── __init__.py
│   ├── login_page.py
│   └── dashboard_page.py
├── tests/
│   ├── __init__.py
│   └── test_login.py
├── conftest.py
└── requirements.txt
```

### requirements.txt
```txt
pytest==7.4.0
selenium==4.15.0
webdriver-manager==4.0.1
pytest-html==4.1.1
```

### conftest.py
```python
"""
Configuration file for pytest fixtures and setup
"""
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="function")
def driver():
    """
    Fixture to initialize and return a Chrome WebDriver instance
    """
    # Set up Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Remove this line to run in headed mode
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")
    
    # Initialize the driver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    # Maximize window and set implicit wait
    driver.maximize_window()
    driver.implicitly_wait(10)
    
    yield driver
    
    # Teardown
    driver.quit()


@pytest.fixture(scope="session")
def base_url():
    """
    Fixture to provide the base URL for the application
    """
    return "https://example.com"  # Replace with actual application URL
```

### pages/login_page.py
```python
"""
Page Object Model for the Login Page
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    """
    Page Object for the Login page
    """
    
    # Locators
    USERNAME_INPUT = (By.ID, "username")  # Update with actual locator
    PASSWORD_INPUT = (By.ID, "password")  # Update with actual locator
    LOGIN_BUTTON = (By.ID, "login-btn")  # Update with actual locator
    ERROR_MESSAGE = (By.CLASS_NAME, "error-message")  # Update with actual locator
    USERNAME_ERROR = (By.ID, "username-error")  # Update with actual locator
    PASSWORD_ERROR = (By.ID, "password-error")  # Update with actual locator
    
    def __init__(self, driver):
        """
        Initialize the LoginPage with a WebDriver instance
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    def load(self, base_url):
        """
        Navigate to the login page
        """
        self.driver.get(f"{base_url}/login")
    
    def enter_username(self, username):
        """
        Enter username in the username field
        """
        username_field = self.wait.until(
            EC.presence_of_element_located(self.USERNAME_INPUT)
        )
        username_field.clear()
        username_field.send_keys(username)
    
    def enter_password(self, password):
        """
        Enter password in the password field
        """
        password_field = self.wait.until(
            EC.presence_of_element_located(self.PASSWORD_INPUT)
        )
        password_field.clear()
        password_field.send_keys(password)
    
    def click_login_button(self):
        """
        Click the login button
        """
        login_button = self.wait.until(
            EC.element_to_be_clickable(self.LOGIN_BUTTON)
        )
        login_button.click()
    
    def get_error_message(self):
        """
        Get the error message text if present
        """
        try:
            error_element = self.wait.until(
                EC.visibility_of_element_located(self.ERROR_MESSAGE)
            )
            return error_element.text
        except:
            return None
    
    def get_username_error(self):
        """
        Get the username field error message
        """
        try:
            error_element = self.wait.until(
                EC.visibility_of_element_located(self.USERNAME_ERROR)
            )
            return error_element.text
        except:
            return None
    
    def get_password_error(self):
        """
        Get the password field error message
        """
        try:
            error_element = self.wait.until(
                EC.visibility_of_element_located(self.PASSWORD_ERROR)
            )
            return error_element.text
        except:
            return None
    
    def is_login_button_enabled(self):
        """
        Check if the login button is enabled
        """
        login_button = self.wait.until(
            EC.presence_of_element_located(self.LOGIN_BUTTON)
        )
        return login_button.is_enabled()
    
    def login(self, username, password):
        """
        Perform login with provided credentials
        """
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()
```

### pages/dashboard_page.py
```python
"""
Page Object Model for the Dashboard Page
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DashboardPage:
    """
    Page Object for the Dashboard page
    """
    
    # Locators
    DASHBOARD_HEADER = (By.TAG_NAME, "h1")  # Update with actual locator
    WELCOME_MESSAGE = (By.ID, "welcome-message")  # Update with actual locator
    LOGOUT_BUTTON = (By.ID, "logout-btn")  # Update with actual locator
    
    def __init__(self, driver):
        """
        Initialize the DashboardPage with a WebDriver instance
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    def is_dashboard_loaded(self):
        """
        Check if the dashboard page is loaded
        """
        try:
            self.wait.until(
                EC.presence_of_element_located(self.DASHBOARD_HEADER)
            )
            return True
        except:
            return False
    
    def get_dashboard_header_text(self):
        """
        Get the text of the dashboard header
        """
        header = self.wait.until(
            EC.visibility_of_element_located(self.DASHBOARD_HEADER)
        )
        return header.text
    
    def get_welcome_message(self):
        """
        Get the welcome message text
        """
        try:
            welcome_msg = self.wait.until(
                EC.visibility_of_element_located(self.WELCOME_MESSAGE)
            )
            return welcome_msg.text
        except:
            return None
    
    def click_logout(self):
        """
        Click the logout button
        """
        logout_button = self.wait.until(
            EC.element_to_be_clickable(self.LOGOUT_BUTTON)
        )
        logout_button.click()
```

### tests/test_login.py
```python
"""
Test cases for login functionality
"""
import pytest
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage


class TestLogin:
    """
    Test class for login functionality
    """
    
    def test_valid_login(self, driver, base_url):
        """
        Test Case 1: Valid login
        Verify that a user can successfully log in with valid credentials
        """
        # Initialize page objects
        login_page = LoginPage(driver)
        dashboard_page = DashboardPage(driver)
        
        # Navigate to login page
        login_page.load(base_url)
        
        # Perform login with valid credentials
        login_page.login("valid_username", "valid_password")  # Replace with actual valid credentials
        
        # Verify redirection to dashboard
        assert dashboard_page.is_dashboard_loaded(), "Dashboard page did not load after login"
        
        # Verify dashboard elements are present
        dashboard_header = dashboard_page.get_dashboard_header_text()
        assert "Dashboard" in dashboard_header, f"Expected 'Dashboard' in header, got: {dashboard_header}"
    
    def test_invalid_login(self, driver, base_url):
        """
        Test Case 2: Invalid login
        Verify that login fails with invalid credentials
        """
        # Initialize page objects
        login_page = LoginPage(driver)
        
        # Navigate to login page
        login_page.load(base_url)
        
        # Perform login with invalid credentials
        login_page.login("invalid_username", "invalid_password")
        
        # Verify error message is displayed
        error_message = login_page.get_error_message()
        assert error_message is not None, "Error message should be displayed for invalid login"
        assert "invalid" in error_message.lower() or "incorrect" in error_message.lower(), \
            f"Expected error message about invalid credentials, got: {error_message}"
        
        # Verify user remains on login page (URL should still contain 'login')
        current_url = driver.current_url
        assert "login" in current_url.lower(), f"User should remain on login page, current URL: {current_url}"
    
    def test_empty_username(self, driver, base_url):
        """
        Test Case 3a: Empty username
        Verify that login fails when username field is empty
        """
        # Initialize page objects
        login_page = LoginPage(driver)
        
        # Navigate to login page
        login_page.load(base_url)
        
        # Enter empty username and valid password
        login_page.enter_username("")
        login_page.enter_password("valid_password")
        login_page.click_login_button()
        
        # Verify username error message is displayed
        username_error = login_page.get_username_error()
        assert username_error is not None, "Username error message should be displayed for empty username"
        assert "required" in username_error.lower() or "empty" in username_error.lower() or "username" in username_error.lower(), \
            f"Expected username required error, got: {username_error}"
    
    def test_empty_password(self, driver, base_url):
        """
        Test Case 3b: Empty password
        Verify that login fails when password field is empty
        """
        # Initialize page objects
        login_page = LoginPage(driver)
        
        # Navigate to login page
        login_page.load(base_url)
        
        # Enter valid username and empty password
        login_page.enter_username("valid_username")
        login_page.enter_password("")
        login_page.click_login_button()
        
        # Verify password error message is displayed
        password_error = login_page.get_password_error()
        assert password_error is not None, "Password error message should be displayed for empty password"
        assert "required" in password_error.lower() or "empty" in password_error.lower() or "password" in password_error.lower(), \
            f"Expected password required error, got: {password_error}"
    
    def test_dashboard_redirection_after_login(self, driver, base_url):
        """
        Test Case 4: Dashboard redirection after login
        Verify that after successful login, user is redirected to the dashboard
        """
        # Initialize page objects
        login_page = LoginPage(driver)
        dashboard_page = DashboardPage(driver)
        
        # Navigate to login page
        login_page.load(base_url)
        
        # Perform login with valid credentials
        login_page.login("valid_username", "valid_password")  # Replace with actual valid credentials
        
        # Verify dashboard is loaded
        assert dashboard_page.is_dashboard_loaded(), "Dashboard page should be loaded after successful login"
        
        # Verify current URL is the dashboard URL
        current_url = driver.current_url
        assert "dashboard" in current_url.lower() or current_url.endswith("/"), \
            f"Expected dashboard URL, got: {current_url}"
        
        # Verify welcome message is displayed
        welcome_message = dashboard_page.get_welcome_message()
        assert welcome_message is not None, "Welcome message should be displayed on dashboard"
        assert "welcome" in welcome_message.lower(), f"Expected welcome message, got: {welcome_message}"
```

## 3. Assertions Summary

The test suite includes the following assertions:

1. **Valid Login Assertions**:
   - Dashboard page loads successfully after login
   - Dashboard header contains expected text (e.g., "Dashboard")

2. **Invalid Login Assertions**:
   - Error message is displayed for invalid credentials
   - Error message contains appropriate text (e.g., "invalid", "incorrect")
   - User remains on the login page (URL contains "login")

3. **Empty Username Assertions**:
   - Username error message is displayed
   - Error message indicates the field is required or empty

4. **Empty Password Assertions**:
   - Password error message is displayed
   - Error message indicates the field is required or empty

5. **Dashboard Redirection Assertions**:
   - Dashboard page is loaded after successful login
   - Current URL is the dashboard URL
   - Welcome message is displayed on the dashboard

## Running the Tests

To run the tests, execute the following command in the terminal:

```bash
# Install dependencies
pip install -r requirements.txt

# Run all tests
pytest tests/ -v

# Run with HTML report
pytest tests/ -v --html=report.html

# Run specific test
pytest tests/test_login.py::TestLogin::test_valid_login -v
```

## Notes

1. **Update Locators**: Replace the placeholder locators (ID, CLASS_NAME, etc.) with the actual locators from your application.

2. **Update Credentials**: Replace "valid_username" and "valid_password" with actual valid credentials for your application.

3. **Update Base URL**: Replace "https://example.com" with your actual application URL.

4. **Headless Mode**: The tests run in headless mode by default. Remove the headless option in conftest.py if you want to see the browser during test execution.

5. **Wait Strategies**: The code uses explicit waits for better reliability. Adjust wait times as needed for your application's performance.

This implementation follows the Page Object Model pattern, making the code maintainable and reusable. Each page has its own class with methods that represent user actions, and the test cases are clean and focused on specific scenarios.
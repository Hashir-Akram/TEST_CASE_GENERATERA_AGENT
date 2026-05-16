# User List Page Automation Test Suite

## 1. Test Scenarios

### Test Scenario 1: Verify User List Page Loads Successfully
- **Description**: Verify that the user list page loads without errors and displays the correct page title
- **Preconditions**: User is logged in and has access to the user list page
- **Steps**:
  1. Navigate to the user list page
  2. Verify page title is correct
  3. Verify page header is displayed
- **Expected Result**: Page loads successfully with correct title and header

### Test Scenario 2: Verify User List Table Structure
- **Description**: Verify that the user list table has the correct columns (username, address, number, pincode, city)
- **Preconditions**: User list page is loaded
- **Steps**:
  1. Check if table headers exist
  2. Verify all 5 required columns are present
  3. Verify column order is correct
- **Expected Result**: Table has all 5 required columns in the correct order

### Test Scenario 3: Verify User Data Display
- **Description**: Verify that user data is correctly displayed in the table
- **Preconditions**: User list page is loaded with at least one user record
- **Steps**:
  1. Check if user data rows are present
  2. Verify each row has data for all 5 fields
  3. Verify data is not empty for required fields
- **Expected Result**: User data is displayed correctly with no empty required fields

### Test Scenario 4: Verify Search Functionality
- **Description**: Verify that search functionality works correctly
- **Preconditions**: User list page is loaded with multiple user records
- **Steps**:
  1. Enter search term in search box
  2. Verify filtered results are displayed
  3. Verify search results contain the search term
- **Expected Result**: Search filters results correctly based on input

### Test Scenario 5: Verify Pagination Functionality
- **Description**: Verify that pagination works correctly when there are multiple pages of users
- **Preconditions**: User list page has more users than can fit on one page
- **Steps**:
  1. Check if pagination controls are visible
  2. Click on next page button
  3. Verify page number changes
  4. Verify different set of users is displayed
- **Expected Result**: Pagination controls work correctly and display different user sets

## 2. Pytest Selenium Automation Script

```python
"""
User List Page Test Automation
This module contains automated tests for the User List page functionality
using pytest and Selenium with Page Object Model pattern.
"""

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


class UserListPage:
    """
    Page Object Model for User List Page
    Encapsulates all elements and actions related to the user list page
    """
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        
        # Page elements locators
        self.PAGE_TITLE = (By.TAG_NAME, "h1")
        self.USER_TABLE = (By.ID, "user-table")
        self.TABLE_HEADERS = (By.XPATH, "//table[@id='user-table']//th")
        self.TABLE_ROWS = (By.XPATH, "//table[@id='user-table']//tbody/tr")
        self.SEARCH_BOX = (By.ID, "search-input")
        self.PAGINATION = (By.CLASS_NAME, "pagination")
        self.NEXT_PAGE_BUTTON = (By.XPATH, "//a[contains(text(), 'Next')]")
        self.PREV_PAGE_BUTTON = (By.XPATH, "//a[contains(text(), 'Previous')]")
        
        # Expected column headers
        self.EXPECTED_COLUMNS = ["Username", "Address", "Number", "Pincode", "City"]
    
    def load_page(self, url):
        """Navigate to the user list page"""
        self.driver.get(url)
    
    def is_page_loaded(self):
        """Verify if the user list page is loaded"""
        try:
            self.wait.until(EC.presence_of_element_located(self.PAGE_TITLE))
            return True
        except TimeoutException:
            return False
    
    def get_page_title(self):
        """Get the page title text"""
        return self.driver.find_element(*self.PAGE_TITLE).text.strip()
    
    def get_table_headers(self):
        """Get all table header texts"""
        headers = self.driver.find_elements(*self.TABLE_HEADERS)
        return [header.text.strip() for header in headers]
    
    def get_table_rows_count(self):
        """Get the number of rows in the user table"""
        rows = self.driver.find_elements(*self.TABLE_ROWS)
        return len(rows)
    
    def get_user_data_from_row(self, row_index):
        """Get user data from a specific row"""
        rows = self.driver.find_elements(*self.TABLE_ROWS)
        if row_index >= len(rows):
            return None
            
        cells = rows[row_index].find_elements(By.TAG_NAME, "td")
        return [cell.text.strip() for cell in cells]
    
    def search_users(self, search_term):
        """Enter search term and submit search"""
        search_box = self.wait.until(EC.presence_of_element_located(self.SEARCH_BOX))
        search_box.clear()
        search_box.send_keys(search_term)
        search_box.submit()
        
        # Wait for results to load
        self.wait.until(EC.staleness_of(search_box))
    
    def is_pagination_visible(self):
        """Check if pagination controls are visible"""
        try:
            return self.driver.find_element(*self.PAGINATION).is_displayed()
        except NoSuchElementException:
            return False
    
    def click_next_page(self):
        """Click on the next page button"""
        next_button = self.wait.until(EC.element_to_be_clickable(self.NEXT_PAGE_BUTTON))
        next_button.click()
        # Wait for page to load
        self.wait.until(EC.staleness_of(next_button))


class TestUserListPage:
    """
    Test class for User List Page functionality
    Contains all test cases for the user list page
    """
    
    @pytest.fixture(scope="class")
    def setup_driver(self):
        """Setup and teardown for WebDriver"""
        # Setup Chrome WebDriver
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        driver.maximize_window()
        
        yield driver
        
        # Teardown
        driver.quit()
    
    @pytest.fixture
    def user_list_page(self, setup_driver):
        """Create UserListPage instance"""
        return UserListPage(setup_driver)
    
    def test_user_list_page_loads_successfully(self, user_list_page):
        """
        Test Case: Verify User List Page Loads Successfully
        """
        # Navigate to user list page
        user_list_page.load_page("https://example.com/users")  # Replace with actual URL
        
        # Verify page is loaded
        assert user_list_page.is_page_loaded(), "User list page failed to load"
        
        # Verify page title
        page_title = user_list_page.get_page_title()
        assert page_title == "User List", f"Expected 'User List', but got '{page_title}'"
    
    def test_user_list_table_structure(self, user_list_page):
        """
        Test Case: Verify User List Table Structure
        """
        # Navigate to user list page
        user_list_page.load_page("https://example.com/users")
        
        # Verify page is loaded
        assert user_list_page.is_page_loaded(), "User list page failed to load"
        
        # Verify table exists
        table = user_list_page.driver.find_element(*user_list_page.USER_TABLE)
        assert table.is_displayed(), "User table is not displayed"
        
        # Verify table headers
        actual_headers = user_list_page.get_table_headers()
        assert len(actual_headers) == 5, f"Expected 5 columns, but found {len(actual_headers)}"
        
        # Verify column names match expected
        for i, expected_header in enumerate(user_list_page.EXPECTED_COLUMNS):
            assert actual_headers[i] == expected_header, \
                f"Column {i+1}: Expected '{expected_header}', but got '{actual_headers[i]}'"
    
    def test_user_data_display(self, user_list_page):
        """
        Test Case: Verify User Data Display
        """
        # Navigate to user list page
        user_list_page.load_page("https://example.com/users")
        
        # Verify page is loaded
        assert user_list_page.is_page_loaded(), "User list page failed to load"
        
        # Verify there are user records
        rows_count = user_list_page.get_table_rows_count()
        assert rows_count > 0, "No user records found in the table"
        
        # Verify data in first few rows (check first 3 rows or all if less than 3)
        rows_to_check = min(3, rows_count)
        for i in range(rows_to_check):
            user_data = user_list_page.get_user_data_from_row(i)
            assert user_data is not None, f"Failed to get data from row {i+1}"
            assert len(user_data) == 5, f"Row {i+1} has {len(user_data)} columns, expected 5"
            
            # Verify required fields are not empty
            for j, field_value in enumerate(user_data):
                assert field_value != "", f"Field {user_list_page.EXPECTED_COLUMNS[j]} is empty in row {i+1}"
    
    def test_search_functionality(self, user_list_page):
        """
        Test Case: Verify Search Functionality
        """
        # Navigate to user list page
        user_list_page.load_page("https://example.com/users")
        
        # Verify page is loaded
        assert user_list_page.is_page_loaded(), "User list page failed to load"
        
        # Get initial row count
        initial_count = user_list_page.get_table_rows_count()
        
        # Perform search with a common term (adjust based on your test data)
        search_term = "john"  # This should be a term that exists in your test data
        user_list_page.search_users(search_term)
        
        # Verify search results are displayed
        search_results_count = user_list_page.get_table_rows_count()
        assert search_results_count > 0, "No search results found"
        
        # Verify that search results contain the search term in at least one field
        # This is a basic check - in a real scenario, you might want to verify specific fields
        found_in_results = False
        for i in range(min(3, search_results_count)):  # Check first 3 results
            user_data = user_list_page.get_user_data_from_row(i)
            if any(search_term.lower() in field.lower() for field in user_data):
                found_in_results = True
                break
        
        assert found_in_results, f"Search term '{search_term}' not found in any result field"
    
    def test_pagination_functionality(self, user_list_page):
        """
        Test Case: Verify Pagination Functionality
        """
        # Navigate to user list page
        user_list_page.load_page("https://example.com/users")
        
        # Verify page is loaded
        assert user_list_page.is_page_loaded(), "User list page failed to load"
        
        # Check if pagination is visible (only test if there are multiple pages)
        if user_list_page.is_pagination_visible():
            # Get first page data (first row for comparison)
            first_page_first_row = user_list_page.get_user_data_from_row(0)
            assert first_page_first_row is not None, "Failed to get first row data from first page"
            
            # Click next page
            user_list_page.click_next_page()
            
            # Verify we're on a different page by checking if first row is different
            second_page_first_row = user_list_page.get_user_data_from_row(0)
            assert second_page_first_row is not None, "Failed to get first row data from second page"
            
            # The first row should be different on the second page
            # (unless there's only one user, which would be an edge case)
            assert first_page_first_row != second_page_first_row, \
                "First row is the same on both pages, pagination may not be working correctly"
        else:
            # If pagination is not visible, we can't test it, but this is not a failure
            # In a real scenario, you might want to have test data that ensures pagination is visible
            pytest.skip("Pagination not visible, skipping pagination test")


if __name__ == "__main__":
    # This allows running the tests directly with python
    pytest.main(["-v", __file__])
```

## 3. Assertions Summary

The automation script includes the following key assertions:

1. **Page Load Assertions**:
   - `assert user_list_page.is_page_loaded()` - Verifies page loads successfully
   - `assert page_title == "User List"` - Verifies correct page title

2. **Table Structure Assertions**:
   - `assert table.is_displayed()` - Verifies table is visible
   - `assert len(actual_headers) == 5` - Verifies correct number of columns
   - `assert actual_headers[i] == expected_header` - Verifies column names match expected

3. **Data Display Assertions**:
   - `assert rows_count > 0` - Verifies there are user records
   - `assert len(user_data) == 5` - Verifies each row has 5 fields
   - `assert field_value != ""` - Verifies required fields are not empty

4. **Search Functionality Assertions**:
   - `assert search_results_count > 0` - Verifies search returns results
   - `assert found_in_results` - Verifies search term appears in results

5. **Pagination Assertions**:
   - `assert first_page_first_row != second_page_first_row` - Verifies different data on different pages

## Usage Instructions

1. Install required packages:
```bash
pip install pytest selenium webdriver-manager
```

2. Update the URL in the test methods to point to your actual user list page

3. Adjust the search term in the search test to match your test data

4. Run the tests:
```bash
pytest user_list_test.py -v
```

The script follows Page Object Model principles, includes comprehensive comments, and provides clean, readable automation code that can be easily maintained and extended.
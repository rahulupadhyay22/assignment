import logging
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
import time

# Configure logging
logging.basicConfig(filename="test_log.log", level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Configure Edge WebDriver
service = Service('msedgedriver.exe')  # Adjust the path to your msedgedriver.exe
driver = webdriver.Edge(service=service)

def functional_test():
    try:
        logging.info("Starting Functional Test: Search, Add to Cart, and Checkout")
        
        # Step 1: Open the website
        driver.get("http://automationpractice.com/")
        time.sleep(3)

        # Step 2: Search for a product
        search_box = driver.find_element(By.ID, "search_query_top")
        search_box.send_keys("T-shirt")
        search_box.submit()
        time.sleep(3)

        # Step 3: Add the product to the cart
        product = driver.find_element(By.CSS_SELECTOR, ".product_img_link")
        product.click()
        time.sleep(3)
        add_to_cart_button = driver.find_element(By.NAME, "Submit")
        add_to_cart_button.click()
        time.sleep(3)

        # Step 4: Proceed to checkout
        checkout_button = driver.find_element(By.LINK_TEXT, "Proceed to checkout")
        checkout_button.click()

        # Step 5: Validate product is in the cart
        cart_items = driver.find_elements(By.CLASS_NAME, "cart_item")
        assert len(cart_items) > 0, "No items in the cart!"
        logging.info("Product added to cart successfully.")
        
    except Exception as e:
        driver.save_screenshot(f"screenshot_functional_{int(time.time())}.png")
        logging.error(f"Functional Test failed: {e}")
    finally:
        driver.quit()
        logging.info("Functional Test completed.")


def login_test():
    try:
        logging.info("Starting Login Test")
        
        # Step 1: Go to login page
        driver.get("http://automationpractice.com/index.php?controller=authentication&back=my-account")
        time.sleep(3)

        # Step 2: Enter valid credentials
        email_input = driver.find_element(By.ID, "email")
        password_input = driver.find_element(By.ID, "passwd")
        email_input.send_keys("testmailwsw@gmail.com")
        password_input.send_keys("Testmail@1234")
        submit_login = driver.find_element(By.ID, "SubmitLogin")
        submit_login.click()
        time.sleep(3)

        # Step 3: Validate login success
        assert "My account" in driver.title, "Login failed!"
        logging.info("Login successful with valid credentials.")
        
        # Step 4: Try invalid credentials
        driver.get("http://automationpractice.com/index.php?controller=authentication&back=my-account")
        email_input = driver.find_element(By.ID, "email")
        password_input = driver.find_element(By.ID, "passwd")
        email_input.send_keys("invalid@test.com")
        password_input.send_keys("wrongpassword")
        submit_login.click()

        # Step 5: Validate error message
        error_message = driver.find_element(By.XPATH, "//div[@class='alert alert-danger']")
        assert "Authentication failed" in error_message.text, "Error message not displayed!"
        logging.info("Invalid login error message validated.")
        
    except Exception as e:
        driver.save_screenshot(f"screenshot_login_{int(time.time())}.png")
        logging.error(f"Login Test failed: {e}")
    finally:
        driver.quit()
        logging.info("Login Test completed.")


def ui_test():
    try:
        logging.info("Starting UI Test: Verifying Key UI Elements")
        
        # Step 1: Open the website
        driver.get("http://automationpractice.com/")

        # Step 2: Verify search bar is present
        search_bar = driver.find_element(By.ID, "search_query_top")
        assert search_bar.is_displayed(), "Search bar not found!"
        logging.info("Search bar is displayed.")

        # Step 3: Verify navigation menu is present
        nav_menu = driver.find_element(By.ID, "block_top_menu")
        assert nav_menu.is_displayed(), "Navigation menu not found!"
        logging.info("Navigation menu is displayed.")

        # Step 4: Verify footer is present
        footer = driver.find_element(By.ID, "footer")
        assert footer.is_displayed(), "Footer not found!"
        logging.info("Footer is displayed.")
        
    except Exception as e:
        driver.save_screenshot(f"screenshot_ui_{int(time.time())}.png")
        logging.error(f"UI Test failed: {e}")
    finally:
        driver.quit()
        logging.info("UI Test completed.")


def form_validation_test():
    try:
        logging.info("Starting Form Validation Test")
        
        # Step 1: Navigate to the contact form page
        driver.get("http://automationpractice.com/index.php?controller=contact")

        # Step 2: Fill in the form fields
        subject_heading = driver.find_element(By.ID, "id_contact")
        subject_heading.send_keys("Customer service")
        email_input = driver.find_element(By.ID, "email")
        email_input.send_keys("testmailwsw@gmail.com")
        message_input = driver.find_element(By.ID, "message")
        message_input.send_keys("This is a test message.")

        # Step 3: Submit the form
        submit_button = driver.find_element(By.ID, "submitMessage")
        submit_button.click()

        # Step 4: Validate successful submission
        success_message = driver.find_element(By.XPATH, "//p[@class='alert alert-success']")
        assert "Your message has been successfully sent" in success_message.text, "Form submission failed!"
        logging.info("Form submitted successfully.")
        
    except Exception as e:
        driver.save_screenshot(f"screenshot_form_{int(time.time())}.png")
        logging.error(f"Form Validation Test failed: {e}")
    finally:
        driver.quit()
        logging.info("Form Validation Test completed.")

if __name__ == "__main__":
    # Ensure Edge WebDriver is configured for all tests
    service = Service('msedgedriver.exe')  # Adjust the path to your msedgedriver.exe
    driver = webdriver.Edge(service=service)

    # Run the tests
    functional_test()
    login_test()
    ui_test()
    form_validation_test()

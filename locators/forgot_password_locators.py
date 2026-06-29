from selenium.webdriver.common.by import By

class ForgotPasswordLocators:
    EMAIL_INPUT = (By.XPATH, "//input[@name='name']")
    RECOVER_BUTTON = (By.XPATH, "//button[text()='Восстановить']")

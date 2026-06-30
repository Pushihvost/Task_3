from selenium.webdriver.common.by import By

class ResetPasswordLocators:
    PASSWORD_INPUT = (By.XPATH, "//input[@name='Введите новый пароль']")
    SHOW_PASSWORD_BUTTON = (By.XPATH, "//div[contains(@class, 'input__icon')]/*[local-name() = 'svg']")
    PASSWORD_FIELD_ACTIVE = (By.XPATH, "//div[contains(@class, 'input_status_active')]")
    SAVE_BTN = (By.XPATH, "//button[text()='Сохранить']")

    MODAL_WINDOW = (By.XPATH, "//div[@class='Modal_modal_overlay__x2ZCr']")

class ForgotPasswordLocators:
    EMAIL_INPUT = (By.XPATH, "//input[@name='name']")
    RECOVER_BUTTON = (By.XPATH, "//button[text()='Восстановить']")

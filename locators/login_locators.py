from selenium.webdriver.common.by import By

class LoginLocators:

    EMAIL_INPUT = (By.NAME, "name")
    PASSWORD_INPUT = (By.NAME, "Пароль")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")
    RECOVERY_PASSWORD_LINK = (By.XPATH, "//a[text()='Восстановить пароль']")
    REGISTER_LINK = (By.XPATH, "//a[text()='Зарегистрироваться']")

    MODAL_WINDOW = (By.XPATH, "//div[@class='Modal_modal_overlay__x2ZCr']")

from selenium.webdriver.common.by import By

class UserAccountLocators:

    LOGOUT_ACCOUNT = (By.XPATH, "//button[text()='Выход']")
    HISTORY_ORDERS = (By.XPATH, "//a[text()='История заказов']")
    ACCOUNT_PROFILE = (By.XPATH, ".//a[@href = '/account/profile']")

    ID_FIRST_ORDER_IN_HISTORY = (By.XPATH,  "//ul/li//p[contains(@class, 'text') and contains(@class, 'text_type_digits-default')]")

    MODAL_WINDOW = (By.XPATH, "//div[@class='Modal_modal_overlay__x2ZCr']")






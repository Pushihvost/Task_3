from selenium.webdriver.common.by import By

class MainLocators:

    USER_ACCOUNT_LINK = (By.XPATH, ".//a[@href = '/account']")

    BURGER_CONSTRUCTOR = (By.XPATH, "//p[text()='Конструктор']")
    HEADER_CONSTRUCTOR = (By.XPATH, "//h1[text()='Соберите бургер']")

    LENTA_ORDERS = (By.XPATH, "//p[text()='Лента Заказов']")
    LENTA_ORDERS_HEADER = (By.XPATH, "//h1[text()='Лента заказов']")

    FLUORESCENT_BUN = (By.XPATH, ".//p[text()='Флюоресцентная булка R2-D3']")
    INGREDIENT_DETAILS = (By.XPATH, ".//h2[contains(@class, 'Modal_modal__title') and contains(text(), 'Детали ингредиента')]")
    CLOSE_INGREDIENT_DETAILS = (By.XPATH, ".//section[contains(@class, 'Modal_modal_open')]//button[contains(@class, 'close')]")

    COUNTER_BUN = (By.XPATH, ".//*[@alt='Флюоресцентная булка R2-D3']/preceding-sibling::div/p")
    BURGER_BUSKET = (By.XPATH, "//ul[contains(@class, 'BurgerConstructor_basket__list')]")

    MAKE_ORDER = (By.XPATH, "//button[text()='Оформить заказ']")
    ID_ORDER_TEXT = (By.XPATH, "//p[text()='идентификатор заказа']")
    CLOSE_ORDER = (By.XPATH, "//button[contains(@class, 'Modal_modal__close_')]")

    MODAL_WINDOW = (By.XPATH, "//div[@class='Modal_modal_overlay__x2ZCr']")


from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
import allure

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Открыть страницу")
    def open(self, url):
        self.driver.get(url)

    @allure.step("Получить страницу")
    def get_url(self):
        return self.driver.current_url

    @allure.step("Проверить страницу")
    def check_url(self, url):
        self.wait.until(EC.url_contains(url))

    @allure.step("Найти элемент")
    def find_element(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))
    
    @allure.step("Нажать на элемент")
    def click_element(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    @allure.step("Ввести текст")
    def send_keys_element(self, locator, text):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    @allure.step("Проскролить до элемента")
    def scroll_to_element(self,locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

    @allure.step("Получить текст и вернуть его")
    def get_text(self, locator):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        return element.text

    @allure.step("Проверить, что элемент исчез")
    def is_invisible_element(self, locator):
        if self.wait.until(EC.invisibility_of_element_located(locator)):
            return True
        return False


    @allure.step("Метод для устранения непонятных и невидимых окон")
    def wait_overlay_disappear(self, locator):
        self.wait.until(
            lambda driver: all(
                not element.is_displayed()
                for element in driver.find_elements(*locator)
            )
        )


    @allure.step("Перетащить элемент")
    def drag_and_drop(self, source_locator, target_locator):
            src = self.find_element(source_locator)
            dst = self.find_element(target_locator)
            js_script = """
                        function simulateDragDrop(sourceNode, targetNode) {
                            var EVENT_TYPES = {
                                DRAG_END: 'dragend',
                                DRAG_START: 'dragstart',
                                DROP: 'drop',
                                DRAG_OVER: 'dragover'
                            };
                            function createCustomEvent(type) {
                                var event = new CustomEvent("CustomEvent");
                                event.initCustomEvent(type, true, true, null);
                                event.dataTransfer = {
                                    data: {},
                                    setData: function(type, val) {
                                        this.data[type] = val;
                                    },
                                    getData: function(type) {
                                        return this.data[type];
                                    }
                                };
                                return event;
                            }
                            function dispatchEvent(node, type, event) {
                                if (node.dispatchEvent) {
                                    return node.dispatchEvent(event);
                                }
                                if (node.fireEvent) {
                                    return node.fireEvent("on" + type, event);
                                }
                            }
                            var event = createCustomEvent(EVENT_TYPES.DRAG_START);
                            dispatchEvent(sourceNode, EVENT_TYPES.DRAG_START, event);
                            var dropEvent = createCustomEvent(EVENT_TYPES.DROP);
                            dropEvent.dataTransfer = event.dataTransfer;
                            dispatchEvent(targetNode, EVENT_TYPES.DROP, dropEvent);
                            var dragEndEvent = createCustomEvent(EVENT_TYPES.DRAG_END);
                            dragEndEvent.dataTransfer = event.dataTransfer;
                            dispatchEvent(sourceNode, EVENT_TYPES.DRAG_END, dragEndEvent);
                        }
                        simulateDragDrop(arguments[0], arguments[1]);
                    """
            self.driver.execute_script(js_script, src, dst)

    @allure.step('Клик по кнопке для скрытых модальных окон')
    def js_click(self, target):
        if isinstance(target, tuple):
            el = self.find_element(target)
        elif isinstance(target, WebElement):
            el = target
        else:
            raise TypeError("js_click expects locator or WebElement")
        self.driver.execute_script("arguments[0].click();", el)
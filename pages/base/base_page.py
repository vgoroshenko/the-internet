import time

from selenium.common.exceptions import NoSuchElementException, TimeoutException, NoAlertPresentException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.locators import UrlLocators
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select


class BasePage:
    def __init__(self, browser, url=UrlLocators.MAIN_URL, timeout=4):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)
        self.browser.delete_all_cookies()
        self.browser.maximize_window()
        self.open()

    def alert_is_present(self, timeout=2):
        try:
            WebDriverWait(self.browser, timeout).until(EC.alert_is_present())
        except TimeoutException:
            assert False, 'should be alert present, but no'

    def alert_is_not_present(self):
        try:
            self.browser.switch_to.alert
        except NoAlertPresentException:
            return True
        assert False, 'should be alert not present, but yes'

    def alert_dismiss(self):
        alert = self.browser.switch_to_alert()
        alert.dismiss()

    def alert_accept(self):
        alert = self.browser.switch_to.alert
        alert.accept()

    def drag_to_element(self, what, where):
        actions = ActionChains(self.browser)
        actions.drag_and_drop(self.browser.find_element(*what), self.browser.find_element(*where))
        actions.perform()

    def get_alert_text(self):
        alert = self.browser.switch_to.alert
        return alert.text

    def get_text(self, how, what):
        return self.browser.find_element(how, what).text

    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, [TimeoutException]). \
                until_not(EC.presence_of_element_located((how, what)) and EC.visibility_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def is_checked(self, how, what):
        return self.browser.find_element(how, what).is_selected()

    def is_element_present_timeout(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, [TimeoutException]). \
                until(EC.presence_of_element_located((how, what)) and EC.visibility_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True

    def is_element_displayed(self, elem):
        return True if elem.is_displayed() else False
        # try:
        #     self.browser.find_element(how, what).is_displayed()
        # except:
        #     return False
        # return True

    def is_not_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return True
        return False

    def has_class(self, how, what, clas):
        classes = self.browser.find_element(how, what).get_attribute("class")
        return True if clas in classes else False

    def click(self, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.element_to_be_clickable((what)))
        except NoSuchElementException:
            return False
        return what.click()

    def move_mouse_to_element(self, elem):
        action = ActionChains(self.browser)
        action.move_to_element(elem)
        action.perform()

    def hold_on_locator_and_move_to_target(self, how, what, target):
        action = ActionChains(self.browser)
        action.click_and_hold(self.browser.find_element(how, what))
        action.move_to_element(self.browser.find_element(*target))
        action.perform()

    def right_click(self, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.element_to_be_clickable((what)))
        except NoSuchElementException:
            return False
        action = ActionChains(self.browser)
        return action.context_click(what).perform()

    def select_element_with_value(self, how, what, value):
        select = Select(self.browser.find_element(how, what))
        select.select_by_value(value)

    def switch_to_frame(self, how, what):
        while True:
            try:
                self.browser.switch_to.frame(self.browser.find_element(how, what))
                break
            except NoSuchElementException:
                raise NoSuchElementException('Фрейм не найден')

    def switch_to_frame_with_locator(self, how, what, iframe):
        try:
            self.browser.switch_to.default_content()
            frame_found = False
            while not frame_found:
                frames = self.browser.find_elements(*iframe)
                for frame in frames:
                    self.browser.switch_to.frame(frame)
                    try:
                        locator_frame = self.browser.find_element(how, what)
                        self.browser.switch_to.frame(locator_frame)
                        frame_found = True
                        break
                    except NoSuchElementException:
                        self.browser.switch_to.default_content()
                if not frame_found:
                    raise NoSuchElementException('Фрейм с указанным локатором не найден')
        except NoSuchElementException as e:
            print('Ошибка:', str(e))

    def open(self):
        self.browser.get(self.url)

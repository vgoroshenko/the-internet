from pages.add_remove_page import AddRemove

def test_go_add_remove_page(browser):
    page = AddRemove(browser)
    page.go_to_module()
    page.should_be_add_remove_page_present()

def test_add_element(browser):
    page = AddRemove(browser)
    page.go_to_module()
    page.press_add_button()
    page.should_be_remove_button_present()

def test_remove_element(browser):
    page = AddRemove(browser)
    page.go_to_module()
    page.press_add_button()
    page.press_delete_button()
    page.should_removed_element()

def test_add_multiple_elements(browser):
    page = AddRemove(browser)
    page.go_to_module()
    page.press_add_buttont_count(2)
    page.should_be_present_remove_buttons_count(2)

def test_remove_multiple_elements(browser):
    page = AddRemove(browser)
    page.go_to_module()
    page.press_add_buttont_count(2)
    page.press_delete_button()
    page.press_delete_button()
    page.should_be_present_remove_buttons_count(0)


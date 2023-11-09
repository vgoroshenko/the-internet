from pages.inputs_page import Inputs


def test_go_to_page(browser):
    page = Inputs(browser)
    page.go_to_page()
    page.should_be_correct_page()

def test_change_number(browser):
    page = Inputs(browser)
    page.go_to_page()
    page.click_input()
    page.press_up(2)
    page.should_be_present_number(2)
    page.press_down(2)
    page.should_be_present_number(0)
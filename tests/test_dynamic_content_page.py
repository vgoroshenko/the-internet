from pages.dynamic_content_page import DynamicContent

def test_go_to_page(browser):
    page = DynamicContent(browser)
    page.go_to_page()
    page.should_be_correct_page()

def test_change_content(browser):
    page = DynamicContent(browser)
    page.go_to_page()
    page.should_be_changed_content_after_change()

def test_dont_changed_content(browser):
    page = DynamicContent(browser)
    page.go_to_page()
    page.change_content()
    page.should_be_not_changed_second_row_content()
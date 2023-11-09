from pages.basic_auth_page import BasicAuth

def test_unsuccessful_basic_auth_page(browser):
    page = BasicAuth(browser)
    page.go_to_failed_module()
    page.should_be_present_failed_message()
def test_success_basic_auth_page(browser):
    page = BasicAuth(browser)
    page.go_to_module()
    page.should_be_success_basic_auth_page()


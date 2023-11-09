from pages.hovers_page import Hover


def test_go_to_page(browser):
    page = Hover(browser)
    page.go_to_page()
    page.should_be_correct_page()

def test_show_profile_hover(browser):
    page = Hover(browser)
    page.go_to_page()
    page.mouse_move_to_profile(1)
    page.should_be_hover_profile_present(1)

def test_open_profile(browser):
    page = Hover(browser)
    page.go_to_page()
    page.click_profile(1)
    page.should_be_profile(1)

def test_all_profiles_hover_present(browser):
    page = Hover(browser)
    page.go_to_page()
    page.should_be_check_all_profile()
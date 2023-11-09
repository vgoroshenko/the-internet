from pages.infinity_scroll_page import InfinityScroll


def test_go_to_page(browser):
    page = InfinityScroll(browser)
    page.go_to_page()
    page.should_be_correct_page()

def test_scroll_page(browser):
    page = InfinityScroll(browser)
    page.go_to_page()
    page.should_be_scrolled()
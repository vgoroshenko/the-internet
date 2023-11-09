from pages.jquery_page import JQuery


def test_go_to_page(browser):
    page = JQuery(browser)
    page.go_to_page()
    page.should_be_correct_page()

def test_go_back_to_menu(browser):
    page = JQuery(browser)
    page.go_to_page()
    page.click_back_to_menu()
    page.should_be_menu_page()
    page.go_to_page()
    page.should_be_correct_page()

def test_download_pdf(browser):
    page = JQuery(browser)
    page.go_to_page()
    page.click_downloads()
    page.download_pdf()
    page.should_be_downloaded_file_extend('pdf')
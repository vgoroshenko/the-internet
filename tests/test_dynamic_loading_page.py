from pages.dynamic_loading_page import DynamicallyLoaded

def test_go_to_page(browser):
    page = DynamicallyLoaded(browser)
    page.go_to_page()
    page.should_be_correct_page()

def test_first_example_show_load_bar(browser):
    page = DynamicallyLoaded(browser)
    page.go_to_page()
    page.click_example_1()
    page.click_start()
    page.should_be_load_bar_present()

def test_first_example_final_text_present(browser):
    page = DynamicallyLoaded(browser)
    page.go_to_page()
    page.click_example_1()
    page.click_start()
    page.should_be_load_bar_disappeared()
    page.should_be_hello_word_present()

def test_second_example_show_load_bar(browser):
    page = DynamicallyLoaded(browser)
    page.go_to_page()
    page.click_example_2()
    page.click_start()
    page.should_be_load_bar_present()

def test_second_example_final_text_present(browser):
    page = DynamicallyLoaded(browser)
    page.go_to_page()
    page.click_example_2()
    page.click_start()
    page.should_be_load_bar_disappeared()
    page.should_be_hello_word_present()

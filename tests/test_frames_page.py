from pages.frames_page import Frames

def test_go_to_page(browser):
    page = Frames(browser)
    page.go_to_page()
    page.should_be_correct_page()

def test_nested_frames(browser):
    page = Frames(browser)
    page.go_to_page()
    page.click_nested_frames()
    page.should_be_left_frame()

def test_iframes(browser):
    page = Frames(browser)
    page.go_to_page()
    page.click_i_frames()
    page.write_text_in_iframe()
    page.should_be_test_text_in_iframe()
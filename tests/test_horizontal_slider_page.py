from pages.horizonral_slider_page import HorizontalSlider


def test_go_to_page(browser):
    page = HorizontalSlider(browser)
    page.go_to_page()
    page.should_be_correct_page()


def test_slider(browser):
    page = HorizontalSlider(browser)
    page.go_to_page()
    page.move_slider_max()
    page.should_be_value_5()
    page.move_slider_min()
    page.should_be_min_slider_value()
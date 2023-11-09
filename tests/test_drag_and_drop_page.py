import pytest

from pages.drag_and_drop_page import DragAndDrop

def test_go_to_page(browser):
    page = DragAndDrop(browser)
    page.go_to_page()
    page.should_be_correct_page()

@pytest.mark.xfail #('drag and drop dont work in selenoid')
def test_drag_and_drop(browser):
    page = DragAndDrop(browser)
    page.go_to_page()
    page.drag_to_element_b()
    page.should_be_change_text()

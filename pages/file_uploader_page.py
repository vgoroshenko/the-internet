from pages.locators import FileUploadLocators, BasePageLocators
from pages.base.base_page import BasePage


class FileUploader(BasePage):

    def go_to_page(self):
        link = self.browser.find_element(*FileUploadLocators.LOADED_PAGE)
        link.click()

    def click_upload(self):
        submit_button = self.browser.find_element(*FileUploadLocators.FILE_SUBMIT)
        submit_button.click()

    def drag_and_drop_file(self):
        JS_DROP_FILE = """
        var target = arguments[0],
            offsetX = arguments[1],
            offsetY = arguments[2],
            document = target.ownerDocument || document,
            window = document.defaultView || window;
        
        var input = document.createElement('INPUT');
        input.type = 'file';
        input.onchange = function () {
          var rect = target.getBoundingClientRect(),
              x = rect.left + (offsetX || (rect.width >> 1)),
              y = rect.top + (offsetY || (rect.height >> 1)),
              dataTransfer = { files: this.files };
        
          ['dragenter', 'dragover', 'drop'].forEach(function (name) {
            var evt = document.createEvent('MouseEvent');
            evt.initMouseEvent(name, !0, !0, window, 0, 0, 0, x, y, !1, !1, !1, !1, 0, null);
            evt.dataTransfer = dataTransfer;
            target.dispatchEvent(evt);
          });
        
          setTimeout(function () { document.body.removeChild(input); }, 25);
        };
        document.body.appendChild(input);
        return input;
        """
        upload_element = self.browser.find_element(*FileUploadLocators.FILE_UPLOAD_DRAG_AND_DROP)
        file_input = self.browser.execute_script(JS_DROP_FILE, upload_element, 0, 0)
        path = './tests/test_data/some-file.txt'
        file_input.send_keys(path)

    def upload_file(self):
        file_input = self.browser.find_element(*FileUploadLocators.FILE_UPLOAD)
        file_input.send_keys('./tests/test_data/some-file.txt')
        self.click_upload()

    def upload_file_drag_and_drop(self):
        file_path = './tests/test_data/some-file.txt'
        upload_element = self.browser.find_element(*FileUploadLocators.FILE_UPLOAD_DRAG_AND_DROP)
        # action_chains = ActionChains(self.browser)
        # action_chains.drag_and_drop(file_path, upload_element).perform()
        upload_element.send_keys(file_path)

    def should_be_correct_page(self):
        text = self.get_text(*BasePageLocators.PAGE_NAME)
        correct_text = 'File Uploader'
        assert correct_text in text, f'should be {correct_text}, but "{text}"'

    def should_be_uploaded_file(self):
        uploaded_text = self.get_text(*FileUploadLocators.UPLOADED_FILE)
        assert 'some-file.txt' in uploaded_text, 'should be uploaded file, but not'

    def should_be_uploaded_file_drag(self):
        uploaded_text = self.get_text(*FileUploadLocators.UPLOADED_FILE_ERROR_SUMMARY)
        assert 'NoMethodError' in uploaded_text, 'should be uploaded file, but not'

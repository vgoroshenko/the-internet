from pages.file_downloader_page import FileDownloader

def test_go_to_page(browser):
    page = FileDownloader(browser)
    page.go_to_page()
    page.should_be_correct_page()


def test_file_download(browser):
    page = FileDownloader(browser)
    page.go_to_page()
    page.download_file()
    page.should_be_downloaded_file()

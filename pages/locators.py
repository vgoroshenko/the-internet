from selenium.webdriver.common.by import By


class ABPageLocators:
    NO_AB_TEXT = (By.CSS_SELECTOR, 'h3')
    AB_PAGE = (By.XPATH, "//a[contains(@href, 'abtest')]")


class AddRemoveLocators:
    ADD_REMOVE_PAGE = (By.XPATH, "//a[contains(@href, '/add_remove_elements/')]")
    ADD_BUTTON = (By.CSS_SELECTOR, "button[onclick='addElement()']")
    DELETE_BUTTON = (By.CSS_SELECTOR, ".added-manually")
    DELETE_BUTTONS = (By.CSS_SELECTOR, "#elements")


class BasicAuthLocators:
    BASIC_AUTH_PAGE = (By.XPATH, "//a[contains(@href, 'basic')]")
    CONGRAT_MESSAGE = (By.CSS_SELECTOR, 'p')
    FAILED_MESSAGE = (By.CSS_SELECTOR, 'body')


class BrokenImagesLocators:
    BROKEN_IMAGE_PAGE = (By.XPATH, "//a[contains(@href, '/broken_images')]")
    PAGE_NAME = (By.CSS_SELECTOR, 'h3')


class ChallengingDomLocators:
    PAGE_NAME = (By.CSS_SELECTOR, 'h3')
    CHALLENGING_DOM_PAGE = (By.XPATH, "//a[@href='/challenging_dom']")
    FIRST_BUTTON = (By.CSS_SELECTOR, "[class='button']")
    SECOND_BUTTON = (By.CSS_SELECTOR, ".button.alert")
    THIRD_BUTTON = (By.CSS_SELECTOR, ".button.success")
    ANSWER = (By.CSS_SELECTOR, '#canvas')


class CheckboxesLocators:
    PAGE_NAME = (By.CSS_SELECTOR, 'h3')
    CHECKBOXES_PAGE = (By.XPATH, "//a[@href='/checkboxes']")
    FIRST_CHECKBOX = (By.CSS_SELECTOR, 'input:nth-of-type(1)')
    SECOND_CHECKBOX = (By.CSS_SELECTOR, 'input:nth-of-type(2)')


class ContextMenuLocators:
    PAGE_NAME = (By.CSS_SELECTOR, 'h3')
    CONTEXT_PAGE = (By.XPATH, "//a[@href='/context_menu']")
    BOX_BUTTON = (By.CSS_SELECTOR, '#hot-spot')


class BasePageLocators:
    PAGE_NAME = (By.CSS_SELECTOR, 'h3')


class DisappearingElementsLocators:
    DISAPPERATING_PAGE = (By.XPATH, "//a[@href='/disappearing_elements']")
    BUTTON_LIST = (By.XPATH, '//li//a')


class DragAndDropLocators:
    DRAG_AND_DROP_PAGE = (By.XPATH, "//a[@href='/drag_and_drop']")
    BOX_A = (By.CSS_SELECTOR, '#column-a')
    BOX_B = (By.CSS_SELECTOR, '#column-b')


class DropdownLocators:
    DROPDOWN_PAGE = (By.XPATH, "//a[@href='/dropdown']")
    DROPDOWN_BUTTON = (By.CSS_SELECTOR, '#dropdown')
    DROPDOWN_FIRST_ELEMENT = (By.CSS_SELECTOR, "option[value='1']")
    DROPDOWN_SECOND_ELEMENT = (By.CSS_SELECTOR, "option[value='2']")


class DynamicContentLocators:
    DYNAMIC_CONTENT_PAGE = (By.XPATH, "//a[@href='/dynamic_content']")
    CHANGE_CONTENT_BUTTON = (By.XPATH, "//a[contains(@href, 'with')]")
    ALL_TEXT_CONTENT_ELEMENTS = (By.CSS_SELECTOR, '#content:nth-child(1) .row .large-10')


class DynamicallyLoadedLocators:
    DYNAMICALLY_LOADED_PAGE = (By.XPATH, "//a[@href='/dynamic_loading']")
    EXAMPLE_ONE_BUTTON = (By.XPATH, "//a[@href='/dynamic_loading/1']")
    EXAMPLE_TWO_BUTTON = (By.XPATH, "//a[@href='/dynamic_loading/2']")
    START_BUTTON = (By.CSS_SELECTOR, "button")
    LOADING_BAR = (By.CSS_SELECTOR, '#loading')
    FINISH_TEXT = (By.CSS_SELECTOR, '#finish')


class EntryAdLocators:
    LOADED_PAGE = (By.XPATH, "//a[@href='/entry_ad']")
    CLOSE_BUTTON = (By.CSS_SELECTOR, "div[class='modal-footer']")
    RE_ENABLE_BUTTON = (By.CSS_SELECTOR, '#restart-ad')
    POPUP = (By.CSS_SELECTOR, '.modal')


class ExitIntentLocators:
    LOADED_PAGE = (By.XPATH, "//a[@href='/exit_intent']")
    CLOSE_BUTTON = (By.CSS_SELECTOR, "div[class='modal-footer']")
    POPUP = (By.CSS_SELECTOR, '.modal')


class FileDownloadLocators:
    LOADED_PAGE = (By.XPATH, "//a[@href='/download']")
    FILE = (By.CSS_SELECTOR, "div[class='example'] a")


class FileUploadLocators:
    LOADED_PAGE = (By.XPATH, "//a[@href='/upload']")
    FILE_UPLOAD = (By.CSS_SELECTOR, "#file-upload")
    FILE_SUBMIT = (By.CSS_SELECTOR, '#file-submit')
    FILE_UPLOAD_DRAG_AND_DROP = (By.CSS_SELECTOR, '#drag-drop-upload')
    UPLOADED_FILE = (By.CSS_SELECTOR, '#uploaded-files')
    UPLOADED_FILE_ERROR_SUMMARY = (By.CSS_SELECTOR, '#summary')


class FormAuthenticationLocators:
    PAGE_NAME = (By.CSS_SELECTOR, "h2")
    LOADED_PAGE = (By.XPATH, "//a[@href='/login']")
    FIELD_USERNAME = (By.CSS_SELECTOR, '#username')
    FIELD_PASSWORD = (By.CSS_SELECTOR, '#password')
    BUTTON_LOGIN = (By.CSS_SELECTOR, '.radius')
    BUTTON_LOGOUT = (By.CSS_SELECTOR, '.button.secondary')
    BUTTON_CLOSE_MESSAGE = (By.CSS_SELECTOR, '.close')
    SUCCESS_LOGIN_PAGE = (By.CSS_SELECTOR, "h2")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '.flash.success')
    ERROR_MESSAGE = (By.CSS_SELECTOR, '.flash.error')


class FramesLocators:
    LOADED_PAGE = (By.XPATH, "//a[@href='/frames']")
    NESTED_FRAMES_BUTTON = (By.XPATH, "//a[@href='/nested_frames']")
    IFRAMES_BUTTON = (By.XPATH, "//a[@href='/iframe']")
    FRAMES = (By.CSS_SELECTOR, "frame")
    FRAME_LEFT = (By.CSS_SELECTOR, 'frame[name="frame-left"]')
    FRAME_BODY = (By.CSS_SELECTOR, 'body')
    FIELD_IFRAME = (By.CSS_SELECTOR, '#tinymce > p')
    IFRAMES = (By.TAG_NAME, 'iframe')
    IFRAME_ID = (By.CSS_SELECTOR, '#mce_0_ifr')


class GeolocationLocators:
    LOADED_PAGE = (By.XPATH, "//a[@href='/geolocation']")
    BUTTON_WHERE_I_AM = (By.CSS_SELECTOR, '.example button')
    BUTTON_GOOGLE_MAP = (By.CSS_SELECTOR, '#map-link > a')
    LATITUDE_COORD = (By.CSS_SELECTOR, '#lat-value')
    LONGITUDE_COORD = (By.CSS_SELECTOR, '#long-value')

class HorizontalSliderLocators:
    LOADED_PAGE = (By.XPATH, "//a[@href='/horizontal_slider']")
    SLIDER = (By.CSS_SELECTOR, '.sliderContainer > input')
    SLIDER_VALUE = (By.CSS_SELECTOR, '#range')

class HoverLocators:
    LOADED_PAGE = (By.XPATH, "//a[@href='/hovers']")
    PERSONS = (By.CSS_SELECTOR, '.figure')
    PERSONS_NAME = (By.CSS_SELECTOR, '.figcaption h5')
    PERSONS_LINK = (By.CSS_SELECTOR, '.figcaption a')

class InfinityScrollLocators:
    LOADED_PAGE = (By.XPATH, "//a[@href='/infinite_scroll']")
    SCROLLED_ROW = (By.CSS_SELECTOR, '.jscroll-added')

class InputsLocators:
    LOADED_PAGE = (By.XPATH, "//a[@href='/inputs']")
    INPUT = (By.CSS_SELECTOR, '[type="number"]')

class JQueryUIMenusLocators:
    LOADED_PAGE = (By.XPATH, "//a[contains(@href, '/jqueryui/menu')]")
    BUTTON_ENABLED = (By.CSS_SELECTOR, '#ui-id-2')
    BUTTON_DOWNLOADS = (By.CSS_SELECTOR, '#ui-id-4')
    BUTTON_BACK = (By.CSS_SELECTOR, '#ui-id-5')
    BUTTON_PDF = (By.CSS_SELECTOR, '#ui-id-5')
    BUTTON_CSV = (By.CSS_SELECTOR, '#ui-id-5')
    BUTTON_EXCEL = (By.CSS_SELECTOR, '#ui-id-5')


class UrlLocators:
    MAIN_URL = "http://172.17.0.1:5000/"
     #MAIN_URL = "http://localhost:5000/"

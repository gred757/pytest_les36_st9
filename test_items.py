from selenium.webdriver.common.by import By
from selenium.common.exceptions import  NoSuchElementException

def test_find_add_item_to_cart(browser):
    try:
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
        browser.get(link)
        el_btn = browser.find_element(By.CLASS_NAME, 'btn-add-to-basket')
        assert el_btn, 'Add product button not found'
    except NoSuchElementException as e:
        print("Add product button not found!", e)


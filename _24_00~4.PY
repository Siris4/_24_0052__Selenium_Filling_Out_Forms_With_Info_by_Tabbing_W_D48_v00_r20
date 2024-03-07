
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time

url = "https://secure-retreat-92358.herokuapp.com/"
FIRST_NAME = "Kevlon"
LAST_NAME = "mARVIN"
EMAIL = "kevlon.mARVIN@gmail.com"

# opening Chrome:
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)   # and keeping Chrome open (as long as: driver.quit() is inactive at the bottom of the code.
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get(url)


# html_block_for_search_bar = '<input class="cdx-text-input__input" accesskey="f" autocapitalize="sentences" title="Search Wikipedia [alt-shift-f]" placeholder="Search Wikipedia" aria-label="Search Wikipedia" name="search" role="combobox" autocomplete="off" aria-autocomplete="list" aria-controls="cdx-typeahead-search-menu-0" aria-expanded="false" type="search" size="1">'

# FULL XPATH:
HTML_input_element = '<input name="fName" type="text" class="form-control top" placeholder="First Name" required="" autofocus="">'
XPath_expression_that_represents_a_path_to_locate_a_specific_element_within_an_HTML_document = '/html/body/form/input[1]'
# working_format: searchbar_for_wikipedia = driver.find_element(By.XPATH, value='//input[@class="cdx-text-input__input"]')   # removed: * and [title="Search Wikipedia [alt-shift-f]"')   # added: @ in front of class


top_field_of_form = driver.find_element(By.XPATH, value="//input[contains(@class, 'form-control')][@placeholder='First Name']")
top_field_of_form.click() # ensuring the field is focused

# time.sleep(1)

top_field_of_form.send_keys(FIRST_NAME)
# top_field_of_form.send_keys(Keys.TAB)  # or ("Python" + Keys.ENTER)
driver.switch_to.active_element.send_keys(Keys.TAB)

# time.sleep(1)

# top_field_of_form.send_keys(Keys.TAB)

driver.switch_to.active_element.send_keys(LAST_NAME)
# top_field_of_form.send_keys(Keys.TAB)  # or ("Python" + Keys.ENTER)
driver.switch_to.active_element.send_keys(Keys.TAB)

# time.sleep(1)

# top_field_of_form.send_keys(Keys.TAB)

driver.switch_to.active_element.send_keys(EMAIL + Keys.ENTER)

# searchbar_for_wikipedia.send_keys(Keys.SHIFT)
# searchbar_for_wikipedia.send_keys(Keys.BACKSPACE)
# searchbar_for_wikipedia.send_keys(Keys.SPACE)
# searchbar_for_wikipedia.send_keys(Keys.HOME)
# searchbar_for_wikipedia.send_keys(Keys.F5)


# time.sleep(1)

# html_doc_for_search_button = '<button class="cdx-button cdx-button--action-default cdx-button--weight-normal cdx-button--size-medium cdx-button--framed cdx-search-input__end-button">Search</button>'

# Use this method:
# searchbar_for_wikipedia.send_keys(Keys.ENTER) # or ("Python" + Keys.ENTER)

#OR the one below, but not both at the same time:

# search_go_button = driver.find_element(By.XPATH, value='//button[contains(@class,"cdx-search-input__end-button")]')
#previous code, not working: value='//*[<button class="cdx-button cdx-button--action-default cdx-button--weight-normal cdx-button--size-medium cdx-button--framed cdx-search-input__end-button">Search</button>]')
# time.sleep(1)

# search_go_button.click()


# closes the active and single tab (not all of them, and doesn't necessarily shutdown the Chrome browser):
# driver.close()

# quits the entire web browser INCLUDING all of the tabs that are still OPEN (the moment it loads the webpage):
# driver.quit()    # COMMENT THIS OUT TO KEEP IT OPEN!!!!

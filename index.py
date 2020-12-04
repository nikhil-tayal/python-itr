from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from getpass import getpass
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www1.incometaxindiaefiling.gov.in/e-FilingGS/Registration/RegistrationHome.html?lang=eng")

driver.find_element_by_link_text("Login").click()

inputElement = driver.find_element_by_id("Login_userName")
inputElement.send_keys('ABCDE1234E')
inputElement = driver.find_element_by_id("Login_password")
inputElement.send_keys('@password@')
checkboxElement = driver.find_element_by_id("otpLogin")
checkboxElement.click()
driver.find_element_by_id("button1").click()

driver.find_element_by_class_name("btnOrange").click()

# OTP Enter
otp_input = input("Enter the OTP")
inputElement = driver.find_element_by_id("OTPLoginValidate_otp")
inputElement.send_keys(otp_input)

# OTP PAGE Need for otp 3 times try implementation

driver.find_element_by_class_name("btnOrange").click()
driver.implicitly_wait(10)


# Login done

element_to_hover_over = driver.find_element_by_css_selector("a.top")

hover = ActionChains(driver).move_to_element(element_to_hover_over)
hover.perform()

driver.find_element_by_link_text("Download Pre-filled XML").click()

# XML Page opened

# select = Select(driver.find_element_by_id('asYear'))
# select = Select(driver.find_element_by_id('returnType'))
download_link = driver.find_element_by_id("continueButton")

driver.find_element_by_xpath(
    "//select[@name='asYear']/option[text()='2018-19']").click()
driver.implicitly_wait(1)

driver.find_element_by_xpath(
    "//select[@name='formId']/option[text()='ITR-1']").click()
download_link.click()
# select.select_by_value('2019')

driver.find_element_by_id("UpdateContactDtls_0").click()  # Download XML button

# POP-UP WILL OPEN
driver.implicitly_wait(2)

driver.find_element_by_id("prefillConcentFlag").click()  # checkbox
driver.implicitly_wait(1)

driver.find_element_by_css_selector(
    ".ui-dialog.ui-widget>#prefillConcentDialog>div>#UpdateContactDtls_0.btnOrange").click()  # Continue

# select.select_by_value('ITR-1')
# driver.implicitly_wait(1)

# download_link.click()
# driver.implicitly_wait(2)


# select.select_by_value('2018')
# select.select_by_value('ITR-1')
# download_link.click()
# driver.implicitly_wait(2)


# select.select_by_value('2017')
# select.select_by_value('ITR-1')
# download_link.click()
# driver.implicitly_wait(2)

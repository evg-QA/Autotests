#Smoke test - authorization + add goods to cart + verifications
import time
from selenium import webdriver
from selenium.webdriver.common.by import By #import of the Selenium library and its module-Webdriver
driver = webdriver.Chrome(executable_path='C:\\Users\\evg\\Desktop\\PythonTest\\chromedriver.exe')

base_url = 'https://www.*******.com/' #save url in variable
driver.get(base_url)  #put the value in method-driver.get
driver.maximize_window()

"""fields validation """
login_standard_user = "standard_user"
password_all = "secret_1"

"""input login"""
user_name = driver.find_element(By.XPATH, "//input[@id='user-name']")
user_name.send_keys(login_standard_user)
print("input login")

"""input password"""
password = driver.find_element(By.XPATH, "//input[@id='password']")
password.send_keys(password_all)
print("input password")

"""click login button"""
button_login = driver.find_element(By.XPATH, "//input[@id='login-button']")
button_login.click()
print("click login button")

"""verification info about product 1 - name"""
item_backpack = driver.find_element(By.XPATH, "//a[@id='item_4_title_link']")
verification_item_backpack = item_backpack.text
print(verification_item_backpack)

"""verification info about product 1 - price"""
item_backpack_price = driver.find_element(By.XPATH, "//div[@class='inventory_item_price']")
verification_item_backpack_price = item_backpack_price.text
print(verification_item_backpack_price)

"""add item to cart"""
Add_item_backpack = driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']")
Add_item_backpack.click()
print("click Add to cart")
time.sleep(2)
"""checking add item to cart"""
# verification_Add_item_backpack = driver.find_element(By.XPATH, "//button[@id='remove-sauce-labs-backpack']")
# Add_item_backpack = verification_Add_item_backpack.text
# assert Add_item_backpack == "Remove"
# print("Test Pass")

"""Go to cart"""
cart_button = driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']")
cart_button.click()
print("click Go to cart")
time.sleep(2)

"""verification info cart product - name, price"""
cart_item_backpack = driver.find_element(By.XPATH, "//a[@id='item_4_title_link']")
cart_verification_item_backpack = cart_item_backpack.text
print(cart_verification_item_backpack)
"""Checking the name of the selected item in the product list and in the cart """
assert verification_item_backpack == cart_verification_item_backpack
print("Item comparison pass")

"""verification info about product - price"""
cart_item_backpack_price = driver.find_element(By.XPATH, "//div[@class='inventory_item_price']")
cart_verification_item_backpack_price = cart_item_backpack_price.text
print(cart_verification_item_backpack_price)
assert verification_item_backpack_price == cart_verification_item_backpack_price
print("Price comparison pass")

"""Click Checkout button"""
checkout_button = driver.find_element(By.XPATH, "//button[@id='checkout']")
checkout_button.click()
print("click Checkout button")
time.sleep(2)

"""Input user data"""
first_name_user = "FirstNAME"
last_name_user = "LastNAME"
zipCode_data_user = "1109112"

first_name = driver.find_element(By.XPATH, "//input[@id='first-name']")
first_name.send_keys(first_name_user)
print("input First name")

last_name = driver.find_element(By.XPATH, "//input[@id='last-name']")
last_name.send_keys(last_name_user)
print("input Last name")

zipCode_data = driver.find_element(By.XPATH, "//input[@id='postal-code']")
zipCode_data.send_keys(zipCode_data_user)
print("input Zip/Postal code")

"""Press continue button"""
continue_button = driver.find_element(By.XPATH, "//input[@id='continue']")
continue_button.click()
print("Press continue button")
time.sleep(3)

"""finish verification info product - name"""
finish_item_backpack = driver.find_element(By.XPATH, "//a[@id='item_4_title_link']")
finish_verification_item_backpack = finish_item_backpack.text
print(finish_verification_item_backpack)

"""Checking the name of the selected item in the product list and in the cart"""
assert verification_item_backpack == finish_verification_item_backpack
print("Finish item comparison pass")

"""finish verification info about product - price"""
finish_item_backpack_price = driver.find_element(By.XPATH, "//div[@class='inventory_item_price']")
finish_verification_item_backpack_price = finish_item_backpack_price.text
print(finish_verification_item_backpack_price)
assert verification_item_backpack_price == finish_verification_item_backpack_price
print("Finish price comparison pass")

"""Summary price - verification """
summary_price = driver.find_element(By.XPATH, "//div[@class='summary_subtotal_label']")
summary_price_verification = summary_price.text
print(summary_price_verification) #get text - Item total: $29.99

item_total = "Item total: " + finish_verification_item_backpack_price #contatination of lines+variable-finish amount before purchase
print(item_total)
assert summary_price_verification == item_total
print("Total summary price - PASS")
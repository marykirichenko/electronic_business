from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import time

driver = webdriver.Safari()

driver.maximize_window()

driver.get("https://localhost:8001")


def add_to_cart(link):
    driver.get(link)
    quantity= driver.find_element(By.ID,
                                   "quantity_wanted")
    addnumber = (random.choice([1, 2]))
    quantity.send_keys(addnumber)
    addtocart = driver.find_element(By.CSS_SELECTOR, "button[class = \"btn btn-primary add-to-cart\"]")
    time.sleep(1)
    driver.execute_script("arguments[0].click();", addtocart)
    time.sleep(4)
    continueshopping = driver.find_element(By.CSS_SELECTOR, "button[class = 'btn btn-secondary']")
    driver.execute_script("arguments[0].click();", continueshopping)
    time.sleep(4)


def add_products():
    skiwear_link = driver.find_element(By.XPATH, '//a[contains(text(), "Skiwear Collection")]')
    skiwear_link.click()
    time.sleep(3)

    skiwear_product_links = []

    product_title_links = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located(
            (By.XPATH, '//div[@class="product-description"]//h2[@class="h3 product-title"]//a'))
    )

    for link in product_title_links:
        skiwear_product_links.append(link.get_attribute('href'))

    random.shuffle(skiwear_product_links)

    for link in skiwear_product_links[:3]:
        add_to_cart(link)

    women_link = driver.find_element(By.CSS_SELECTOR, 'a[href*="https://localhost:8001/6-category-url"]')
    driver.execute_script("arguments[0].click();", women_link)
    time.sleep(4)

    total_products = driver.find_element(By.CLASS_NAME, "total-products")
    driver.execute_script("arguments[0].scrollIntoView();", total_products)

    women_product_links = []

    women_title_links = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located(
            (By.XPATH, '//div[@class="product-description"]//h2[@class="h3 product-title"]//a'))
    )

    for link in women_title_links:
        women_product_links.append(link.get_attribute('href'))

    random.shuffle(women_product_links)

    for link in women_product_links[:2]:
        add_to_cart(link)

    tocart = driver.find_element(By.CSS_SELECTOR, "i[class = \"material-icons shopping-cart\"")
    driver.execute_script("arguments[0].click();", tocart)

    men_link = driver.find_element(By.CSS_SELECTOR, 'a[href*="https://localhost:8001/6-category-url"]')
    driver.execute_script("arguments[0].click();", men_link)
    time.sleep(4)

    search_input = driver.find_element(By.NAME, "s")
    search_input.send_keys("Bag")
    search_input.submit()
    time.sleep(2)

    product_title_links = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located(
            (By.XPATH, '//div[@class="product-description"]//h2[@class="h3 product-title"]//a'))
    )

    search_product_links = []
    for link in product_title_links:
        search_product_links.append(link.get_attribute('href'))

    random.shuffle(search_product_links)

    print(search_product_links[0])
    add_to_cart(search_product_links[0])

    tocart = driver.find_element(By.CSS_SELECTOR, "i[class = \"material-icons shopping-cart\"")
    driver.execute_script("arguments[0].click();", tocart)

    for _ in range(1):

        products_in_cart = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "cart-item"))
        )
        time.sleep(1)
        canceledproduct = products_in_cart[1].find_element(By.CSS_SELECTOR, ".remove-from-cart")
        products_in_cart.remove(products_in_cart[1])
        driver.execute_script("arguments[0].click();", canceledproduct)
        time.sleep(2)

    time.sleep(5)
    driver.get("https://localhost:8001/zamówienie")

def register():
    driver.get("https://localhost:8001/logowanie?back=my-account")
    time.sleep(2)
    driver.get("https://localhost:8001/logowanie?create_account=1")
    time.sleep(2)
    gender = driver.find_element(By.CSS_SELECTOR, "input[type='radio'][value='1']")
    gender.click()
    firstname = driver.find_element(By.CSS_SELECTOR, "input[type='text'][id='field-firstname']")
    firstname.send_keys("gggg")
    lastname = driver.find_element(By.CSS_SELECTOR, "input[type='text'][id='field-lastname']")
    lastname.send_keys("rrrr")
    email = driver.find_element(By.CSS_SELECTOR, "input[type='email'][id='field-email']")
    email.send_keys("grr7uu799i@mail.com")
    password = driver.find_element(By.CSS_SELECTOR, "input[type='password'][id='field-password']")
    password.send_keys("qwerty123")
    dateOfBirth = driver.find_element(By.CSS_SELECTOR, "input[id='field-birthday'][name='birthday']")
    dateOfBirth.send_keys("2002-10-01")
    personaldatacheckbox = driver.find_element(By.CSS_SELECTOR, "input[name='customer_privacy'][type='checkbox']")
    driver.execute_script("arguments[0].scrollIntoView();", personaldatacheckbox)
    driver.execute_script("arguments[0].click();", personaldatacheckbox)
    time.sleep(2)
    acceptconditions = driver.find_element(By.CSS_SELECTOR, "input[name='psgdpr'][type='checkbox']")

    driver.execute_script("arguments[0].click();", acceptconditions)
    time.sleep(2)
    submit = driver.find_element(By.CLASS_NAME, "form-control-submit")
    driver.execute_script("arguments[0].click();", submit)
    time.sleep(2)

def adres():
    addr = driver.find_element(By.CSS_SELECTOR, "input[id='field-address1'][name='address1']")
    addr.send_keys("Alabama, 180.32.45.76")
    driver.execute_script("arguments[0].scrollIntoView();", addr)
    driver.execute_script("arguments[0].click();", addr)
    postal = driver.find_element(By.CSS_SELECTOR, "input[id='field-postcode'][name='postcode']")
    postal.send_keys("01-460")
    city = driver.find_element(By.CSS_SELECTOR, "input[id='field-city'][name='city']")
    city.send_keys("Warsawcon")
    submit = driver.find_element(By.CSS_SELECTOR, "button[type='submit'][name='confirm-addresses']")
    driver.execute_script("arguments[0].click();", submit)
    time.sleep(3)

def delivery():
    message = driver.find_element(By.ID, "delivery_message")

    driver.execute_script("arguments[0].scrollIntoView();", message)
    submit2 = driver.find_element(By.CSS_SELECTOR, "button[name='confirmDeliveryOption']")
    print(submit2)
    time.sleep(3)
    driver.execute_script("arguments[0].click();", submit2)
    time.sleep(6)
    payment = driver.find_element(By.ID, "payment-option-2")
    driver.execute_script("arguments[0].scrollIntoView();", payment)
    driver.execute_script("arguments[0].click();", payment)
    agreement = driver.find_element(By.CLASS_NAME, "js-terms")
    driver.execute_script("arguments[0].click();", agreement)
    time.sleep(2)
    confirmPayment = driver.find_element(By.CSS_SELECTOR, "div[id='payment-confirmation']")
    confirmPayment = confirmPayment.find_element(By.CSS_SELECTOR,
                                                 "button[type='submit'][class='btn btn-primary center-block']")
    driver.execute_script("arguments[0].click();", confirmPayment)
    time.sleep(5)
    driver.get("https://localhost:8001/moje-konto")
    time.sleep(3)
    driver.get("https://localhost:8001/historia-zamowien")
    time.sleep(3)
    order_link = driver.find_element(By.XPATH, '//a[contains(text(), "Szczegóły")]')
    driver.execute_script("arguments[0].click();", order_link)
    time.sleep(5)

register()
add_products()
adres()
delivery()

print("OK")

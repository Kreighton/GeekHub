'''Завдання: за допомогою браузера (Selenium) відкрити форму за наступним посиланням:
https://docs.google.com/forms/d/e/1FAIpQLScLhHgD5pMnwxl8JyRfXXsJekF8_pDG36XtSEwaGsFdU2egyw/viewform?usp=sf_link
заповнити і відправити її.
Зберегти два скріншоти: заповненої форми і повідомлення про відправлення форми.
В репозиторії скріншоти зберегти.
Корисні посилання:
https://www.selenium.dev/documentation/
https://chromedriver.chromium.org/downloads

'''


from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


chrome_profile_path = ''

options = ChromeOptions()
options.add_argument('--no-sandbox')


wd = Chrome(options=options, executable_path='./chromedriver.exe')
wait = WebDriverWait(wd, 10)
wd.get('https://docs.google.com/forms/d/e/1FAIpQLScLhHgD5pMnwxl8JyRfXXsJekF8_pDG36XtSEwaGsFdU2egyw/viewform?usp=sf_link')



input_field = wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, 'input[jsname="YPqjbf"]')))
input_field.click()
input_field.send_keys('Павел')
wd.save_screenshot('filled_form.png')

btn_to_click = wd.find_element(By.XPATH, "//span[@class='appsMaterialWizButtonPaperbuttonLabel quantumWizButtonPaperbuttonLabel exportLabel']")
btn_to_click.click()
wd.save_screenshot('btn_pressed.png')

from selenium import webdriver
import time
import math


link = "http://suninjuly.github.io/get_attribute.html"

driver = webdriver.Chrome(executable_path='C:\chromedriver\chromedriver.exe')
driver.get(link)

img = driver.find_element_by_id('treasure')

pic_attribute = img.get_attribute("valuex")
x = int(pic_attribute)

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

y = calc(x)

textarea = driver.find_element_by_id("answer")
textarea.send_keys(y)
time.sleep(3)

check_box = driver.find_element_by_id("robotCheckbox")
check_box.click()

radiobutton = driver.find_element_by_id("robotsRule")
radiobutton.click()

button = driver.find_element_by_css_selector("button.btn.btn-default")

button.click()

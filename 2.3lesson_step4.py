from selenium import webdriver
import time
import math


link = "http://suninjuly.github.io/alert_accept.html"

driver = webdriver.Chrome(executable_path='C:\chromedriver\chromedriver.exe')
driver.get(link)


button = driver.find_element_by_class_name("btn.btn-primary")

button.click()


confirm = driver.switch_to.alert
confirm.accept()

x_el = driver.find_element_by_id('input_value')

x = int(x_el.text)
#print(x)

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

y = calc(x)

textarea = driver.find_element_by_id("answer")
textarea.send_keys(y)
time.sleep(1)

button = driver.find_element_by_class_name("btn.btn-primary")

button.click()


https://github.com/Perehodko/stepik-auto-tests-course.git
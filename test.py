from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import NoSuchElementException




browser = webdriver.Firefox()#("C:\Users\acer_v3\Downloads\geckodriver.exe"')
m=1
browser.get('https://webrigada.amocrm.ru')
time.sleep(2)
loginAmo = browser.find_element(By.ID,'session_end_login').send_keys('login')

time.sleep(2)
passwordAmo = browser.find_element(By.ID,'password').send_keys('password')

time.sleep(2)
browser.find_element(By.ID, 'auth_submit').click()

time.sleep(2)
print('Авторизация прошла епта')

browser.get('https://webrigada.amocrm.ru/contacts/list/contacts/?skip_filter=Y')
print('список контактов получен')
time.sleep(2)

browser.find_element(By.CLASS_NAME, 'button-input-more-inner').click()
time.sleep(3)
print('нашел три точки')



browser.find_element(By.CLASS_NAME,'button-input__context-menu__item__inner')
time.sleep(3)
print('нажал поиск дублей') 


try:
    more_doubles = browser.find_element(By.ID, 'more_doubles')
    more_doubles.click()
    print("Поиск дублей MoreCRM")
    time.sleep(3)
except NoSuchElementException:
    span_more_doubles = browser.find_element(By.CLASS_NAME, 'button-input__context-menu__item__text')
    span_more_doubles.click()
    print('Поиск дублей по имени класса')
    time.sleep(3)


browser.find_element(By.ID, 'last_result').click()
print("Последний результат")
time.sleep(3)

browser.find_element(By.CLASS_NAME, 'pagination').find_element(By.LINK_TEXT, '1').click()
for i in range(20):
    browser.find_element(By.CLASS_NAME, 'container_values').find_element(By.CLASS_NAME, 'contacts').find_element(By.CLASS_NAME, 'button-input').click()
    
    cell_head_inner = browser.find_element(By.CLASS_NAME, 'cell-head__inner')
    browser.find_element(By.CLASS_NAME, 'control-checkbox  multiple-actions__top-checkbox  is-checked').click()
    print('выбрал все контакты-дубли')
    time.sleep(2)
    browser.find_element(By.CLASS_NAME, 'list-multiple-actions__item__icon icon icon-merge-action').click()
    print ('нажал на Объединить')
    time.sleep(2)
    browser.find_element(By.CLASS_NAME, 'button-input    modal-body__actions__save js-modal-accept js-button-with-loader js-merge-start').click()
    time.sleep(10)
    browser.find_element(By.CLASS_NAME, 'button-input    js-modal-accept js-button-with-loader modal-body__actions__save js-progress-cont-to-work').click()
    print('нажал продолжить работу')
    
    
    # print('нашел контакт')
    # time.sleep(2)
    
    
    
browser.find_element(By.ID, "last_result")
print ("последний результат")
time.sleep(2)

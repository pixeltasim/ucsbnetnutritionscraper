from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

url = 'https://netnutrition.housing.ucsb.edu/NetNutrition/1#'
browser.get(url)
dlg = browser.find_element_by_css_selector('a[onclick="javascript:unitsSelectUnit(7);"]')
dlg.click()
menuitem = browser.find_element_by_link_text("De La Guerra's Daily Menu")
menuitem.click()
dinner = browser.find_element_by_link_text("Dinner")
dinner.click()
barleysoup = browser.find_element_by_css_selector('td[onmouseover*="(23703354)"]')
barleysoup.move_to_element()
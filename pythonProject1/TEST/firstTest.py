from selenium import webdriver
import time

from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.get("https://www.mappy.com")

driver.find_element(By.XPATH, "//button[@id='didomi-notice-agree-button']/span[.='Accepter & Fermer']").click()
driver.find_element(By.CSS_SELECTOR, ".TAKMb > span > svg > path").click()
time.sleep(5)
driver.find_element(By.XPATH, "//a[@class='ll3c4 IJzr8 BPLAW']").click()
time.sleep(2)
driver.find_element(By.XPATH, "/html//input[@id='username']").send_keys("agbopa@hotmail.com")
driver.find_element(By.XPATH, "/html//input[@id='password']").send_keys("Testeur1")
driver.find_element(By.CSS_SELECTOR, "input#kc-login").click()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, ".TAKMb > span > svg > path").click()
time.sleep(2)
nom = driver.find_element(By.XPATH, "//div[@class='PPXlE']").text
assert nom == "Paul agbo"
print("Vous êtes connecté au de : "+ nom)
time.sleep(3)
driver.find_element(By.XPATH, "/html//div[@id='app']/div[@class='SearchHomePage withToaster']/div[2]//div[@class='Lp1YC']").click()

driver.find_element(By.XPATH, "//div[contains(text(),'Mes lieux favoris')]").click()
"""
driver.find_element(By.ID, "SearchInputundefined").send_keys("Lens")
"""
print("Coucou, ça en est où ?")
print ("git essais")
driver.close()
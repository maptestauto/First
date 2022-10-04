from selenium import webdriver
import time

from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.get("https://login.yahoo.com/?.intl=fr&.lang=fr-FR&src=ym&activity=ybar-mail&pspid=2023392333&done=https%3A%2F%2Fmail.yahoo.com%2Fd%2F%3F.intl%3Dfr%26.lang%3Dfr-FR%26pspid%3D2023392333%26activity%3Dybar-mail&add=1")


driver.find_element(By.XPATH, "//input[@id='login-username']").send_keys("maptestauto@yahoo.com")
driver.find_element(By.XPATH, "//input[@id='login-signin']").click()
time.sleep(3)
driver.find_element(By.XPATH, "//input[@id='login-passwd']").send_keys("Testeur1")
driver.find_element(By.XPATH, "//*[@id='login-signin']").click()
time.sleep(5)
driver.find_element(By.XPATH, "//span[contains(text(),'Alors... On a oublié son mot de passe Mappy ?')]").click()

driver.find_element(By.XPATH, "//a[contains(text(),'ce lien')]").click()

driver.switch_to.window(driver.window_handles[1])
driver.find_element(By.XPATH, "//input[@id='password-new']").send_keys("Testeur1")
driver.find_element(By.XPATH, "//input[@id='password-confirm']").send_keys("Testeur1")
driver.find_element(By.XPATH, "//div[@id='kc-form-buttons']/input[@value='Valider']").click()
"""
time.sleep(5)
driver.find_element(By.LINK_TEXT, "CONNEXION / INSCRIPTION").click()
time.sleep(2)
"""

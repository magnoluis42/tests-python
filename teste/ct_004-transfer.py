from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

servico = Service(ChromeDriverManager().install())

navegador = webdriver.Chrome(service=servico)
navegador.get("https://demo.testfire.net/login.jsp")
navegador.find_element('xpath', '//*[@id="uid"]').send_keys("jsmith")
navegador.find_element('xpath', '//*[@id="passw"]').send_keys("demo1234")
navegador.find_element('xpath', '//*[@id="login"]/table/tbody/tr[3]/td[2]/input').click()
navegador.find_element('xpath', '//*[@id="MenuHyperLink3"]').click()
navegador.find_element('xpath', '//*[@id="fromAccount"]/option[1]').click()
time.sleep(2)
navegador.find_element('xpath', '//*[@id="toAccount"]/option[2]').click()
time.sleep(2)
navegador.find_element('xpath','//*[@id="transferAmount"]').send_keys(-100)
time.sleep(2)
navegador.find_element('xpath', '//*[@id="transfer"]').click()
time.sleep(2)


input("Pressione Enter para fechar o navegador...")
navegador.quit()

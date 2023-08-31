from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

servico = Service(ChromeDriverManager().install())

navegador = webdriver.Chrome(service=servico)
navegador.get("https://demo.testfire.net/login.jsp")
navegador.find_element('xpath', '//*[@id="uid"]').send_keys("admin")
navegador.find_element('xpath', '//*[@id="passw"]').send_keys("admin")
navegador.find_element('xpath', '//*[@id="login"]/table/tbody/tr[3]/td[2]/input').click()

navegador.find_element('xpath', '//*[@id="_ctl0__ctl0_Content_Administration"]/ul/li/a').click()

navegador.find_element('xpath', '/html/body/table[2]/tbody/tr/td[2]/div/table/tbody/tr[9]/td[1]/input[1]').send_keys("magno")
navegador.find_element('xpath', '/html/body/table[2]/tbody/tr/td[2]/div/table/tbody/tr[9]/td[1]/input[2]').send_keys("luis")
navegador.find_element('xpath', '/html/body/table[2]/tbody/tr/td[2]/div/table/tbody/tr[9]/td[2]/input').send_keys("magnoluis")
navegador.find_element('xpath', '/html/body/table[2]/tbody/tr/td[2]/div/table/tbody/tr[9]/td[3]/input[1]').send_keys("senha1")
navegador.find_element('xpath', '/html/body/table[2]/tbody/tr/td[2]/div/table/tbody/tr[9]/td[3]/input[2]').send_keys("senha2")
navegador.find_element('xpath', '/html/body/table[2]/tbody/tr/td[2]/div/table/tbody/tr[9]/td[4]/input').click()

input("Pressione Enter para fechar o navegador...")
navegador.quit()

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://demo.anhtester.com/basic-first-form-demo.html')
driver.implicitly_wait(10)
try: 
    print('Fechando o addsense')
    addsense = driver.find_element(By.XPATH, '//*[@id="at-cv-lightbox-close"]')
    addsense.click()
except:
    print('Erro ao fechar o Addsense')

campo_mensagem = driver.find_element(By.XPATH, '//*[@id="user-message"]')
campo_mensagem.send_keys('Não acredito que isso está acontecendo!')
botao_exibir_mensagem = driver.find_element(By.XPATH, '//*[@id="get-input"]/button')
sleep(2)
botao_exibir_mensagem.click()

sleep(3)
driver.quit()



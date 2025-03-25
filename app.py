from selenium import webdriver
from selenium.webdriver.common.by import By

#configurando as opcoes do driver
options = webdriver.ChromeOptions()
options.add_argument('--ignore-ssl-errors')
options.add_argument('--ignore-certificate-errors')
options.add_argument('--headless')
options.add_argument('--disable-gpu')

# criando e conectando o driver
driver = webdriver.Chrome(options=options)
driver.get("https://economia.uol.com.br/cotacoes/cambio/")

# comecando o script
box = driver.find_element(by=By.CLASS_NAME, value="chart-content")
print(box)


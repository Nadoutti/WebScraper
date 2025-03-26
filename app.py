from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

def cotacao_moeda(moeda_escolhida):
    #configurando as opcoes do driver
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-ssl-errors')
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')


    # criando e conectando o driver
    driver = webdriver.Chrome(options=options)
    url = "https://economia.uol.com.br/cotacoes/cambio/"
    url_final: str


    if moeda_escolhida.lower() == 'euro':
        url_final = url + 'euro-uniao-europeia/'

    elif moeda_escolhida.lower() == 'libra':
        url_final = url + 'libra-esterlina-reino-unido/'
    elif moeda_escolhida.lower() == 'dolar':
        url_final = url
        

    driver.get(url_final)

    # comecando o script
    valor_de_compra = WebDriverWait(driver, 10).until(
        ec.presence_of_element_located((By.XPATH, "/html/body/div[3]/article/div[2]/div/div[1]/div/div/div[1]/div[3]/div/div/div/div[2]/div[1]/div[1]/div/span[2]"))
    )

    return valor_de_compra.text

print("Cotacao de moedas em tempo real!")
print("Qual moeda voce gostaria de saber o preco hoje?")
print("Opcoes: euro, libra, dolar")
moeda_escolhida =  input("Moeda para cotar: ")
print(cotacao_moeda(moeda_escolhida))
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from db_conn import connect_db



def cotacao_moeda(moeda_escolhida):
    #configurando as opcoes do driver
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-ssl-errors')
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')

    connection = connect_db()
    cursor = connection.cursor()


    # criando e conectando o driver
    driver = webdriver.Chrome(options=options)
    url = "https://economia.uol.com.br/cotacoes/cambio/"
    url_final = ""
    moeda_id = 1

    if moeda_escolhida.lower() == 'euro':
        url_final = url + 'euro-uniao-europeia/'
        moeda_id = 2

    elif moeda_escolhida.lower() == 'libra':
        url_final = url + 'libra-esterlina-reino-unido/'
        moeda_id = 3
        
    elif moeda_escolhida.lower() == 'dolar':
        url_final = url
        

    driver.get(url_final)

    # comecando o script
    valor_de_compra = WebDriverWait(driver, 10).until(
        ec.presence_of_element_located((By.XPATH, "/html/body/div[3]/article/div[2]/div/div[1]/div/div/div[1]/div[3]/div/div/div/div[2]/div[1]/div[1]/div/span[2]"))
    )
    
    dia_cotacao = driver.find_element(By.XPATH, "/html/body/div[3]/article/div[2]/div/div[1]/div/div/div[1]/div[3]/div/div/div/div[2]/div[2]/span")


    
    dia_cotacao_split = dia_cotacao.text.split()
    dia_cotacao_filtrado = dia_cotacao_split[2]
    print(dia_cotacao_filtrado)

    
    # adicionar ao banco de dados
    cursor.execute('''
        INSERT INTO dados (MOEDA_ID, VALOR_COTACAO, DIA_COTACAO, NOME_MOEDA) VALUES (?, ?, ?, ?)
    ''', (moeda_id, int(valor_de_compra.text), dia_cotacao_filtrado, moeda_escolhida))

    if cursor.rowcount > 0:
        print("Dados adicionados com sucesso")


    return valor_de_compra.text

print("Cotacao de moedas em tempo real!")
print("Qual moeda voce gostaria de saber o preco hoje?")
print("Opcoes: euro, libra, dolar")
moeda_escolhida =  input("Moeda para cotar: ")

print(cotacao_moeda(moeda_escolhida))


print("Gostaria de ver um grafico nos ultimos 30 dias?")


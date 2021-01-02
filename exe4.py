from selenium.webdriver import Firefox
from urllib.parse import urlparse
from time import sleep

# Objetivo dar match com assert entre a url enviada e o retorno do resultado

url = 'https://selenium.dunossauro.live/exercicio_04.html'

firefox = Firefox()

firefox.get(url)

def data_filler(browser, nome, email, senha, telefone):
    browser.find_element_by_name('nome').send_keys(nome)
    browser.find_element_by_name('email').send_keys(email)
    browser.find_element_by_name('senha').send_keys(senha)
    browser.find_element_by_name('telefone').send_keys(telefone)
    browser.find_element_by_name('btn').click()

dados = {
    'nome': 'Eduardo',
    'email': 'edu@du.edu',
    'senha': 'q1w2e3r4',
    'telefone': '987654321'
}

sleep(2)

data_filler(firefox, **dados)

url_parsed = urlparse(firefox.current_url)

sleep(2)

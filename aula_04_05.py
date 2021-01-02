from selenium.webdriver import Firefox
from time import sleep
from pprint import pprint

"""
1. Pegar todos os links de aulas
    {'nome da aula': 'link da aula'}
2. Navegar até o exercício 3
    achar a url do exercício 3 e ir até lá
"""

browser = Firefox()
browser.get('http://selenium.dunossauro.live/aula_04.html')

def get_links(browser, elemento): # dicionário
    """
    Pega todos os links dentro de um elemento

    - browser = a instância do navegador
    - element = webelement [aside, main, body, ul, ol]
    """
    result = {}
    element = browser.find_element_by_tag_name(elemento)
    anchors = element.find_elements_by_tag_name('a')

    for anchor in anchors:
        result[anchor.text] = anchor.get_attribute('href')
    
    return result


"""
Parte 1
"""
sleep(2)

aulas = get_links(browser, 'aside') 
pprint(aulas)

"""
Podemos chamar as páginas com: python3 -i xxxx.py
    - browser.get(resultado_1['Aula 3'])
    - browser.get(resultado_1['Aula 4'])
"""

"""
Parte 2
"""

exercicios = get_links(browser, 'main')
pprint(exercicios)

browser.get(exercicios['Exercício 3'])
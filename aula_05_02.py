from selenium.webdriver import Firefox

url = 'http://selenium.dunossauro.live/aula_05_b.html'

firefox = Firefox()

firefox.get(url)

topico = firefox.find_element_by_class_name('topico')
linguagens = firefox.find_element_by_class_name('linguagens')

for linguagem in linguagens:
    print(
        (linguagem.find_element_by_tag_name('h2').text,
        linguagem.find_element_by_tag_name('p').text)
    )

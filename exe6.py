from selenium.webdriver import Firefox
from time import sleep
from selenium.common.exceptions import NoSuchElementException

url = 'http://selenium.dunossauro.live/exercicio_06.html'

b = Firefox()

b.get(url)
sleep(1)

def fill_form(browser, form, name, password):
    browser.find_element_by_css_selector(f'.form-{form} input[name="nome"]').send_keys(name)
    browser.find_element_by_css_selector(f'.form-{form} input[name="senha"]').send_keys(password)
    browser.find_element_by_css_selector(f'.form-{form} input[name="{form}"]').click()

def to_be_filled():
        return b.find_elements_by_css_selector('div.grid-container span')[0].text

while 'Mentira' not in to_be_filled():
    fill_form(b, to_be_filled(), 'Fulano', 'senha1234')
    sleep(1)
    
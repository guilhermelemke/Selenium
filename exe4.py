from selenium.webdriver import Firefox
from urllib.parse import urlparse, parse_qsl, urlsplit
from time import sleep
from json import loads

url = 'https://selenium.dunossauro.live/exercicio_04.html'

firefox = Firefox()

firefox.get(url)

def fill_form(browser, name, email, password, phone):
    browser.find_element_by_name('nome').send_keys(name)
    browser.find_element_by_name('email').send_keys(email)
    browser.find_element_by_name('senha').send_keys(name)
    browser.find_element_by_name('telefone').send_keys(name)
    browser.find_element_by_name('btn').click()

sleep(2)

values = {
    'name': 'Eduardo',
    'email': 'dudu@du.edu',
    'password': 'q1w2e3r4',
    'phone': '987654321'
}

fill_form(firefox, **values)

sleep(2)

parsed_url = urlparse(firefox.current_url)
dict_test = dict(parse_qsl(urlsplit(firefox.current_url).query))
print(dict_test)

result_dict = firefox.find_element_by_tag_name('textarea').text
print(result_dict)
#assert result_dict == values

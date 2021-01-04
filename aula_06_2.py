from selenium.webdriver import Firefox

url = 'http://selenium.dunossauro.live/aula_06_a.html'

b = Firefox()

b.get(url)

""" Using Type Tag
nome = b.find_element_by_css_selector('[type="text"]')
password = b.find_element_by_css_selector('[type="password"]')
btn = b.find_element_by_css_selector('[type="submit"]')
"""

# Using Name Tag
nome = b.find_element_by_css_selector('[name="nome"]')
password = b.find_element_by_css_selector('[name="senha"]')
btn = b.find_element_by_css_selector('[name="l0c0"]')

nome.send_keys('Eduardo')
password.send_keys('senha123')
btn.click()

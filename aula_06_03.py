from selenium.webdriver import Firefox

url = 'http://selenium.dunossauro.live/aula_06_a.html'

b = Firefox()

b.get(url)

b.find_elements_by_css_selector('div.form-group')

b.find_elements_by_css_selector('div.form-group + br')[0].get_atribute('id')

# Take id #inside-name from tag div
b.find_element_by_css_selector('div.form-group > #inside-name')

# All labels inside form
b.find_element_by_css_selector('form label')

from selenium.webdriver import Firefox

url = 'http://curso-python-selenium.netlify.app/exercicio_01.html'

browser = Firefox()
browser.get(url)
browser.implicitly_wait(3)

initial_dictionary = {}

atribute_list = browser.find_elements_by_tag_name('p')

for item in atribute_list:
    initial_dictionary[item.get_attribute('atributo')] = item.text

final_dictionary = {}
final_dictionary['h1'] = initial_dictionary

print(final_dictionary)

browser.quit()

from selenium.webdriver import Firefox

url = 'https://curso-python-selenium.netlify.app/exercicio_02.html'

browser = Firefox()
browser.get(url)
browser.implicitly_wait(3)

button = browser.find_element_by_tag_name('a')

win = False

while(not win):
    p_value = browser.find_elements_by_tag_name('p')
    if 'Você ganhou' in p_value[-1].text:
        win = True
        break
    button.click()
    
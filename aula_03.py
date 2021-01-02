from selenium.webdriver import Firefox

url = 'https://curso-python-selenium.netlify.app/aula_03.html'

browser = Firefox()
browser.get(url)
browser.implicitly_wait(5)

a = browser.find_element_by_tag_name('a')
p = browser.find_element_by_tag_name('p')


#browser.quit()
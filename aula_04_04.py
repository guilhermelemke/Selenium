from selenium.webdriver import Firefox
from urllib.parse import urlparse

browser = Firefox()
browser.get('http://selenium.dunossauro.live/aula_04_a.html')

parsed_url = urlparse(browser.current_url)

print(parsed_url)
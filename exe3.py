from selenium.webdriver import Firefox
from time import sleep
from urllib.parse import urlparse

url = 'https://selenium.dunossauro.live/exercicio_03.html'
browser = Firefox()
browser.get(url)

def get_links_text(browser, element, second_element):
    result = {}
    element = browser.find_element_by_tag_name(element)
    anchors = element.find_elements_by_tag_name(second_element)

    for anchor in anchors:
        result[anchor.text] = anchor.get_attribute('href')

    return result


def get_links_attr(browser, element, second_element):
    result = {}
    element = browser.find_element_by_tag_name(element)
    anchors = element.find_elements_by_tag_name(second_element)

    for anchor in anchors:
        result[anchor.get_attribute('attr')] = anchor.get_attribute('href')

    return result


sleep(2)
# First link
first_link = get_links_text(browser, 'main', 'a')
browser.get(first_link['Começar por aqui'])

sleep(2)
# Second link
second_link = get_links_attr(browser, 'main', 'a')
browser.get(second_link['errado'])

sleep(30)
# Third Link
third_link = get_links_text(browser, 'main', 'a')
browser.get(third_link[browser.title])

sleep(2)
# Fourth Link
fourth_link = get_links_text(browser, 'main', 'a')
browser.get(fourth_link[urlparse(browser.current_url).path[1:]])
browser.refresh()

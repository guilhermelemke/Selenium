from selenium.webdriver import Firefox
from selenium.webdriver.support.events import AbstractEventListener, EventFiringWebDriver

class Listener(AbstractEventListener):
    def after_navigate_to(self, url, webdriver):
        print(f'Going to {url}')

    def before_navigate_back(self, url, webdriver):
        print('going back to last visited page')    

    def before_click(self, element, webdriver):
        if element.tag_name == 'input':
            print(webdriver.find_element_by_tag_name('span').text)
        print(f'before click on element {element.tag_name}')

    def after_click(self, element, webdriver):
        if element.tag_name == 'input':
            print(webdriver.find_element_by_tag_name('span').text)
        print(f'after click on element {element.tag_name}')

browser = Firefox()

fire_browser = EventFiringWebDriver(browser, Listener())

fire_browser.get('https://selenium.dunossauro.live/aula_07_d')

text_input = fire_browser.find_element_by_tag_name('input')
span = fire_browser.find_element_by_tag_name('span')
p = fire_browser.find_element_by_tag_name('p')

text_input.click()
span.click()

fire_browser.get('https://selenium.dunossauro.live/aula_07_c')
fire_browser.back()
browser.quit()

"""
1 - Check if the change occurs in span (focus, blus)
2 - Check if the change occurs in p (change)
"""

from selenium.webdriver import Firefox

browser = Firefox()

browser.get('https://selenium.dunossauro.live/aula_07_d')

text_input = browser.find_element_by_tag_name('input')
span = browser.find_element_by_tag_name('span')
p = browser.find_element_by_tag_name('p')

"""
When input is clicked
Then the text `está com foco` should be the content of `span`
When span is clicked
Then the text `está sem foco` should be the content of `span`
"""

text_input.click()
assert 'está com foco' == span.text, 'Failed - span out of focus'
span.click()
assert 'está sem foco' == span.text, 'Failed - span in focus'

"""
Given that `p` content is `1`
When `text` is sent in element `input`
Then the text `está com foco` should be the content of `span`
When span is clicked
Then the text `está sem foco` should be the content of `span`
Then the text `1` should be the content of `p`
"""

assert p.text == '0', 'p is not 0'
text_input.send_keys('text')
assert 'está com foco' == span.text, 'está com foco não está em foco'
span.click()
assert 'está sem foco' == span.text, 'está sem foco não está em foco'
assert p.text == '1', 'p não é um'


browser.quit()

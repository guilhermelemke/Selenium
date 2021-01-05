from selenium.webdriver import Firefox

url = 'http://selenium.dunossauro.live/aula_06_a.html'

b = Firefox()

b.get(url)

""" Using Type Attribute [attr=value] - exact value
nome = b.find_element_by_css_selector('[type="text"]')
password = b.find_element_by_css_selector('[type="password"]')
btn = b.find_element_by_css_selector('[type="submit"]')
"""

"""# Using Name Attribute [attr=value] - exact value
nome = b.find_element_by_css_selector('[name="nome"]')
password = b.find_element_by_css_selector('[name="senha"]')
btn = b.find_element_by_css_selector('[name="l0c0"]')
"""

"""
# using attribute [attr*=value] - includes the value
nome = b.find_element_by_css_selector('[name*="ome"]')
password = b.find_element_by_css_selector('[name*="nha"]')
btn = b.find_element_by_css_selector('[name*="l0"]')
"""

"""
# using attribute [attr|="value"] - start with or equal to value
nome = b.find_element_by_css_selector('[name|="nome"]')
password = b.find_element_by_css_selector('[name|="senha"]')
btn = b.find_element_by_css_selector('[name|="l0c0"]')
"""

# using attribute [attrˆ="value"] - starts with
nome = b.find_element_by_css_selector('[nameˆ="n"]')
password = b.find_element_by_css_selector('[nameˆ="s"]')
btn = b.find_element_by_css_selector('[nameˆ="l"]')

nome.send_keys('Eduardo')
password.send_keys('senha123')
btn.click()

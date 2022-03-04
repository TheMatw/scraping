from selenium import webdriver
browser = webdriver.Chrome()
browser.maximize_window()

url = "https://flight.naver.com/"
browser.get(url)

# browser.find_element_by("가는 날").click()
#
# browser.find_element_by_link_text("27")[0].click()
# browser.find_element_by_link_text("28")[0].click()

browser.find_element_by_xpath("//*[@id='__next']/div/div[1]/div[9]/div/ul/li[1]/a").click()
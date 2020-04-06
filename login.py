from selenium import webdriver

driver = webdriver.Chrome()

driver.get("http://127.0.0.1:8000/accounts/login/")
driver.find_element_by_name("username").send_keys("aboli2")
driver.find_element_by_name("password").send_keys("1234wxyz")
driver.find_element_by_xpath("//input[@type = 'submit']").click()
print(driver.current_url)
#if anything is displayed then we go on to that element by any attribute and (.text) it and print 
# that text so that we know the signup is working correctly 

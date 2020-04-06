from selenium import webdriver

driver = webdriver.Chrome()

driver.get("http://127.0.0.1:8000/accounts/signup/")
driver.find_element_by_name("username").send_keys("aboli3")
driver.find_element_by_name("password1").send_keys("1234wxyz")
driver.find_element_by_name("password2").send_keys("1234wxyz")
driver.find_element_by_xpath("//input[@type = 'submit']").click()
print(driver.current_url)
message = driver.current_url
assert "article" in message # for complete check we can have == sign instead of 'in'
#if anything is displayed then we go on to that element by any attribute and (.text) it and print 
# that text so that we know the signup is working correctly 
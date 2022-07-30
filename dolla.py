from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

like_url = 'https://www.like4like.org/login'
like_username = "testingsecondacc"
like_password = "123123.Tt"

twitter_username = "riseld02"
twitter_password = "123123.T"

options = webdriver.FirefoxOptions()
options.add_argument("--headless")

driver = webdriver.Firefox(options = options)
driver.implicitly_wait(50)

driver.fullscreen_window()
driver.get(like_url)

username = driver.find_element(By.ID, "username")
password = driver.find_element(By.ID, "password")

username.clear()
password.clear()

username.send_keys(like_username)
password.send_keys(like_password)
password.send_keys(Keys.RETURN)

driver.find_element(By.CSS_SELECTOR, 'a[title="Earn Credits"]').click()
driver.find_element(By.CSS_SELECTOR, 'a[title="Earn Credits By Twitter Follows"]').click()

print("like4like login sucessful")

interactions = 0

while True:

	if interactions == 25:
		time.sleep(7500)
		interactions = 0
		driver.refresh()
		continue

	print("clicking on earn credits button")
	driver.find_element(By.CSS_SELECTOR, '.earn_pages_button').click()

	time.sleep(5)

	try:
		driver.switch_to.window(driver.window_handles[1])
	except:
		print("something went wrong. new window wasn't opened")
		driver.refresh()
		continue

	try:
		twit_user_inp = driver.find_element(By.NAME, "session[username_or_email]")
		twit_pass_inp = driver.find_element(By.NAME, "session[password]")
		twit_user_inp.clear()
		twit_pass_inp.clear()

		twit_user_inp.send_keys(twitter_username)
		twit_pass_inp.send_keys(twitter_password)
		twit_pass_inp.send_keys(Keys.RETURN)
	except:
		# already logged in
		pass

	time.sleep(5)
	actions = ActionChains(driver)
	actions.send_keys(Keys.RETURN)
	actions.perform()
	time.sleep(5)
	print("person followed")

	driver.close()
	driver.switch_to.window(driver.window_handles[0])

	driver.find_element(By.CSS_SELECTOR, 'img[title="Click On The Button To Confirm Interaction!"]').click()
	print("follow confirmed")
	print("credits added")
	interactions = interactions + 1

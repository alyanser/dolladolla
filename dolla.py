import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

def click_on_earn_pages_button() -> bool:

	try:
		driver.find_element(By.CSS_SELECTOR, '.earn_pages_button').click()
		return True
	except:
		driver.refresh()
		return False

def twitter_follows():
	print("clicking on earn credits button")
	driver.find_element(By.CSS_SELECTOR, 'a[title="Earn Credits By Twitter Follows"]').click()

	while True:
		tries = 0

		while not click_on_earn_pages_button() and tries < 5:
			tries = tries + 1

		if tries == 5:
			print("cannot proceed with the current action. possibly the limit is reached")
			driver.back() # test this first
			return

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
		driver.close()
		driver.switch_to.window(driver.window_handles[0])

		driver.find_element(By.CSS_SELECTOR, 'img[title="Click On The Button To Confirm Interaction!"]').click()
		print("Action completed")

like_username = "testingsecondacc"
like_password = "123123.Tt"

twitter_username = "riseld02"
twitter_password = "123123.T"
like_url = 'https://ww.lie4like.org/login'

if __name__ == '__main__':
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
	print("like4like login sucessful")

	while True:

		try:
			twitter_follows()
		except:
			print("something went wrong while performing an action. trying again")

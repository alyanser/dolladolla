import time
from os.path import exists
from os import mkdir
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

def click_on_earn_pages_button():

	for _ in range(3):

		try:
			driver.find_element(By.CSS_SELECTOR, '.earn_pages_button').click()
			time.sleep(3)
			driver.switch_to.window(driver.window_handles[1])
			return True
		except:
			driver.refresh()

	driver.back()
	return False

def click_on_confirm_button():

	for _ in range(5):

		try:
			driver.find_element(By.CSS_SELECTOR, 'img[title="Click On The Button To Confirm Interaction!"]').click()
			print("Action completed")
			return
		except:
			pass

	print("could not click on confirm button")

def twitter_follows():
	print("twitter follows in process...")
	actions.send_keys(Keys.UP * 8)
	actions.perform()
	time.sleep(2)
	driver.find_element(By.CSS_SELECTOR, 'a[title="Earn Credits By Twitter Follows"]').click()

	while True:

		if not click_on_earn_pages_button():
			return

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

		time.sleep(3)
		actions.send_keys(Keys.RETURN)
		actions.perform()
		time.sleep(3)
		driver.close()
		driver.switch_to.window(driver.window_handles[0])

		click_on_confirm_button()

def insta_follows():
	print("instagram follows in process...")
	actions.send_keys(Keys.DOWN * 8)
	actions.perform()
	time.sleep(2)
	driver.find_element(By.CSS_SELECTOR, 'a[title="Earn Credits By Instagram Follows"]').click()

	while True:

		if not click_on_earn_pages_button():
			return

		time.sleep(4)

		# it's buggy. use CSS_SELECTOR
		actions.send_keys(Keys.TAB * 3)
		actions.send_keys(Keys.RETURN)
		actions.perform()

		time.sleep(4)
		driver.close()
		driver.switch_to.window(driver.window_handles[0])
		click_on_confirm_button()

profile_dir = "firefox-profile"

like_username = "testingsecondacc"
like_password = "123123.Tt"

like_url = 'https://www.like4like.org/login'
twitter_username = "riseld02"
twitter_password = "123123.T"
insta_username = "reallysomeone_"
insta_password = "reallysomeone123"

if __name__ == '__main__':
	print("dolla dolla bill y'all")
	print("starting the bot...")

	if not exists(profile_dir):
		mkdir(profile_dir)

	options = webdriver.FirefoxOptions()

	options.add_argument("--headless")
	options.add_argument("--profile") 
	options.add_argument(profile_dir) 

	driver = webdriver.Firefox(options = options)

	driver.implicitly_wait(30)
	actions = ActionChains(driver)

	driver.get(like_url)

	try:
		username = driver.find_element(By.ID, "username")
		password = driver.find_element(By.ID, "password")

		username.clear()
		password.clear()

		username.send_keys(like_username)
		password.send_keys(like_password)
		password.send_keys(Keys.RETURN)
	except:
		pass

	try:
		driver.find_element(By.CSS_SELECTOR, 'a[title="Earn Credits"]').click()
		print("login successful")
	except:
		print("could not login. exiting...")
		exit(1)

	while True:

		try:
			twitter_follows()
			insta_follows()
		except KeyboardInterrupt:
			exit(1)
		except:
			driver.quit()
			raise

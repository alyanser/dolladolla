import time
from os.path import exists
from os import mkdir
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

def click_on_earn_pages_button():

	for _ in range(2):

		try:
			driver.find_element(By.CSS_SELECTOR, '.earn_pages_button').click()
			time.sleep(1)
			driver.switch_to.window(driver.window_handles[1])
			return True
		except:
			driver.refresh()

	driver.back()
	return False

def click_on_confirm_button():

	for _ in range(2):

		try:
			driver.find_element(By.CSS_SELECTOR, 'img[title="Click On The Button To Confirm Interaction!"]').click()
			print("action confirmed successfully")
			return True
		except:
			pass

	print("could not click on confirm button")
	driver.refresh()
	return False

def scroll_into_view(element):
	dest = element.location_once_scrolled_into_view

	if dest == None:
		raise Exception("dict is null somehow")

	driver.execute_script("window.scrollBy({X}, {Y})".format(X = dest["x"], Y = dest["y"]))
	time.sleep(1)

def twitter_login(username, password):
	print("logging into twitter")
	driver.get("https://www.twitter.com/login")

	try:
		_ = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a/div/span/div/div/span/span")
		print("already logged into twitter")
		return
	except:
		pass

	time.sleep(3)
	actions.send_keys(Keys.TAB * 3)
	actions.send_keys(username)
	actions.send_keys(Keys.RETURN)
	actions.perform()
	time.sleep(2)
	actions.send_keys(password)
	actions.send_keys(Keys.RETURN)
	actions.perform()
	_ = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a/div/span/div/div/span/span")
	print("logged into twitter")

def like4like_login(username, password):
	print("logging into like4like")
	driver.get("https://www.like4like.org/login")
	username_inp = driver.find_element(By.XPATH, '//*[@id="username"]')
	password_inp = driver.find_element(By.XPATH, '//*[@id="password"]')

	username_inp.clear()
	password_inp.clear()

	username_inp.send_keys(username)
	password_inp.send_keys(password)
	password_inp.send_keys(Keys.RETURN)
	time.sleep(3)
	print("logged into like4like")
	return

	try:
		captcha = driver.find_element(By.XPATH, '')
		print("captcha detected. solve it to continue (continuing in 30 seconds)")
		captcha.click()
		time.sleep(30)
	except:
		return

def twitter_follows():
	print("twitter follows in process...")

	twit_access_button = driver.find_element(By.XPATH, '/html/body/div[6]/div/div[1]/div/div/div[3]/a[1]')
	twit_access_button.click()

	while True:

		if not click_on_earn_pages_button():
			return

		time.sleep(2)
		actions.send_keys(Keys.RETURN) # emulate pressing follow button
		actions.perform()
		time.sleep(3)
		driver.close()
		driver.switch_to.window(driver.window_handles[0])
		click_on_confirm_button()

def twitter_retweets():
	print("twitter retweets in process...")

	twit_access_button = driver.find_element(By.XPATH, '/html/body/div[6]/div/div[1]/div/div/div[3]/a[2]')

	twit_access_button.click()

	while True:

		if not click_on_earn_pages_button():
			return

		try:
			retweet_button = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/section/div/div/div/div/div/div[1]/article/div/div/div/div[3]/div[7]/div/div[2]/div/div/div')
		except:
			retweet_button = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/section/div/div/div/div/div/div[1]/article/div/div/div/div[3]/div[8]/div/div[2]/div/div/div')

		scroll_into_view(retweet_button)
		actions.send_keys(Keys.UP * 3) # hacky but what can you do
		actions.perform()
		time.sleep(1)
		retweet_button.click()
		actions.send_keys(Keys.RETURN)
		actions.perform()
		time.sleep(3)
		driver.close()
		driver.switch_to.window(driver.window_handles[0])
		click_on_confirm_button()

def twitter_likes():
	print("twitter likes in process...")

	twit_access_button = driver.find_element(By.XPATH, '/html/body/div[6]/div/div[1]/div/div/div[3]/a[3]')
	twit_access_button.click()

	while True:

		if not click_on_earn_pages_button():
			return

		try:
			like_button = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/section/div/div/div/div/div/div[1]/article/div/div/div/div[3]/div[7]/div/div[3]/div/div/div')
		except:
			like_button = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/section/div/div/div/div/div/div[1]/article/div/div/div/div[3]/div[8]/div/div[3]/div/div/div')

		scroll_into_view(like_button)
		actions.send_keys(Keys.UP * 3)
		actions.perform()
		time.sleep(1)
		like_button.click()
		time.sleep(3)
		driver.close()
		driver.switch_to.window(driver.window_handles[0])
		click_on_confirm_button()

def youtube_likes():
	print("youtube likes in process...")

	yt_access_button = driver.find_element(By.XPATH, '/html/body/div[6]/div/div[1]/div/div/div[2]/a[1]')
	yt_access_button.click()

	while True:
		
		if not click_on_earn_pages_button():
			return

		like_button = driver.find_element(By.XPATH, '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[2]/ytd-watch-metadata/div/div[2]/div[2]/div/div/ytd-menu-renderer/div[1]/ytd-toggle-button-renderer[1]/a')

		scroll_into_view(like_button)
		time.sleep(1)
		like_button.click()
		time.sleep(3)
		driver.close()
		driver.switch_to.window(driver.window_handles[0])
		click_on_confirm_button()

if __name__ == '__main__':
	print("dolla dolla bill y'all")
	print("starting the bot...")

	profile_dir = "firefox-profile"

	if not exists(profile_dir):
		mkdir(profile_dir)

	options = webdriver.FirefoxOptions()
	options.add_argument("--headless")
	options.add_argument("--profile") 
	options.add_argument(profile_dir) 

	driver = webdriver.Firefox(options = options)

	print("web-driver profile loaded")

	driver.implicitly_wait(10)
	driver.fullscreen_window()
	actions = ActionChains(driver)

	twitter_login(username = "riseld02", password = "123123.T")
	like4like_login(username = "testingsecondacc", password = "123123.Tt")

	earn_pages_url = "https://www.like4like.org/user/earn-pages.php"
	driver.get(earn_pages_url)

	if driver.current_url != earn_pages_url:
		print("like4like login failed.")
		exit(1)

	ops = [twitter_follows, twitter_likes, twitter_retweets]

	while True:

		for i in range(len(ops)):

			try:
				ops[i]()
			except KeyboardInterrupt:
				driver.quit()
				exit(1)
			except:
				# maybe close existing windows first
				driver.get(earn_pages_url)
				pass

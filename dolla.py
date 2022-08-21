#!/usr/bin/env python

import time
import pickle
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

def click_on_earn_pages_button():

	try:
		driver.find_element(By.CSS_SELECTOR, '.earn_pages_button').click()
		time.sleep(2)
		driver.switch_to.window(driver.window_handles[1])
		return True
	except:
		driver.back()
		print(ERROR + "could not click on earn_pages button. the current action cannot be performed")
		return False

def click_on_confirm_button():

	try:
		driver.find_element(By.CSS_SELECTOR, 'img[title="Click On The Button To Confirm Interaction!"]').click()
		return True
	except:
		print(ERROR + "could not click on confirm button")
		driver.refresh()
		return False

def scroll_into_view(element):
	dest = element.location_once_scrolled_into_view

	if dest == None:
		raise Exception("dict is null somehow")

	driver.execute_script("window.scrollBy({X}, {Y})".format(X = dest["x"], Y = dest["y"]))
	time.sleep(2)

def youtube_login(username, password):
	print(INFO + "logging into youtube")
	driver.get("https://accounts.google.com/signin/v2/identifier?service=youtube&uilel=3&passive=true&continue=https%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26app%3Ddesktop%26hl%3Den%26next%3Dhttps%253A%252F%252Fwww.youtube.com%252F&hl=en&ec=65620&flowName=GlifWebSignIn&flowEntry=ServiceLogin")

	try:
		_ = driver.find_element(By.XPATH, "/html/body/ytd-app/div[1]/div/ytd-masthead/div[3]/div[3]/div[2]/ytd-topbar-menu-button-renderer[1]/div/a/yt-icon-button/button/yt-icon")
		print(INFO + "already logged into youtube")
		return
	except:
		pass

	username_inp = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input')
	username_inp.clear()
	username_inp.send_keys(username)
	actions.send_keys(Keys.ENTER)
	actions.perform()
	driver.implicitly_wait(20)

	try:
		_ = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[4]/div[2]/div/div[1]/div/div[1]/input")
		print(INFO + "FUCK a captcha came")
	except:
		pass
	password_inp = driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input')
	scroll_into_view(password_inp)
	password_inp.clear()
	time.sleep(1)
	password_inp.send_keys(password)
	actions.send_keys(Keys.ENTER)
	actions.perform()
	time.sleep(5)

	_ = driver.find_element(By.XPATH, "/html/body/ytd-app/div[1]/div/ytd-masthead/div[3]/div[3]/div[2]/ytd-topbar-menu-button-renderer[1]/div/a/yt-icon-button/button/yt-icon")
	time.sleep(3)
	print(INFO + " logged into gooogle im not sure check")

def validate_submission():
	time.sleep(2)

	try:
		header = driver.find_element(By.XPATH, '//*[@id="top-header-earned-credits"]')

		if "block" in header.get_attribute("style"):
			print(INFO + "credits earned :", header.get_attribute("innerHTML"))
			return True
	except:
		pass

	print(WARNING + "action failed")
	driver.back()
	return False

def twitter_follows():
	print(INFO + "twitter follows in process...")

	twit_access_button = driver.find_element(By.XPATH, '/html/body/div[6]/div/div[1]/div/div/div[3]/a[1]')
	scroll_into_view(twit_access_button)
	actions.send_keys(Keys.UP * 4)
	actions.perform()
	time.sleep(1)
	twit_access_button.click()

	while True:

		if not click_on_earn_pages_button():
			return

		time.sleep(5)
		actions.send_keys(Keys.RETURN)
		actions.perform()
		time.sleep(3)
		driver.close()
		time.sleep(2)
		driver.switch_to.window(driver.window_handles[0])
		click_on_confirm_button()

		if not validate_submission():
			return
	
def get_accessor(type, paths):

	for path in paths:

		try:
			accessor = driver.find_element(type, path)
			return accessor
		except:
			pass

	assert len(driver.window_handles) == 2
	driver.close()
	driver.switch_to.window(driver.window_handles[0])
	raise Exception("could not find accessor for current action")

def twitter_retweets():
	print(INFO + "twitter retweets in process...")

	twit_access_button = driver.find_element(By.XPATH, '/html/body/div[6]/div/div[1]/div/div/div[3]/a[2]')
	scroll_into_view(twit_access_button)
	actions.send_keys(Keys.UP * 4)
	actions.perform()
	time.sleep(1)
	twit_access_button.click()

	while True:

		if not click_on_earn_pages_button():
			return

		retweet_button = get_accessor(By.XPATH, ["/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/section/div/div/div/div/div/div[1]/article/div/div/div/div[3]/div[7]/div/div[2]/div/div/div", "/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/section/div/div/div/div/div/div[1]/article/div/div/div/div[3]/div[8]/div/div[2]/div/div/div"])

		scroll_into_view(retweet_button)
		actions.send_keys(Keys.UP * 3)
		actions.perform()
		time.sleep(1)
		retweet_button.click()
		actions.send_keys(Keys.RETURN)
		actions.perform()
		time.sleep(3)
		driver.close()
		time.sleep(2)
		driver.switch_to.window(driver.window_handles[0])
		click_on_confirm_button()

		if not validate_submission():
			return

def twitter_likes():
	print(INFO + "twitter likes in process...")

	twit_access_button = driver.find_element(By.XPATH, '/html/body/div[6]/div/div[1]/div/div/div[3]/a[3]')
	scroll_into_view(twit_access_button)
	actions.send_keys(Keys.UP * 4)
	actions.perform()
	time.sleep(1)
	twit_access_button.click()

	while True:

		if not click_on_earn_pages_button():
			return

		like_button = get_accessor(By.XPATH, ["/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/section/div/div/div[1]/div/div/div[1]/article/div/div/div/div[3]/div[7]/div/div[3]/div/div/div", "/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/section/div/div/div[1]/div/div/div[1]/article/div/div/div/div[3]/div[8]/div/div[3]/div/div/div"])

		scroll_into_view(like_button)
		actions.send_keys(Keys.UP * 3)
		actions.perform()
		time.sleep(2)
		like_button.click()
		time.sleep(3)
		driver.close()
		time.sleep(2)
		driver.switch_to.window(driver.window_handles[0])
		click_on_confirm_button()

		if not validate_submission():
			return

def twitch_follows():
	print(INFO + "twitch follows in process...")

	twitch_access_button = driver.find_element(By.XPATH, '/html/body/div[6]/div/div[1]/div/div/div[15]/a')
	scroll_into_view(twitch_access_button)
	twitch_access_button.click()

	while True:

		if not click_on_earn_pages_button():
			return

		follow_button = get_accessor(By.XPATH, ['/html/body/div[1]/div/div[2]/div/main/div[1]/div[3]/div/div/div[1]/div[1]/div[2]/div/section/div/div/div/div/div[2]/div[1]/div[2]/div[2]/div[2]/div/div[2]/div/div[1]/div/div/div/div/button/div/div/div/span/div', '/html/body/div[1]/div/div[2]/div/main/div[1]/div[3]/div/div/div[1]/div[1]/div[2]/div/section/div[2]/div[1]/div[2]/div[1]/div[2]/div/div[2]/div/div[1]/div/div/div/div/button'])

		print(follow_button)
		scroll_into_view(follow_button)
		time.sleep(3)
		follow_button.click()
		time.sleep(3)

		driver.close()
		time.sleep(2)
		driver.switch_to.window(driver.window_handles[0])
		click_on_confirm_button()

		if not validate_submission():
			return

def youtube_likes():
	print(INFO + "youtube likes in process...")

	yt_access_button = driver.find_element(By.XPATH, '/html/body/div[6]/div/div[1]/div/div/div[2]/a[1]')
	yt_access_button.click()

	while True:

		if not click_on_earn_pages_button():
			print(INFO + "total credits : ", get_credits())
			return


		like_button = driver.find_element(By.XPATH, '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[2]/div[7]/div[1]/div[2]/ytd-video-primary-info-renderer/div/div/div[3]/div/ytd-menu-renderer/div[1]/ytd-toggle-button-renderer[1]/a/yt-icon-button/button/yt-icon')
		time.sleep(3)
		like_button.click()
		time.sleep(4)
		driver.close()
		time.sleep(2)
		driver.switch_to.window(driver.window_handles[0])
		click_on_confirm_button()
		time.sleep(1)

def youtube_subs():
	print(INFO + "youtube subs in process...")

	yts_access_button = driver.find_element(By.XPATH, '/html/body/div[6]/div/div[1]/div/div/div[2]/a[2]')
	yts_access_button.click()

	while True:

		if not click_on_earn_pages_button():
			return

		time.sleep(10)
		actions.send_keys(Keys.TAB * 15)
		actions.perform()
		actions.send_keys(Keys.ENTER)
		actions.perform()
		time.sleep(6)
		driver.close()
		time.sleep(2)
		driver.switch_to.window(driver.window_handles[0])
		time.sleep(2)
		click_on_confirm_button()
		time.sleep(1)
		
def instagram_followers():
	print(INFO + "instagram followers in process...")

	ig_access_button = driver.find_element(By.XPATH, '/html/body/div[6]/div/div[1]/div/div/div[7]/a[1]')
	scroll_into_view(ig_access_button)
	ig_access_button.click()

	while True:

		if not click_on_earn_pages_button():
			return


		sub_button = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/main/div/header/section/div[1]/div[1]/div/div/button/div/div')
		sub_button.click()
		time.sleep(5)
		driver.close()
		time.sleep(2)
		driver.switch_to.window(driver.window_handles[0])
		click_on_confirm_button()
		time.sleep(1)

def instagram_likes():
	print(INFO + "instagram likes in process...")

	ig_access_button = driver.find_element(By.XPATH, '/html/body/div[6]/div/div[1]/div/div/div[7]/a[2]')
	scroll_into_view(ig_access_button)
	ig_access_button.click()

	while True:

		if not click_on_earn_pages_button():
			return

		like_button = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/main/div[1]/div[1]/article/div/div[2]/div/div[2]/section[1]/span[1]/button/div[2]/span/svg/path')
		like_button.click()
		time.sleep(5)

		driver.close()
		time.sleep(2)
		driver.switch_to.window(driver.window_handles[0])
		click_on_confirm_button()

		time.sleep(1)

def fetch_cookies():
	print(INFO + "fetching cookies...")

	def get_spec_cookies(filename):

		if validate_submission():
			time.sleep(2)
			print(INFO + "credits earned :", get_credits() - cur_credits)
			time.sleep(3)
		else:
			soundcloud_follows.fails = soundcloud_follows.fails + 1
			print(INFO + "total credits : ", get_credits())
			return

		try:
			print(INFO + "adding {} cookies".format(filename))
			cookies = pickle.load(open(filename + ".pkl", "rb"))

			for cookie in cookies:
				driver.add_cookie(cookie)

			print(INFO + "added {} cookies".format(filename))
			return True
		except:
			print(WARNING + "couldn't add {} cookies".format(filename))
			return False

	driver.get("https://like4like.org/login")

	if not get_spec_cookies(".like4like"):
		raise Exception("cannot proceed anymore as like4like login failed")

	allowed_ops = []

	# driver.get("https://twitch.tv")

	# if get_spec_cookies(".twitch"):
	# 	allowed_ops.append(twitch_follows)

	driver.get("https://twitter.com")

	if get_spec_cookies(".twitter"):
		allowed_ops.append(twitter_likes)
		allowed_ops.append(twitter_follows)
		allowed_ops.append(twitter_retweets)

	# driver.get("https://instagram.com")

	# if get_spec_cookies(".instagram"):
		# allowed_ops.append(instagram_likes)
		# allowed_ops.append(instagram_followers)

	return allowed_ops

def get_driver_options():
	options = webdriver.ChromeOptions()

	options.add_argument("--headless")
	# options.add_argument("--kiosk")

	return options

if __name__ == '__main__':
	WARNING = "[WARNING] "
	INFO = "[INFO] "
	ERROR = "[ERROR] "

	print("-" * 30 + "\ndolla dolla bill y'all\n" + '-' * 30)
	print(INFO + "starting the bot...")
	driver.implicitly_wait(15)
	driver.fullscreen_window()

	driver = webdriver.Chrome(options = get_driver_options())
	driver.implicitly_wait(15)
	actions = ActionChains(driver)

	ops = fetch_cookies()

	if len(ops) == 0:
		print("no operation can be performed. try refreshing the cookies. exiting...")
		exit(1)

	print("-" * 30 + "\n{} performable operations : ".format(len(ops)))

	for op in ops:
		print('\t' + op.__name__)

	print("-" * 30)

	earn_pages_url = "https://www.like4like.org/user/earn-pages.php"
	driver.get(earn_pages_url)

	while True:

		for i in range(len(ops)):

			try:
				ops[i]()
			except KeyboardInterrupt:
				driver.quit()
				exit(1)
			except Exception as e:
				print(ERROR + str(e))

				while True:

					try:
						driver.get(earn_pages_url)
						break
					except:
						print(ERROR + "could not load like4like.com. check your connection. retrying in 60 seconds...")
						time.sleep(60)
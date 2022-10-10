#!/usr/bin/env python

import time
import json
import sys
from os.path import exists
from threading import Timer
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common import exceptions
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

def click_on_earn_pages_button(caller):

	try:
		earn_pages_button = driver.find_element(By.CSS_SELECTOR, '.earn_pages_button')
		scroll_into_view(earn_pages_button)
		driver.execute_script("window.scrollBy(0, 200)")
		time.sleep(2)
		earn_pages_button.click()
		driver.switch_to.window(driver.window_handles[1])
	except Exception:

		try:
			error_element = driver.find_element(By.ID, "error-text")
			error = error_element.get_attribute("innerHTML")

			if "minutes" in error:
				digits = [int(x) for x in error.split() if x.isdigit()]

				if len(digits) == 0:
					raise Exception("(like4like message) " + error)

				if len(digits) == 1:
					timeout_mins = digits[0]
				else:
					timeout_mins = digits[1]

				print(WARNING + "{} got a timeout for {} minutes".format(caller.__name__, timeout_mins))
				print(WARNING + "removing {} from performable operations".format(caller.__name__))
				ops.remove(caller)
				Timer(timeout_mins * 60, add_back, [caller]).start()
			elif "No tasks are currently available" in error:
				deactive_secs = 600
				print(INFO + "No tasks available for {}. Deactivating it for {} seconds".format(caller.__name__, deactive_secs))
				ops.remove(caller)
				Timer(deactive_secs, add_back, [caller]).start()

			raise Exception("(like4like message) " + error)
		except exceptions.NoSuchElementException:

			try:
				reward = driver.find_element(By.CLASS_NAME, "captchaImage")
				print(INFO + "found reward images. clicking on a random one..")
				scroll_into_view(reward)
				reward.click()
				driver.refresh()
				click_on_earn_pages_button(caller)
			except:
				raise Exception("couldn't click on earn-credits-button")

def add_back(function):
	print(INFO + "adding {} back to performable operations".format(function.__name__))
	ops.append(function)
	print_performable_ops()

def click_on_confirm_button():
	switch_to_main_window()
	confirm_button = driver.find_element(By.CSS_SELECTOR, 'img[title="Click On The Button To Confirm Interaction!"]')
	scroll_into_view(confirm_button)
	confirm_button.click()
	validate_submission()

def scroll_into_view(element):
	dest = element.location_once_scrolled_into_view
	driver.execute_script("window.scrollBy({X}, {Y})".format(X = dest["x"], Y = dest["y"]))
	driver.execute_script("window.scrollBy(0, -100)")
	time.sleep(3)

def switch_to_main_window():
	driver.close()
	driver.switch_to.window(driver.window_handles[0])

def get_driver_options():
	options = webdriver.ChromeOptions()

	if not (len(sys.argv) > 1 and sys.argv[1] == "-n"):
		options.add_argument("--headless")

	options.add_argument("log-level=3")
	options.add_argument("--disable-notifications")
	options.add_argument("--mute-audio")

	return options

def print_performable_ops():
	print("-" * 30 + "\n{} performable operations : ".format(len(ops)))

	for op in ops:
		print('\t' + op.__name__)

	print("-" * 30)

def validate_submission():

	for _ in range(15):
		time.sleep(1)

		header = driver.find_element(By.XPATH, '//*[@id="top-header-earned-credits"]')

		if "block" in header.get_attribute("style"):
			print(INFO + "credits earned :", header.get_attribute("innerHTML"))
			return

	raise Exception("action failed")

def get_accessor(type, paths):

	for path in paths:

		try:
			accessor = driver.find_element(type, path)
			return accessor
		except:
			pass

	switch_to_main_window()
	raise Exception("could not find accessor for current action")

def twitter_follows():

	while True:
		click_on_earn_pages_button(twitter_follows)

		time.sleep(10)
		actions.send_keys(Keys.RETURN)
		actions.perform()
		time.sleep(AFTER_SECS)

		click_on_confirm_button()

def twitter_retweets():

	while True:
		click_on_earn_pages_button(twitter_retweets)

		retweet_button = get_accessor(By.XPATH, ["/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/section/div/div/div/div/div/div[1]/article/div/div/div/div[3]/div[7]/div/div[2]/div/div/div", "/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/section/div/div/div/div/div/div[1]/article/div/div/div/div[3]/div[8]/div/div[2]/div/div/div"])

		scroll_into_view(retweet_button)
		retweet_button.click()
		actions.send_keys(Keys.RETURN)
		actions.perform()
		time.sleep(AFTER_SECS)

		click_on_confirm_button()

def twitter_likes():

	while True:
		click_on_earn_pages_button(twitter_likes)

		like_button = get_accessor(By.XPATH, ["/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/section/div/div/div/div/div/div[1]/article/div/div/div/div[3]/div[7]/div/div[3]/div/div/div", "/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/section/div/div/div/div/div/div[1]/article/div/div/div/div[3]/div[8]/div/div[3]/div/div/div"])

		scroll_into_view(like_button)
		like_button.click()
		time.sleep(AFTER_SECS)

		click_on_confirm_button()

def twitch_follows():

	while True:
		click_on_earn_pages_button(twitch_follows)

		follow_button = get_accessor(By.XPATH, ['/html/body/div[1]/div/div[2]/div/main/div[1]/div[3]/div/div/div[1]/div[1]/div[2]/div/section/div/div/div/div/div[2]/div[1]/div[2]/div[2]/div[2]/div/div[2]/div/div[1]/div/div/div/div/button/div/div/div/span/div', '/html/body/div[1]/div/div[2]/div/main/div[1]/div[3]/div/div/div[1]/div[1]/div[2]/div/section/div[2]/div[1]/div[2]/div[1]/div[2]/div/div[2]/div/div[1]/div/div/div/div/button'])

		scroll_into_view(follow_button)
		follow_button.click()
		time.sleep(AFTER_SECS)

		click_on_confirm_button()

def youtube_likes():

	while True:
		click_on_earn_pages_button(youtube_likes)

		like_button = get_accessor(By.XPATH, ["//div[@id='info']//ytd-toggle-button-renderer[1]//a[1]//yt-icon-button[1]//button[1]//yt-icon[1]"])

		scroll_into_view(like_button)
		time.sleep(BEFORE_SECS)
		like_button.click()
		time.sleep(AFTER_SECS)

		click_on_confirm_button()

def youtube_subs():

	while True:
		click_on_earn_pages_button(youtube_subs)

		sub_button = get_accessor(By.XPATH, ['//*[@id=\"subscribe-button\"]/ytd-subscribe-button-renderer'])

		scroll_into_view(sub_button)
		time.sleep(BEFORE_SECS)
		sub_button.click()
		time.sleep(AFTER_SECS)

		click_on_confirm_button()

def soundcloud_follows():

	while True:
		click_on_earn_pages_button(soundcloud_follows)

		follow_button = get_accessor(By.XPATH, ["/html/body/div[1]/div[2]/div[2]/div/div[3]/div/div[2]/div/button[1]"])
		time.sleep(BEFORE_SECS)
		scroll_into_view(follow_button)
		follow_button.click()
		time.sleep(AFTER_SECS)

		click_on_confirm_button()

def soundcloud_likes():

	while True:
		click_on_earn_pages_button(soundcloud_likes)

		like_button = get_accessor(By.XPATH, ["/html/body/div[1]/div[2]/div[2]/div/div[3]/div[1]/div/div[1]/div/div/div[2]/div/div/button[1]"])
		scroll_into_view(like_button)
		time.sleep(BEFORE_SECS)
		like_button.click()
		time.sleep(AFTER_SECS)

		click_on_confirm_button()

def fetch_cookies():
	print(INFO + "fetching cookies...")

	allowed_ops = []

	def get_spec_cookies(platform):

		urls = {
			"twitch" : "https://twitch.tv",
			"twitter" : "https://twitter.com",
			"youtube" : "https://youtube.com",
			"soundcloud" : "https://soundcloud.com",
			"like4like" : "https://like4like.org/login",
		}

		filename = '.' + platform + '.json'

		if not exists(filename):
			print(ERROR + "couldn't add cookies for {} because {} doesn't exist".format(platform, filename))
			return

		print(INFO + "adding {} cookies".format(platform))

		driver.get(urls[platform])

		cookies_file = open(filename, "r")
		cookies = json.loads(cookies_file.read())

		for cookie in cookies:
			driver.add_cookie(cookie)

		print(INFO + "added {} cookies".format(platform))

		if platform == "like4like":
			return

		operations = {
			"twitter" : [twitter_likes, twitter_follows, twitter_retweets],
			"twitch" : [twitch_follows],
			"youtube" : [youtube_likes, youtube_subs],
			"soundcloud" : [soundcloud_likes, soundcloud_follows],
		}

		for operation in operations[platform]:
			allowed_ops.append(operation)

	platforms = [
		"like4like",
		"youtube",
		"twitter",
		"soundcloud",
		"twitch",
	]

	for platform in platforms:
		get_spec_cookies(platform)

	return allowed_ops

if __name__ == '__main__':
	WARNING = "[WARNING] "
	INFO = "[INFO] "
	ERROR = "[ERROR] "
	BEFORE_SECS = 10
	AFTER_SECS = 10

	print("-" * 30 + "\ndolla dolla bill y'all\n" + '-' * 30)
	print(INFO + "starting the bot...")

	driver = webdriver.Chrome(options = get_driver_options(), service = ChromeService(ChromeDriverManager().install()))
	driver.implicitly_wait(15)
	actions = ActionChains(driver)

	ops = fetch_cookies()

	if len(ops) == 0:
		print("no operation can be performed. try refreshing the cookies. exiting...")
		driver.quit()
		exit(1)

	print_performable_ops()

	base_url = "https://www.like4like.org/earn-credits.php?feature="

	feature_urls = {
		youtube_likes : base_url + "youtube",
		youtube_subs : base_url + "youtubes",
		twitter_follows : base_url + "twitter",
		twitter_likes : base_url + "twitterfav",
		twitter_retweets : base_url + "twitterret",
		twitch_follows : base_url + "twitch",
		soundcloud_follows : base_url + "soundcloudfol",
		soundcloud_likes : base_url + "soundcloudlik",
	}

	while True:

		if len(ops) == 0:
			print(INFO + "no action can be performed currently. trying again after 1 minute...")
			time.sleep(60)
			continue

		for op in ops:

			try:
				driver.get(feature_urls[op])
				print(INFO + "{} in process...".format(op.__name__))
				op()
			except KeyboardInterrupt:
				driver.quit()
				exit(1)
			except Exception as e:
				print(ERROR + str(e))

				if len(driver.window_handles) > 1:
					switch_to_main_window()

				while True:

					try:
						driver.get("https://like4like.org")
						break
					except:
						print(ERROR + "could not load like4like.com. check your connection. retrying in 60 seconds...")
						time.sleep(60)

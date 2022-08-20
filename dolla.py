#!/usr/bin/env python

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
			time.sleep(1)
			driver.switch_to.window(driver.window_handles[1])
			return True
		except:
			driver.refresh()

	driver.back()
	print(ERROR + "could not click on earn_pages button. the current action cannot be performed anymore")
	return False

def click_on_confirm_button():

	for _ in range(3):

		try:
			driver.find_element(By.CSS_SELECTOR, 'img[title="Click On The Button To Confirm Interaction!"]').click()
			return True
		except:
			pass

	print(ERROR + "could not click on confirm button")
	driver.refresh()
	return False

def scroll_into_view(element):
	dest = element.location_once_scrolled_into_view

	if dest == None:
		raise Exception("dict is null somehow")

	driver.execute_script("window.scrollBy({X}, {Y})".format(X = dest["x"], Y = dest["y"]))
	time.sleep(1)

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

def twitter_login(username, password):
	print(INFO + "logging into twitter")
	driver.get("https://www.twitter.com/login")

	try:
		_ = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a/div/span/div/div/span/span")
		print(INFO + "already logged into twitter")
		return
	except:
		pass

	username_inp = driver.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')

	username_inp.send_keys(username)
	actions.send_keys(Keys.RETURN)
	actions.perform()
	time.sleep(1)
	actions.send_keys(password)
	actions.send_keys(Keys.RETURN)
	actions.perform()
	_ = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a/div/span/div/div/span/span")
	time.sleep(3)
	print(INFO + "logged into twitter")

def instagram_login(username, password):
	print(INFO + "logging into instagram")
	driver.get("https://www.instagram.com/")

	try:
		_ = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/main/div[1]/section/div[3]/div[1]/div/div/div[2]/div/div/div/a")
		print(INFO + "already logged into instagram")
		return
	except:
		pass

	username_inp = driver.find_element(By.XPATH, '/html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[1]/div/label/input')

	username_inp.send_keys(username)
	time.sleep(1)
	actions.send_keys(Keys.TAB)
	actions.perform()
	time.sleep(1)
	actions.send_keys(password)
	time.sleep(1)
	actions.send_keys(Keys.ENTER)
	actions.perform()
	_ = driver.find_element(By.XPATH, "/html/body/div[1]/section/main/div/div/div/div/button")
	print(INFO + "logged into instagram")


def get_credits():
	html = driver.find_element(By.CLASS_NAME, "earned-credits").get_attribute("outerHTML")
	s = ""

	for c in html:

		if c.isdigit():
			s += c

	return int(s)

def like4like_login(username, password):
	print(INFO + "logging into like4like")

	login_url = 'https://www.like4like.org/login/'
	driver.get(login_url)

	username_inp = driver.find_element(By.XPATH, '//*[@id="username"]')
	password_inp = driver.find_element(By.XPATH, '//*[@id="password"]')

	username_inp.clear()
	password_inp.clear()

	username_inp.send_keys(username)
	password_inp.send_keys(password)
	password_inp.send_keys(Keys.ENTER)
	time.sleep(5)

	while driver.current_url == login_url:
		print(WARNING + "catpcha detected while logging into like4like. login after solving it to continue")
		print(INFO + "will automatically proceed in 30 seconds")
		time.sleep(30)
		print(INFO + "continuing...")

	print(INFO + "logged into like4like")

def validate_submission():

	try:
		_ = driver.find_element(By.XPATH, '//*[@id="top-header-earned-credits"]')
		return True
	except:
		print(WARNING + "action failed")

	return False

def twitter_follows():

	if twitter_follows.fails == fail_limit:
		print(WARNING + "could not initiate twitter follows because of high failure count")
		return
		
	print(INFO + "twitter follows in process...")

	twitf_access_button = driver.find_element(By.XPATH, '/html/body/div[6]/div/div[1]/div/div/div[3]/a[1]')
	scroll_into_view(twitf_access_button)
	actions.send_keys(Keys.UP * 4)
	actions.perform()
	time.sleep(1)
	twitf_access_button.click()

	while True:
		cur_credits = get_credits()

		if not click_on_earn_pages_button():
			print(INFO + "total credits : ", get_credits())
			return

		time.sleep(5)
		actions.send_keys(Keys.RETURN)
		actions.perform()
		time.sleep(5)
		driver.close()
		driver.switch_to.window(driver.window_handles[0])
		click_on_confirm_button()

		if validate_submission():
			time.sleep(2)
			print(INFO + "credits earned :", get_credits() - cur_credits)
			time.sleep(3)
		else:
			twitter_follows.fails = twitter_follows.fails + 1
			print(INFO + "total credits : ", get_credits())
			return

def twitter_retweets():

	if twitter_retweets.fails == fail_limit:
		print(WARNING + "could not initiate twitter retweets because of high failure count")
		return

	print(INFO + "twitter retweets in process...")

	twitr_access_button = driver.find_element(By.XPATH, '/html/body/div[6]/div/div[1]/div/div/div[3]/a[2]')
	scroll_into_view(twitr_access_button)
	actions.send_keys(Keys.UP * 4)
	actions.perform()
	time.sleep(1)
	twitr_access_button.click()

	while True:
		cur_credits = get_credits()

		if not click_on_earn_pages_button():
			print(INFO + "total credits : ", get_credits())
			return

		try:
			retweet_button = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/section/div/div/div/div/div/div[1]/article/div/div/div/div[3]/div[7]/div/div[2]/div/div/div')
		except:
			retweet_button = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/section/div/div/div/div/div/div[1]/article/div/div/div/div[3]/div[8]/div/div[2]/div/div/div')

		scroll_into_view(retweet_button)
		actions.send_keys(Keys.UP * 3)
		actions.perform()
		time.sleep(1)
		retweet_button.click()
		actions.send_keys(Keys.RETURN)
		actions.perform()
		time.sleep(3)
		driver.close()
		driver.switch_to.window(driver.window_handles[0])
		click_on_confirm_button()

		if validate_submission():
			time.sleep(2)
			print(INFO + "credits earned :", get_credits() - cur_credits)
			time.sleep(3)
		else:
			twitter_follows.fails = twitter_follows.fails + 1
			print(INFO + "total credits : ", get_credits())
			return

def twitter_likes():

	if twitter_likes.fails == fail_limit:
		print(WARNING + "could not initiate twitter likes because of high failure count")
		return
			
	print(INFO + "twitter likes in process...")

	twitl_access_button = driver.find_element(By.XPATH, '/html/body/div[6]/div/div[1]/div/div/div[3]/a[3]')
	scroll_into_view(twitl_access_button)
	actions.send_keys(Keys.UP * 4)
	actions.perform()
	time.sleep(1)
	twitl_access_button.click()

	while True:
		cur_credits = get_credits()

		if not click_on_earn_pages_button():
			print(INFO + "total credits : ", get_credits())
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

		if validate_submission():
			time.sleep(2)
			print(INFO + "credits earned :", get_credits() - cur_credits)
			time.sleep(3)
		else:
			twitter_follows.fails = twitter_follows.fails + 1
			print(INFO + "total credits : ", get_credits())
			return

def twitch_follows():

	if twitch_follows.fails == fail_limit:
		print(WARNING + "could not initiate twitch follows because of high failure count")
		return
			
	print(INFO + "twitch follows in process...")

	twitch_access_button = driver.find_element(By.XPATH, '/html/body/div[6]/div/div[1]/div/div/div[15]/a')
	scroll_into_view(twitch_access_button)
	twitch_access_button.click()

	while True:
		cur_credits = get_credits()

		if not click_on_earn_pages_button():
			print(INFO + "total credits : ", get_credits())
			return

		follow_button = driver.find_element(By.CSS_SELECTOR, 'button[data-a-target="follow-button"]')
		scroll_into_view(follow_button)
		time.sleep(5)
		follow_button.click()
		time.sleep(3)

		driver.close()
		driver.switch_to.window(driver.window_handles[0])
		click_on_confirm_button()

		if validate_submission():
			time.sleep(2)
			print(INFO + "credits earned :", get_credits() - cur_credits)
			time.sleep(3)
		else:
			twitch_follows.fails = twitch_follows.fails + 1
			print(INFO + "total credits : ", get_credits())
			return

def youtube_likes():

	if youtube_likes.fails == fail_limit:
		print(WARNING + "could not initiate youtube likes because of high failure count")
		return
		
	print(INFO + "youtube likes in process...")

	yt_access_button = driver.find_element(By.XPATH, '/html/body/div[6]/div/div[1]/div/div/div[2]/a[1]')
	yt_access_button.click()

	while True:
		cur_credits = get_credits()

		if not click_on_earn_pages_button():
			return

		like_button = driver.find_element(By.XPATH, '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[2]/div[7]/div[1]/div[2]/ytd-video-primary-info-renderer/div/div/div[3]/div/ytd-menu-renderer/div[1]/ytd-toggle-button-renderer[1]/a/yt-icon-button/button/yt-icon')
		time.sleep(3)
		like_button.click()
		time.sleep(4)
		driver.close()
		driver.switch_to.window(driver.window_handles[0])
		click_on_confirm_button()
		time.sleep(1)

		upd_credits = get_credits()
		print("updated credits : ", upd_credits)

		if upd_credits > cur_credits:
			print(INFO + "action completed")
		else:
			print(ERROR + "action failed")
			youtube_likes.fails = youtube_likes.fails + 1

def youtube_subs():

	if youtube_subs.fails == fail_limit:
		print(WARNING + "could not initiate youtube subs because of high failure count")
		return

	print(INFO + "youtube subs in process...")

	yts_access_button = driver.find_element(By.XPATH, '/html/body/div[6]/div/div[1]/div/div/div[2]/a[2]')
	yts_access_button.click()

	while True:
		cur_credits = get_credits()

		if not click_on_earn_pages_button():
			return

		time.sleep(10)
		actions.send_keys(Keys.TAB * 15)
		actions.perform()
		actions.send_keys(Keys.ENTER)
		actions.perform()
		time.sleep(6)
		driver.close()
		driver.switch_to.window(driver.window_handles[0])
		time.sleep(2)
		click_on_confirm_button()
		time.sleep(1)

		upd_credits = get_credits()
		print("updated credits : ", upd_credits)

		if upd_credits > cur_credits:
			print(INFO + "action completed")
			youtube_subs.done = youtube_subs.done + 1
		else:
			print(ERROR + "action failed")
			youtube_subs.fails = youtube_subs.fails + 1
		
		if youtube_subs.done == 30:
			print(WARNING + "we hit the daily limit")
			return

def instagram_followers():
	
	if instagram_followers.fails == fail_limit:
		print(WARNING + "too many failures we skipping this")
		return
		
	print(INFO + "instagram followers in process...")

	ig_access_button = driver.find_element(By.XPATH, '/html/body/div[6]/div/div[1]/div/div/div[7]/a[1]')
	scroll_into_view(ig_access_button)
	ig_access_button.click()

	while True:
		cur_credits = get_credits()

		if not click_on_earn_pages_button():
			return


		sub_button = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/main/div/header/section/div[1]/div[1]/div/div/button/div/div')
		sub_button.click()
		time.sleep(5)
		driver.close()
		driver.switch_to.window(driver.window_handles[0])
		click_on_confirm_button()
		time.sleep(1)

		upd_credits = get_credits()
		print("updated credits : ", upd_credits)

		if upd_credits > cur_credits:
			print(INFO + "action completed")
			instagram_likes.done = instagram_likes.done + 1
		else:
			print(ERROR + "action failed")
			instagram_likes.fails = instagram_likes.fails + 1

		if instagram_followers.done == 15:
			print(WARNING + "limit for likes is hit,we moving to next task")
			return

def instagram_likes():
	
	if instagram_likes.fails == fail_limit:
		print(WARNING + "too many failures we skipping this")
		return
		
	print(INFO + "instagram likes in process...")

	ig_access_button = driver.find_element(By.XPATH, '/html/body/div[6]/div/div[1]/div/div/div[7]/a[2]')
	scroll_into_view(ig_access_button)
	ig_access_button.click()

	while True:
		cur_credits = get_credits()

		if not click_on_earn_pages_button():
			return


		like_button = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/main/div[1]/div[1]/article/div/div[2]/div/div[2]/section[1]/span[1]/button/div[2]/span/svg/path')
		like_button.click()
		time.sleep(5)
		driver.close()
		driver.switch_to.window(driver.window_handles[0])
		click_on_confirm_button()
		time.sleep(1)

		upd_credits = get_credits()
		print("updated credits : ", upd_credits)

		if upd_credits > cur_credits:
			print(INFO + "action completed")
			instagram_likes.done = instagram_likes.done + 1
		else:
			print(ERROR + "action failed")
			instagram_likes.fails = instagram_likes.fails + 1

		if instagram_likes.done == 50:
			print(WARNING + "limit for likes is hit,we moving to next task")
			return

def read_credentials():
	print("reading the credentials...")

	creds = {}

	with open(".creds.ini", "r") as file:
		creds["youtube_username"] = file.readline()
		creds["youtube_password"] = file.readline()
		creds["instagram_username"] = file.readline()
		creds["instagram_password"] = file.readline()
		creds["twitter_username"] = file.readline()
		creds["twitter_password"] = file.readline()
		creds["like4like_username"] = file.readline()
		creds["like4like_password"] = file.readline()

	print("credentials read successfully")
	return creds

if __name__ == '__main__':
	WARNING = "[WARNING] "
	INFO = "[INFO] "
	ERROR = "[ERROR] "

	print("*" * 30 + "\ndolla dolla bill y'all\n" + '-' * 30)

	try:
		creds = read_credentials()
	except:
		print("could not read the credentials. cannot proceed. exiting...")
		exit(1)

	print(INFO + "starting the bot...")

	profile_dir = "firefox-profile"

	if not exists(profile_dir):
		mkdir(profile_dir)

	options = webdriver.FirefoxOptions()
 
	options.add_argument("--headless")
	options.add_argument("--profile")
	options.add_argument(profile_dir)
	user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36'
	options.add_argument('user-agent={0}'.format(user_agent))

	driver = webdriver.Firefox(options = options)
	print(INFO + "web-driver profile loaded")

	driver.implicitly_wait(10)
	driver.fullscreen_window()

	actions = ActionChains(driver)

	youtube_login(username = creds["youtube_username"], password = creds["youtube_password"])
	instagram_login(username = creds["instagram_username"], password = creds["instagram_password"])
	twitter_login(username = creds["twitter_username"], password = creds["twitter_password"])
	like4like_login(username = creds["like4like_username"], password = creds["like4like_password"])

	earn_pages_url = "https://www.like4like.org/user/earn-pages.php"
	driver.get(earn_pages_url)

	fail_limit = 5
	youtube_subs.fails = 0
	youtube_likes.fails = 0
	twitter_likes.fails = 0
	twitter_retweets.fails = 0
	twitter_follows.fails = 0
	instagram_likes.fails = 0

	youtube_subs.done = 0
	instagram_likes.done = 0
	instagram_followers.done = 0

	ops = [twitter_likes,twitter_retweets,twitter_follows,instagram_likes,youtube_subs,youtube_likes]
	
	

	while True:

		for i in range(len(ops)):

			try:
				ops[i]()
			except KeyboardInterrupt:
				driver.quit()
				exit(1)
			except:

				while True:

					try:
						driver.get(earn_pages_url)
						break
					except:
						print(ERROR + "could not load like4like.com. check your connection. retrying in 60 seconds...")
						time.sleep(60)
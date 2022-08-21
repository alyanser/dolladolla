#!/usr/bin/env python

import time
import pickle
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

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
		wait_seconds = 20
		print(INFO + "will automatically proceed in {} seconds".format(wait_seconds))
		time.sleep(wait_seconds)
		print(INFO + "continuing...")


	print(INFO + "logged into like4like")

def instagram_login(username, password):
	print(INFO + "logging into instagram")
	driver.get("https://www.instagram.com/")

	username_inp = driver.find_element(By.XPATH, '/html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[1]/div/label/input')

	username_inp.send_keys(username)
	actions.send_keys(Keys.TAB)
	actions.send_keys(password)
	actions.send_keys(Keys.ENTER)
	actions.perform()

	_ = driver.find_element(By.XPATH, "/html/body/div[1]/section/main/div/div/div/div/button")
	print(INFO + "logged into instagram")

def twitter_login(username, password):
	print(INFO + "logging into twitter")
	driver.get("https://www.twitter.com/login")

	username_inp = driver.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')

	username_inp.send_keys(username)
	actions.send_keys(Keys.RETURN)
	actions.perform()
	time.sleep(2)
	actions.send_keys(password)
	actions.send_keys(Keys.RETURN)
	actions.perform()

	_ = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div")
	print(INFO + "logged into twitter")

def twitch_login(username, password):
	print(INFO + "logging into twitch.tv...")
	driver.get("https://www.twitch.tv/login")

	username_inp = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div[3]/div/div/div/div[3]/form/div/div[1]/div/div[2]/input')
	username_inp.send_keys(username)
	actions.send_keys(Keys.TAB)
	actions.send_keys(password)
	actions.send_keys(Keys.RETURN)
	actions.perform()

	_ = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/nav/div/div[3]/div[5]/div[1]/div/div[1]/button/div/div[2]')
	print(INFO + "logged into twitch.tv")

def read_credentials():
	print(INFO + "reading credentials...")
	creds = {}

	with open(".creds.ini", "r") as file:

		for line in file:
			list = line.split()
			assert len(list) == 3 and list[1] == ':'
			creds[list[0]] = list[2]

	print(INFO + "credentials read successfully")
	return creds

def save_cookies(filename):
	print(INFO + "writing cookies to ", filename, ".pkl ...", sep = '')
	pickle.dump(driver.get_cookies(), open(filename + '.pkl', "wb"))

def obtain_cookies(platform):

	if platform == "instagram":
		login_function = instagram_login
	elif platform == "twitter":
		login_function = twitter_login
	elif platform == "like4like":
		login_function = like4like_login
	elif platform == "twitch":
		login_function = twitch_login
	else:
		print(ERROR + "unrecognized platform : {}. cannot proceed".format(platform))
		return

	username_head = platform + "_username"
	password_head = platform + "_password"
	cookie_filename = "." + platform

	if username_head in creds and password_head in creds:
		print(INFO + "found {} credentials. obtaining cookies...".format(platform))
		driver.delete_all_cookies()

		try:
			login_function(username = creds[username_head], password = creds[password_head])
			save_cookies(cookie_filename)
		except:
			print(ERROR + "couldn't login into {}. no cookies added.".format(platform))

	else:
		print(WARNING + "couldn't find {} credentials".format(platform))

if __name__ == '__main__':
	WARNING = "[WARNING] "
	INFO = "[INFO] "
	ERROR = "[ERROR] "

	try:
		creds = read_credentials()
	except:
		print(ERROR + "could not read credentials. exiting...")
		exit(1)

	driver = webdriver.Chrome()
	driver.implicitly_wait(15)
	actions = webdriver.ActionChains(driver)

	obtain_cookies("like4like")
	obtain_cookies("instagram")
	obtain_cookies("twitter")
	obtain_cookies("twitch")

	print(INFO + "closing the driver...")
	driver.close()

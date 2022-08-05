import time
from os.path import exists
from os import mkdir
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

profile_dir = "firefox-profile"
like_url = 'https://www.like4like.org'
wait_interval = 30 # seconds

like_username = "testingsecondacc"
like_password = "123123.Tt"

twitter_username = "riseld02"
twitter_password = "123123.T"

insta_username = "reallysomeone_"
insta_password = "reallysomeone123"

def click_on_earn_pages_button():

	for _ in range(3):

		try:
			driver.find_element(By.XPATH, '/html/body/div[6]/div/div[1]/div/div[2]/div[4]/div[1]/div[2]/div[1]/div/div[3]/div/div/a').click()
			time.sleep(3)
			driver.switch_to.window(driver.window_handles[1])
			return True
		except:
			driver.refresh()

	driver.back()
	return False

def click_on_confirm_button():

	for _ in range(3):

		try:
			confirm_button = driver.find_element(By.XPATH, '/html/body/div[6]/div/div[1]/div/div[2]/div[4]/div[1]/div[2]/div[1]/div/div[1]/a/img')
			confirm_button.click()
			print("action confirmed successfully")
			return
		except:
			pass

	print("could not click on confirm button")
	driver.refresh()

def scroll_and_click(element):
	driver.execute_script("window.scrollBy(0, {Y})".format(Y = element.location_once_scrolled_into_view))
	time.sleep(1)
	element.click()

def twitter_follows():
	print("twitter follows in process...")

	twit_access_button = driver.find_element(By.XPATH, '/html/body/div[6]/div/div[1]/div/div/div[3]/a[1]')
	scroll_and_click(twit_access_button)

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

		time.sleep(2)
		actions.send_keys(Keys.RETURN) # emulate pressing follow button
		actions.perform()
		time.sleep(3)
		driver.close()
		driver.switch_to.window(driver.window_handles[0])
		click_on_confirm_button()

def insta_follows():
	print("instagram follows in process...")

	insta_access_button = driver.find_element(By.CSS_SELECTOR, 'a[title="Earn Credits By Instagram Follows"]')
	scroll_and_click(insta_access_button)

	while True:

		if not click_on_earn_pages_button():
			return

		follow_button = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/main/div/header/section/div[1]/div[2]/div/div[2]/button/div/div')
		time.sleep(2)
		follow_button.click()
		time.sleep(3)
		driver.close()
		driver.switch_to.window(driver.window_handles[0])
		click_on_confirm_button()

def youtube_likes():
	print("youtube likes in process...")

	yt_access_button = driver.find_element(By.XPATH, '')
	scroll_and_click(yt_access_button)

	while True:
		
		if not click_on_earn_pages_button():
			return

		like_button = driver.find_element(By.XPATH, '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[2]/ytd-watch-metadata/div/div[2]/div[2]/div/div/ytd-menu-renderer/div[1]/ytd-toggle-button-renderer[1]/a')
		time.sleep(2)
		scroll_and_click(like_button)
		time.sleep(3)
		driver.close()
		driver.switch_to.window(driver.window_handles[0])
		click_on_confirm_button()

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
	print("web-driver profile loaded")

	driver.implicitly_wait(wait_interval)
	actions = ActionChains(driver)

	driver.get(like_url)

	login_button = driver.find_element(By.XPATH, '/html/body/header/div/nav/ul/li[3]/a')
	login_button.click()

	username = driver.find_element(By.XPATH, '//*[@id="username"]')
	password = driver.find_element(By.XPATH, '//*[@id="password"]')

	username.clear()
	password.clear()

	username.send_keys(like_username)
	password.send_keys(like_password)
	password.send_keys(Keys.RETURN)

	try:
		earn_credits_button = driver.find_element(By.XPATH, '/html/body/header/div/nav/ul/li[2]/a')
		earn_credits_button.click()
		print("login successful")
	except:
		print("could not login. exiting...")
		exit(1)

	while True:

		try:
			twitter_follows()
			insta_follows()
			youtube_likes()
		except KeyboardInterrupt:
			exit(1)
		except:
			driver.quit()
			raise

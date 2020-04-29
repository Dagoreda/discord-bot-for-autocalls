import os
from selenium import webdriver
import asyncio

counter = 0
browser = webdriver.Chrome()
async def make_a_call():
	make_a_call = browser.find_element_by_css_selector("[aria-label='Start Voice Call']")
	make_a_call.click()

async def stop_a_call():
	stop_a_call = browser.find_element_by_css_selector("[aria-label='Disconnect']")
	stop_a_call.click()

async def botstart():
	global counter
	if counter == 0:
		clear = lambda: os.system('cls')
		clear()
		print("Choose a user and whenever you are ready type anything.")
		answer = input()
		clear()
		print("Ok, let's work!")
		counter = 1
	else:
		await asyncio.sleep(1)
		await make_a_call()
		await asyncio.sleep(25)
		await stop_a_call()
async def main():
	browser.get("http://discordapp.com/login")

	email = browser.find_element_by_name("email")
	password = browser.find_element_by_name("password")
	button = browser.find_elements_by_tag_name('button')

	email.send_keys("email")
	password.send_keys("password")
	button[1].click()
	while True:
		await botstart()
	
loop  =  asyncio.get_event_loop() 
loop.run_until_complete(main ())


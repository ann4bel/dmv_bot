from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import requests

options = Options()
options.add_argument('--headless')
driver = webdriver.Chrome(r"path_to_chromedriver.exe", options=options)
# discord bot token
token = "discord_bot_token_here"
headers = {'Authorization': 'Bot '+ token,
           'Content-Type': 'application/json'}

def scrape(url, place):
    driver.get(url)
    time.sleep(0.5)
    dates = driver.find_elements_by_xpath("//div[contains(@class, 'no-dates-available')]")
    dates_list = []
    for p in range(len(dates)):
        dates_list.append(dates[p].text)
    if len(dates_list) == 0:
         send_message("Go make an appt at " + place + " ASAP")

def send_message(message):
    postdata = '{ "content": "' + message + '" }'
    requests.post('discord_url_for_messages', headers=headers, data=postdata)

urls = {}
//insert the urls of different appointment locations here
urls["abingdon"] = "https://vadmvappointments.as.me/schedule.php?calendarID=5776807"
urls["alexandria"] = "https://vadmvappointments.as.me/schedule.php?calendarID=5776710"
urls["altavista"] = "https://vadmvappointments.as.me/schedule.php?calendarID=4150919"

while True:
    for place in urls:
        scrape(urls[place], place)
    time.sleep(45)
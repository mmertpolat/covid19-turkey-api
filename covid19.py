from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from datetime import date
import time
import os
import json
import telebot

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
t = webdriver.Chrome('chromedriver', options=chrome_options)
t.get("https://covid19.saglik.gov.tr/")
time.sleep(1)
t.maximize_window()
today = date.today()
tarih = today.strftime("%d/%m/%Y")
buguntest = t.find_element_by_css_selector("section#post-data-harita div.vaka_box_1 > div > div.col-lg-8 > b").text
bugunvaka = t.find_element_by_css_selector("section#post-data-harita div.vaka_box_2 > div > div.col-lg-8 > b").text
bugunvefat = t.find_element_by_css_selector("section#post-data-harita div.vaka_box_3 > div > div.col-lg-8 > b").text
buguniyilesen = t.find_element_by_css_selector("section#post-data-harita div.vaka_box_4 > div > div.col-lg-8 > b").text

rapor = "Tarih: " + tarih + "\n" + "Bugün Yapılan Test: " + buguntest + "\n" + "Bugün Vaka: " + bugunvaka + "\n" + "Bugün Vefat: " + bugunvefat + "\n" + "Bugün İyileşen: " + buguniyilesen
print(rapor)

data = {}
data['rapor'] = []
data['rapor'].append({
    'tarih': tarih,
    'buguntest': buguntest,
    'bugunvaka': bugunvaka,
    'bugunvefat': bugunvefat,
    'buguniyilesen': buguniyilesen
})

with open('daily.json', 'w') as outfile:
    json.dump(data, outfile)
t.close()

telesecret = os.environ.get("TELEGRAM_TOKEN")
chatid = os.environ.get("CHAT_ID")

tb = telebot.TeleBot(telesecret, parse_mode=None)
tb.send_message(chatid, rapor)

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
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
tarih = t.find_element_by_css_selector("section#vaka_sayilari_home h3").text
buguntest = t.find_element_by_css_selector("section#vaka_sayilari_home div:nth-child(2) > div:nth-child(2) > div > p").text
bugunvaka = t.find_element_by_css_selector("section#vaka_sayilari_home div:nth-child(2) > div:nth-child(3) > div > p").text
bugunhasta = t.find_element_by_css_selector("section#vaka_sayilari_home div:nth-child(2) > div:nth-child(4) > div > p").text
bugunvefat = t.find_element_by_css_selector("section#vaka_sayilari_home div:nth-child(2) > div:nth-child(5) > div > p").text
buguniyilesen = t.find_element_by_css_selector("section#vaka_sayilari_home div:nth-child(2) > div:nth-child(6) > div > p").text
toplamtest = t.find_element_by_css_selector("section#vaka_sayilari_home div:nth-child(4) > div:nth-child(2) > div > p").text
toplamvaka = t.find_element_by_css_selector("section#vaka_sayilari_home div:nth-child(4) > div:nth-child(3) > div > p").text
toplamvefat = t.find_element_by_css_selector("section#vaka_sayilari_home div:nth-child(4) > div:nth-child(4) > div > p").text
toplamagirhasta = t.find_element_by_css_selector("section#vaka_sayilari_home div:nth-child(4) > div:nth-child(5) > div > p").text
toplamiyilesen = t.find_element_by_css_selector("section#vaka_sayilari_home div:nth-child(4) > div:nth-child(6) > div > p").text

rapor = "Tarih: " + tarih + "\n" + "Bugün Yapılan Test: " + buguntest + "\n" + "Bugün Vaka: " + bugunvaka + "\n" + "Bugün Hasta: " + bugunhasta + "\n" + "Bugün Vefat: " + bugunvefat + "\n" + "Bugün İyileşen: " + buguniyilesen + "\n" + "Toplam Test: " + toplamtest + "\n" + "Toplam Vaka: " + toplamvaka + "\n" + "Toplam Vefat: " + toplamvefat + "\n" + "Toplam Ağır Hasta: " + toplamagirhasta + "\n" + "Toplam İyileşen: " + toplamiyilesen
print(rapor)

data = {}
data['rapor'] = []
data['rapor'].append({
    'tarih': tarih,
    'buguntest': buguntest,
    'bugunvaka': bugunvaka,
    'bugunhasta': bugunhasta,
    'bugunvefat': bugunvefat,
    'buguniyilesen': buguniyilesen,
    'toplamtest': toplamtest,
    'toplamvaka': toplamvaka,
    'toplamvefat': toplamvefat,
    'toplamagirhasta': toplamagirhasta,
    'toplamiyilesen': toplamiyilesen
})

with open('dataset/daily.txt', 'w') as outfile:
    json.dump(data, outfile)
t.close()

telesecret = os.environ.get("TELEGRAM_TOKEN")
chatid = os.environ.get("CHAT_ID")

tb = telebot.TeleBot(telesecret, parse_mode=None)
tb.send_message(chatid, rapor)

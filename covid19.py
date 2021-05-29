from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import json

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

print(tarih + "\n" + buguntest + "\n" + bugunvaka + "\n" + bugunhasta + "\n" + bugunvefat + "\n" + buguniyilesen + "\n" + toplamtest + "\n" + toplamvaka + "\n" + toplamvefat + "\n" + toplamagirhasta + "\n" + toplamiyilesen)

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

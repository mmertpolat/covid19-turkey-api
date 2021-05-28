from selenium import webdriver
import time
import json

chromedriver = "E:/chromedriver" # change with your chromedriver url
tarayici = webdriver.Chrome(chromedriver)
tarayici.get("https://covid19.saglik.gov.tr/")
time.sleep(1)
tarayici.maximize_window()
tarih = tarayici.find_element_by_css_selector("section#vaka_sayilari_home h3").text
buguntest = tarayici.find_element_by_css_selector("section#vaka_sayilari_home div:nth-child(2) > div:nth-child(2) > div > p").text
bugunvaka = tarayici.find_element_by_css_selector("section#vaka_sayilari_home div:nth-child(2) > div:nth-child(3) > div > p").text
bugunhasta = tarayici.find_element_by_css_selector("section#vaka_sayilari_home div:nth-child(2) > div:nth-child(4) > div > p").text
bugunvefat = tarayici.find_element_by_css_selector("section#vaka_sayilari_home div:nth-child(2) > div:nth-child(5) > div > p").text
buguniyilesen = tarayici.find_element_by_css_selector("section#vaka_sayilari_home div:nth-child(2) > div:nth-child(6) > div > p").text
toplamtest = tarayici.find_element_by_css_selector("section#vaka_sayilari_home div:nth-child(4) > div:nth-child(2) > div > p").text
toplamvaka = tarayici.find_element_by_css_selector("section#vaka_sayilari_home div:nth-child(4) > div:nth-child(3) > div > p").text
toplamvefat = tarayici.find_element_by_css_selector("section#vaka_sayilari_home div:nth-child(4) > div:nth-child(4) > div > p").text
toplamagirhasta = tarayici.find_element_by_css_selector("section#vaka_sayilari_home div:nth-child(4) > div:nth-child(5) > div > p").text
toplamiyilesen = tarayici.find_element_by_css_selector("section#vaka_sayilari_home div:nth-child(4) > div:nth-child(6) > div > p").text

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

with open('covid19.txt', 'w') as outfile:
    json.dump(data, outfile)

tarayici.close()
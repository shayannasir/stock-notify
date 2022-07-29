from urllib import response
import requests
import json
from bs4 import BeautifulSoup
import telegram_send;

url = "https://keychron.in/product/keychron-k2-v-2/"
headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
}
f = requests.get(url, headers = headers)
soup = BeautifulSoup(f.content, 'html5lib')
data = soup.find('form', attrs = {'class':'variations_form'}) 
dict = json.loads(data.attrs['data-product_variations'])
responseList = []
for item in dict:
    attr_dict = item['attributes'];
    model_color = attr_dict['attribute_pa_switch-option']
    model_backlight = attr_dict['attribute_pa_version']
    if (model_backlight == "white-backlight"):
      if (model_color == "blue-switch" or model_color == "brown-switch"):
          model_availability = "Available" if "In Stock" in item['availability_html'] else "UNAVAILABLE"
          model_price = item['display_price']
          responseMessage = model_color + " | " + model_backlight + " is " + model_availability + " at " + str(model_price)
          responseList.append(responseMessage)
responseList.append("<------------------------------->")
telegram_send.send(messages=responseList)

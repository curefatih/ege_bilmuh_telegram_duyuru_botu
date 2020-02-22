import requests
from bs4 import BeautifulSoup
response = requests.get("https://bilmuh.ege.edu.tr/")
soup = BeautifulSoup(response.text, "lxml")
duyurular = soup.select('a[class^=hbrstyl]')
for i in range(len(duyurular)):
    duyurular[i] = duyurular[i].text
duyuru = duyurular[0]+" duyurusu yayınlanmıştır. Ayrıntısını görmek için https://bilmuh.ege.edu.tr/ adresine bakınız."
token = "" #buraya telegramdan aldığınız kendi tokeninizi yazacaksınız.
chat_id = "" #buraya token kullanarak bulduğunuz chat_idyi yazacaksınız.
requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id': chat_id, 'text': duyuru}).json()



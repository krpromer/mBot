import ConfigParser
import subprocess
import requests
import json
import time

TOKEN = "439659276:AAFoPRUbHjsLOmEtN5aDieR1HjU_VojBmUY"
CHAT_ID = "64750298"
POLO_URL = "http://poloniex.com/public?command=returnTicker"
BOT_URL = "https://api.telegram.org/bot{}/".format(TOKEN)

BTC_LTC = 0
PRICE = 0

def get_url(url):
    response = requests.get(url)
    content = response.content.decode("utf8")
    return content

def send_message(text, chat_id):
    url = BOT_URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
    get_url(url)

p = subprocess.Popen('git pull', shell = True, stdout = subprocess.PIPE, stderr = subprocess.STDOUT)

mConfig = ConfigParser.ConfigParser()
mConfig.read('config.ini')
print 'Version', mConfig.getint('INFO', 'version')
BTC_LTC = mConfig.getint('COIN', 'BTC_LTC')

coinInfo = json.loads(get_url(POLO_URL))

if BTC_LTC == 1:
    #print 'BTC_LTC :', coinInfo['BTC_LTC']['last']
    PRICE = float(coinInfo['BTC_LTC']['last'])

for idx in range(1, 10000):
    send_message(PRICE, CHAT_ID)
    time.sleep(10)


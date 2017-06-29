import ConfigParser
import subprocess
import requests
import json
import time

TOKEN = "439659276:AAFoPRUbHjsLOmEtN5aDieR1HjU_VojBmUY"
CHAT_ID = "64750298"
POLONIEX_URL = "http://poloniex.com/public?command=returnTicker"
BITTREX_URL = "https://bittrex.com/api/v1.1/public/getticker?market=bt"
BOT_URL = "https://api.telegram.org/bot{}/".format(TOKEN)

BTC_LTC = 0
BTC_WAVES = 0
PRICE_LTC = 0.000000001
PRICE_WAVES = 0.000000001
TEMP = 0.000000001
run = 1

def get_url(url):
    response = requests.get(url)
    content = response.content.decode("utf8")
    return content

def send_message(text, chat_id):
    url = BOT_URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
    get_url(url)

def diff(a, b):
	if a > b:
		return a/b
	else:
		return b/a

while run:
	p = subprocess.Popen('git pull', shell = True, stdout = subprocess.PIPE, stderr = subprocess.STDOUT)

	mConfig = ConfigParser.ConfigParser()
	mConfig.read('config.ini')
#print 'Version', mConfig.getint('INFO', 'version')
	BTC_LTC = mConfig.getint('COIN', 'BTC_LTC')
	BTC_WAVES = mConfig.getint('COIN', 'BTC_WAVES')
	run = mConfig.getint('INFO', 'run')
	coinInfo = json.loads(get_url(POLONIEX_URL))

	if BTC_LTC == 1:
		#print 'BTC_LTC :', coinInfo['BTC_LTC']['last']
		TEMP = float(coinInfo['BTC_LTC']['last'])
		CH = diff(PRICE_LTC, TEMP)
		if CH > 1.05:
			PRICE_LTC = TEMP
			send_message('LTC', CHAT_ID)
			send_message(PRICE_LTC, CHAT_ID)

	time.sleep(30)


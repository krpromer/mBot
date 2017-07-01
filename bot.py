import ConfigParser
import subprocess
import requests
import json
import time

TOKEN = "439659276:AAFoPRUbHjsLOmEtN5aDieR1HjU_VojBmUY"
CHAT_ID = "64750298"
POLONIEX_URL = "http://poloniex.com/public?command=returnTicker"
BITTREX_URL = "https://bittrex.com/api/v1.1/public/getticker?market=btc-waves"
LIQUI_URL = "https://api.liqui.io/api/3/ticker/snm_btc"

BOT_URL = "https://api.telegram.org/bot{}/".format(TOKEN)

BTC_LTC = 0
BTC_WAVES = 0
BTC_SNM = 0
PRICE_LTC = 0.00000001
PRICE_WAVES = 0.00000001
PRICE_SNM = 0.00000001
TEMP = 0.00000001
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
	BTC_SNM = mConfig.getint('COIN', 'BTC_SNM')
	run = mConfig.getint('INFO', 'run')

	if BTC_LTC == 1:
		PRICE_LTC =  mConfig.getfloat('PRICE', 'BTC_LTC')
		content = get_url(POLONIEX_URL)
		if content == "":
			print 'POLO ERROR'
		else:
			coinInfo = json.loads(content)
			TEMP = float(coinInfo['BTC_LTC']['last'])
			CH = diff(PRICE_LTC, TEMP)
			print 'price=',PRICE_LTC,' now=',TEMP,' debug ltc = ', CH
			if CH > 1.05:
				mConfig.set('PRICE','BTC_LTC',TEMP)
				MSG = "LTC =", TEMP
				send_message(MSG, CHAT_ID)

	if BTC_WAVES == 1:
		PRICE_WAVES =  mConfig.getfloat('PRICE', 'BTC_WAVES')
		content = get_url(BITTREX_URL)
		if content == "":
			print 'BITTREX ERROR'
		else:
			coinInfo = json.loads(content)
			TEMP = float(coinInfo['result']['Last'])
			CH = diff(PRICE_WAVES, TEMP)
			print 'price=',PRICE_WAVES,' now=',TEMP,' debug waves = ', CH
			if CH > 1.05:
				mConfig.set('PRICE','BTC_WAVES',TEMP)
				MSG = "WAVES =", TEMP
				send_message(MSG, CHAT_ID)

	if BTC_SNM == 1:
		PRICE_SNM =  mConfig.getfloat('PRICE', 'BTC_SNM')
		content = get_url(LIQUI_URL)
		if content == "":
			print 'LIQUI ERRROR'
		else:
			coinInfo = json.loads(content)
			TEMP = float(coinInfo['snm_btc']['last'])
			CH = diff(PRICE_SNM, TEMP)
			print 'price=',"{0:.8f}".format(PRICE_SNM),' now=',"{0:.8f}".format(TEMP),' debug snm = ',"{0:.8f}".format(CH)
			if CH > 1.05:
				mConfig.set('PRICE','BTC_SNM',TEMP)
				MSG = "SNM =", "{0:.8f}".format(TEMP)
				send_message(MSG, CHAT_ID)
	
	mConfigFile = open('config.ini', 'w')
	mConfig.write(mConfigFile)
	mConfigFile.close()
	print time.strftime("%y/%m/%d %H:%M:%S", time.localtime())
	time.sleep(30)


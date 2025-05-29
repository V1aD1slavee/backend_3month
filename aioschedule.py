import schedule
import time
import requests

def test():
    print("Hello world")
    print(time.ctime())

def get_btc_price():
    print("======BTC======")
    url = "https://api.binance.com/api/v3/avgPrice?symbol=BTCUSDT"
    response = requests.get(url=url).json()
    print(response)

# schedule.every(2).seconds.do(test)
# schedule.every(1).minutes.do(test)
# schedule.every().day.at('12:58').do(test)
# schedule.every().thursday.at('14:56').do(test)
# schedule.every().day.at('19:30', 'Europe/Moscow').do(test)
# schedule.every().hour.at(':25').do(test)

while True:
    schedule.run_pending()

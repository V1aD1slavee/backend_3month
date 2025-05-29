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
    # print(response)
    price = response.get('price')

    print(f"Стоимость биткоина {price}, {time.ctime()}")

# get_btc_price()
# schedule.every(2).seconds.do(test)
# schedule.every(1).minutes.do(test)
# schedule.every().day.at('12:58').do(test)
# schedule.every().thursday.at('14:56').do(test)
# schedule.every().day.at('19:30', 'Europe/Moscow').do(test)
# schedule.every().hour.at(':25').do(test)
schedule.every(2).seconds.do(get_btc_price)

while True:
    schedule.run_pending()

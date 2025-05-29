import schedule
import time

def test():
    print("Hello world")
    print(time.ctime())

# schedule.every(2).seconds.do(test)
# schedule.every(1).minutes.do(test)
# schedule.every().day.at('12:58').do(test)
# schedule.every().thursday.at('14:56').do(test)
# schedule.every().day.at('19:30', 'Europe/Moscow').do(test)
# schedule.every().hour.at(':25').do(test)

while True:
    schedule.run_pending()

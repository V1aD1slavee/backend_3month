import schedule
import time

def test():
    print("Hello world")
    print(time.ctime())

# schedule.every(2).seconds.do(test)
# schedule.every(1).minutes.do(test)
# schedule.every().day.at('12:58').do(test)

while True:
    schedule.run_pending()
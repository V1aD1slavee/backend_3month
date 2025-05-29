import schedule
import time

def test():
    print("Hello world")
    print(time.ctime())

schedule.every(2).seconds.do(test)

while True:
    schedule.run_pending()
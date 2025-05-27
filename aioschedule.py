import schedule
import time

def test():
    print("Hello world")
    print(time.ctime())

schedule.every(2).seconds

while True:
    schedule.run_pending()
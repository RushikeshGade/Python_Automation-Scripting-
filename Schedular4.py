import datetime 
import time
import schedule

def Schedule_Minute():
    print("Schedular executes after each munut :",datetime.datetime.now())

def main():
    print(datetime.datetime.now())

    
    schedule.every(1).minutes.do(Schedule_Minute)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__=="__main__":
    main()    
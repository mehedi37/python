import time

def time_format(mins):
    if(int(mins) > 9):
            return mins
    else:
        mins = f"0{mins}"
        return mins

def count_down(sec):
    while sec:
        mins, secs = divmod(sec, 60)
        print(f"{time_format(mins)}:{time_format(secs)}", end="\r")
        time.sleep(1)
        sec -= 1
    print("Timer Ended !")
count_down(10)

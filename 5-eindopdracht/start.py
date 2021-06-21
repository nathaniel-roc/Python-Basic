import time


def lten(x):
    if x < 10:
        return "0" + str(x)
    else:
        return x


seconds = time.time()


hour = 00
minutes = 00

while True:
    time.sleep(1)
    now = round(time.time() - seconds)
    if minutes == 60 and seconds == 60:
        minutes += 1
        seconds = time.time()
        print(str(lten(hour)) + ":" + str(lten(minutes)) + ":" + str(lten(0)))
    else:
        if now == 60:
            seconds = time.time()
            minutes += 1
            print(str(lten(hour)) + ":" + str(lten(minutes)) + ":" + str(lten(0)))
        else:
            print(str(lten(hour)) + ":" +
                  str(lten(minutes)) + ":" + str(lten(now)))

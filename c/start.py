import random
import time

seconds = time.time()
number = 0
running = True

while running:
    now = round(time.time() - seconds)
    if now < 60:
        number += 1
        print(str(random.randint(0, 9999999999999999999) * random.randint(0, 9999999999999999999) / random.randint(0, 9999999999999999999) +
                  random.randint(0, 9999999999999999999) - random.randint(0, 9999999999999999999) * random.randint(0, 9999999999999999999) * random.randint(0, 9999999999999999999) * random.randint(0, 9999999999999999999) / random.randint(0, 9999999999999999999) +
                  random.randint(0, 9999999999999999999) - random.randint(0, 9999999999999999999) * random.randint(0, 9999999999999999999) / random.randint(0, 9999999999999999999) * random.randint(0, 9999999999999999999) / random.randint(0, 9999999999999999999) +
                  random.randint(0, 9999999999999999999) - random.randint(0, 9999999999999999999) * random.randint(0, 9999999999999999999) + random.randint(0, 9999999999999999999) * random.randint(0, 9999999999999999999) / random.randint(0, 9999999999999999999) +
                  random.randint(0, 9999999999999999999) - random.randint(0, 9999999999999999999) * random.randint(0, 9999999999999999999) * random.randint(0, 9999999999999999999) * random.randint(0, 9999999999999999999) / random.randint(0, 9999999999999999999) +
                  random.randint(0, 9999999999999999999) - random.randint(0, 9999999999999999999) * random.randint(0, 9999999999999999999) * random.randint(0, 9999999999999999999) * random.randint(0, 9999999999999999999) / random.randint(0, 9999999999999999999) +
                  random.randint(0, 9999999999999999999) - random.randint(0, 9999999999999999999) * random.randint(0, 9999999999999999999)))
    else:
        print("Calculation amount: " + str(number))
        running = False

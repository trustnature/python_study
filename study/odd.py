from datetime import datetime

import random
import time

odds = [1, 3, 5, 7, 9,
        11, 13, 15, 17, 19]

for i in range(5):
    right_this_minute = datetime.today().minute

    if right_this_minute in odds:
        print("This minute sees a little odd.")
    else:
        print("Not an odd minute.")
    wait_time = random.randint(1, 60)
    time.sleep(wait_time)

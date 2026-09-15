# Explonetial Backoff
#Pro: Implement an exponential backoff strategy that doubles the wait time betwee retries, starting from 1 second, but stops after 5 retries

import time

retries = 0
wait_time = 1

while retries < 5:
    print("Trying...")

    success = False   # simulate failure (change to True to stop early)

    if success:
        print("Success!")
        break
    else:
        print("Failed. Waiting", wait_time, "seconds...")
        time.sleep(wait_time)

        wait_time = wait_time * 2
        retries += 1

else:
    print("Stopped after 5 retries")
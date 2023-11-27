# your code goes here!
import time

def countdown_with_sleep(seconds):
    i = seconds
    while i > 0:
        print(f"{i} SECOND(S)!")
        time.sleep(1)
        i -= 1
    print("HAPPY NEW YEAR!")


countdown_with_sleep(5)

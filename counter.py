// counter python back end
import time

def simple_timer(seconds):
    print(f"Timer started for {seconds} seconds.")
    time.sleep(seconds)
    print("Time's up!")

#Set a timer for 5 seconds
simple_timer(5.5)

# Tatsuo Miyajima - 'Time Waterfall' displayed in the British Museum
import random, time

# prints random numbers between 1 and 9 across the terminal
def time_waterfall():
    for _ in range(200):
        time.sleep(0.2)
        random_number = str(random.randint(1, 9))
        print(random_number, end = '\r', flush=True) 
        # \r replaces the previous random number with the new one

#time_waterfall()

# uses the iterable produced by range to countdown
def countdown():
    for num in range(9, 0, -1):
        time.sleep(1)
        print(num, end = '\r', flush=True)

#countdown()

# marches across the screen and prints the numbers like cascading water
def countdown_repeat():
    space = 0
    for _ in range(50):
        space +=1
        whitespace = space * ' '
        start = random.randint(1, 9)
        for num in range(start, 0, -1):
            time.sleep(0.75)
            print(whitespace, num, end = '\n', flush=True)
        
            #print(whitespace, end = '')

countdown_repeat()

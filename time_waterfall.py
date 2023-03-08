# Tatsuo Miyajima - 'Time Waterfall' displayed in the British Museum
import random, time

# prints random numbers between 1 and 9 across the terminal
def time_waterfall():
    for _ in range(175):
        time.sleep(0.1)
        random_number = str(random.randint(1, 9))
        print(random_number, end = '', flush=True) 

time_waterfall()
print()
print()

# uses the iterable produced by range to countdown
def countdown():
    for num in range(9, 0, -1):
        time.sleep(1.5)
        print(num, end = '\r', flush=True)
        # \r replaces the previous random number with the new one

countdown()
print()

# marches across the screen and prints the numbers like cascading water
def countdown_repeat():
    space = 0
    for _ in range(200):
        space +=1
        whitespace = space * ' '
        start = random.randint(1, 9)
        for num in range(start, 0, -1):
            time.sleep(0.75)
            print(whitespace, num, end = '\n', flush=True)
        
            #print(whitespace, end = '')

countdown_repeat()

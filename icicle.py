import random, time

def icicle(word):
    rand_num = random.randint(1, 100)
    screen_area = rand_num * ' '
    length = len(word)
    whitespace = (length-2) * ' '
    letter = []
    letter += word
    num_ord = ord(letter[-1])
    count = num_ord
    print(screen_area, word)
    while count < 122:
        num_ord += 1
        count += 1
        time.sleep(0.1)
        print(screen_area, whitespace, chr(num_ord))

icy_words = ["icicle", "cold", "freeze", "melt", "freezing", "melting", "skate", "frozen"]
word = random.choice(icy_words)
icicle(word)

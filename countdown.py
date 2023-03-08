# uses the iterable produced by range to countdown
def countdown():
    for num in range(9, 0, -1):
        time.sleep(1.5)
        print(num, end = '\r', flush=True)
        # \r replaces the previous random number with the new one

countdown()

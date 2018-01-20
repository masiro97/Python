import time
def countdown(n):
    if n>0:
        print(n)
        time.sleep(1)
        countdown(n-1)
    else:
        print('발사!')

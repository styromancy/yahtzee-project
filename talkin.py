import time
def sleep(s):
  time.sleep(s)
def talk(str):
  for char in str:
    pause = .01
    if char == ',':
      pause = .2
    elif char == '.':
      pause = .1
    elif char == '!' or char == '-':
      pause = .25
    elif char == '?':
      pause = .2
    print(char, end = '')
    sleep(pause)

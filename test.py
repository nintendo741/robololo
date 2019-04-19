import sys
from Utils import DBConnector as DB
DB.DBConnect()
from Bot.Integrations import MovingPlantform as MP
from Bot.Integrations import SendingComand as SC
#import Tests.CheckDevices as CD
#import time
#import config as CF
if sys.platform[:3] == 'win':
  import msvcrt
  def getkey():
    key = msvcrt.getch()
    return key
elif sys.platform[:3] == 'lin':
  import termios, sys, os
  TERMIOS = termios

  def getkey():
    fd = sys.stdin.fileno()
    old = termios.tcgetattr(fd)
    new = termios.tcgetattr(fd)
    new[3] = new[3] & ~TERMIOS.ICANON & ~TERMIOS.ECHO
    new[6][TERMIOS.VMIN] = 1
    new[6][TERMIOS.VTIME] = 0
    termios.tcsetattr(fd, TERMIOS.TCSANOW, new)
    c = None
    try:
      c = os.read(fd, 1)
    finally:
      termios.tcsetattr(fd, TERMIOS.TCSAFLUSH, old)
    return c



Speed=int(input('enter speed'))
Turn=int(input('enter turn(1/1000)'))
while True:
  print(SC.ReadComand('Moving'))
  pressedKey = getkey().decode("utf-8")
  if pressedKey == 'y':
    sys.exit()
  elif pressedKey == 'w':
    MP.ForwardMoving(Speed,Turn)
  elif pressedKey == 'a':
    MP.LeftMoving(Speed,Turn)
  elif pressedKey == 's':
    MP.BackMoving(Speed,Turn)
  elif pressedKey == 'd':
    MP.RightMoving(Speed,Turn)
  elif pressedKey == 'q':
    MP.ForwardLeftMoving(Speed,Turn)
  elif pressedKey == 'e':
    MP.ForwardRightMoving(Speed,Turn)
  elif pressedKey == 'z':
    MP.BackLeftMoving(Speed,Turn)
  elif pressedKey == 'c':
    MP.BackRightMoving(Speed,Turn)
  elif pressedKey == 'f':
    MP.TurnLeftMoving(Speed,Turn)
  elif pressedKey == 'g':
    MP.TurnRightMoving(Speed,Turn)
  elif pressedKey == 'r':
    Speed=int(input('enter speed'))
    Turn=int(input('enter turn(1/1000)'))
  else:
    print("Key:" + pressedKey)
    print('press y to exit or r to change parametrs')

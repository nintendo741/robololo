import msvcrt, sys
import Bot.Integrations.MovingPlantform as MP
Speed=int(input('enter speed'))
Turn=int(input('enter turn(1/1000)'))
while True:
  pressedKey = msvcrt.getch()
  pressedKey=pressedKey.decode("utf-8")
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

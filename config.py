#TimeStartMov = 2
#TimeActivateExperiment = 4
#TimeCollectAtoms = 6
#TimeDropOnLibra = 8
#TimeDropOnFields = 10
Actions = ["Start moving", "Activate experiment", "Atom collect", "Drop on libra", "Drop on field"]
ActionsTime = [2, 4, 6, 8, 10]
# 0 - no print, 1 - print before every func
Debug = 0
Step = 100
Devices = [['MovingArduino', 'usb-1a86_USB2.0-Serial']]#,['SortedArduino', '756303134363511072A0']]
ArduinoComands = ['F', 'B', 'R', 'L', 'TR', 'TL', 'FR', 'FL', 'BR', 'BL']
GPIOPins = [5,6,13,19,26]
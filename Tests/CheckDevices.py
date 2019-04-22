#check ACM
import subprocess
#import serial
from config import Debug as D
#import Utils.DBConnector as DB

# 756303134363511072A0 - full Arduino Serial Number
# 75630
# /dev/serial/by-id
# /dev/serial/by-path


def DevicePath(id):
	#print(id)
	port = subprocess.check_output("""ls -la /dev/serial/by-id/ | grep %s | awk '{print($11)}' | sed 's/..\/..\///g'"""%(id), shell=True)
	path = "/dev/" + port[:-1].decode()
	#print(path)
	if D > 0:
		print("id:" + str(id) + "path:" + str(path))
	return path


#check ACM
import subprocess

# 756303134363511072A0 - full Arduino Serial Number
# 75630
# /dev/serial/by-id
# /dev/serial/by-path

def DevicePath(id):
    port = subprocess.check_output("""ls -la /dev/serial/by-id/ | grep %s | awk '{print($11)}' | sed 's/..\/..\///g'"""%(id), shell=True)
    path = "/dev/" + str(port)
    return path

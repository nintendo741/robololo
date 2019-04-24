import socket
import json
from Utils import DBConnector as DB
def PrepareData (data,FrameId):
    for i in range(len(data[0])):

        DB.JsonWrite(FrameId,data[0][i],data[1][i],data[2][i],data[3][i],data[4][i],data[5][i])
DB.DBConnect() #убрать потом это говно
FrameId=0
sock = socket.socket()
sock.bind(('', 9090))
sock.listen(1)
conn, addr = sock.accept()

print ('connected:', addr)
try:
    while True:
        data=None
        while True:
            data = conn.recv(2048)
            if not data:
                break

            data=data.decode()
            data=data.split("|")


            if data[0]!='Nothing':
                for i in range(len(data)-1):
                    frameData=json.loads(data[i])
                    FrameId+=1
                    PrepareData(frameData,FrameId)
            else:
                FrameId+=1
                DB.JsonWrite(FrameId,0,0,0,0,0,0)

except KeyboardInterrupt:
    conn.close()


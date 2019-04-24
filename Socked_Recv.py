import socket
import json
from Utils import DBConnector as DB
def PrepareData (data,FrameId):
    for i in range(len(data[0])):
        for j in range(6):
            print(data[j][i],end=" ")
        print()
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
            print(data)
            FrameId+=1
            data=data.decode()
            if data!='Nothing':
                data=json.loads(data)
                print(data)
                PrepareData(data,FrameId)
            else:
                DB.JsonWrite(FrameId,0,0,0,0,0,0)
except KeyboardInterrupt:
    conn.close()


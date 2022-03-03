import SerialModule
import time

def initConnection(portNo, baudRate):
    try:
        ser = SerialModule.SerialModule(portNo,baudRate)
        print("Device COnnect")
        return ser
    except:
        print("Not Connected")

def sendData(se, data, digits):
    myString = "$"
    for d in data:
        myString += str(d).zfill(digits)
    try:
        se.write(myString.encode())
        print(myString)
    except:
        print("Data Transmission Failed")

if __name__ == "__main__":
    ser = initConnection("/dev/ttyACM0", 9600)
    while True:
        sendData(ser, [0,255],3)
        time.sleep(1)
        sendData(ser, [0,0],3)
        time.sleep(1)
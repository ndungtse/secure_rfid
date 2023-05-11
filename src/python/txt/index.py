#!/usr/bin/env python3
from serial import Serial, PARITY_NONE, STOPBITS_ONE, EIGHTBITS

ser = Serial(
    # windows USB 
        port='COM11',  # plz change this according to your port number
        baudrate=9600,
        parity= PARITY_NONE,
        stopbits= STOPBITS_ONE,
        bytesize= EIGHTBITS,
        timeout=1
)

ser.flush()

def readFile(uuid):
    print(f"[py:log] Checking for UUID: |{uuid}|")
    with open("./tags.txt", "r") as f:
        for line in f.readlines():
            if line.rstrip().lstrip() == uuid:
                return True
        
    return False
            
    


if __name__ == '__main__':
    while True:
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').rstrip()
            print(line)
            if line[0:14] == "[check-access]":
                print("Checking Access")
                isAllowed = readFile(line[14:].rstrip().lstrip())
                response = "granted" if isAllowed else "denied"
                ser.write(response.encode())
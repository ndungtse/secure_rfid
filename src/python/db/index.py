#!/usr/bin/env python3
import serial
import mysql.connector
from playsound import playsound

# Connect to the MySQL database
db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="chazard10.3",
  database="secure_rfid"
)
    
ser = serial.Serial(
    port="COM11",  # plz change this according to your port number
    baudrate=9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1,
)

ser.flush()

 # create db cursor
cursor = db.cursor()
def create_card_table():
    create_table = """CREATE TABLE IF NOT EXISTS CARD_FORMAT(
        ID INTEGER PRIMARY KEY AUTO_INCREMENT,
        UUID VARCHAR(400) NOT NULL
    )"""

    # execute the query
    cursor.execute(create_table)
    
def insert_into_db(card: str):
    sql = "INSERT INTO card_format (UUID) VALUES (%s)"
    values = (card,)
    cursor.execute(sql, values)
    db.commit()
    print("INSERTED 😲😲😲😲")


def readFile(uuid):
    print(f"[py:log] Checking for UUID: |{uuid}|")
    dict = {"UUID": uuid}
    cursor.execute("SELECT * FROM CARD_FORMAT WHERE UUID = %(UUID)s", dict)
    rows = cursor.fetchall()
    if len(rows) == 0:
        print(f"[py:log] UUID not found: {uuid}")
        return False
    else:
        print(f"[py:log] UUID found: {uuid}")
        return True
    

if __name__ == "__main__":
    create_card_table()
    # insert_into_db("BA 0D D0 43")
    # exit(0)
    while True:
        if ser.in_waiting > 0:
            line = ser.readline().decode("utf-8").rstrip()
            print(line)
            if line[0:14] == "[check-access]":
                print("Checking Access")
                isAllowed = readFile(line[14:].rstrip().lstrip())
                response = "granted" if isAllowed else "denied"
                ser.write(response.encode())
                if isAllowed:
                    playsound("../audio/granted.mp3")
                else:
                    playsound("../audio/denied.mp3")
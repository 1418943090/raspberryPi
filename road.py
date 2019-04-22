import os
import paho.mqtt.client as mqtt
import time
import pymysql
import serial
ser=serial.Serial('/dev/ttyUSB0',9600,timeout=0.5)
if(ser.isOpen()==False):
  ser.open()
#**********************************
connecting=pymysql.connect(
        host="localhost",
        user="root",
        password="huang110",
        db="lot",
        charset="utf8"
        )
cur=connecting.cursor()
#*******************************
client=mqtt.Client()
f=open('mqtt.txt')
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
def mqtt_connect():
    client.username_pw_set("adminroad", "password") 
    client.on_connect = on_connect
    host_name = "192.168.137.76"
    client.connect(host_name, 1883, 60)
    client.loop_start()   
def Mqtt_Publish(s):
    client.publish('node_information',s)
#************************************************
def Uart_Send(s):
    global ser
    id=s[3:6]
    order=s[7:]
   # print(id)
   # print(order)
    ser.write('s'.encode())
    time.sleep(0.1)
    for i in id:
    #   print(i)
       i=i.encode()
       ser.write(i)
       time.sleep(0.1)
    if(order=='on'):
    #   print('f')
       ser.write('1'.encode())
       time.sleep(0.1)
    if(order=='off'):
       ser.write('0'.encode())
       time.sleep(0.1)
def Get_Style(ID):
    global cur
    cur.execute("select style from node_information where ID=\'%s\'"%ID)
    data=cur.fetchone()
    style=data[0]
   # print(style)
    return style
#********************************
def addzigbeeequ(zigbeeid):
   
   if(len(zigbeeid)==1):
     zigbeeid="equ00"+zigbeeid
   if(len(zigbeeid)==2):
     zigbeeid="equ0"+zigbeeid
   if(len(zigbeeid)==3):
     zigbeeid="equ"+zigbeeid
   #print(zigbeeid)
   id=zigbeeid[3:6]
   order=zigbeeid[6:7]
   
#********************************
def fun():
  s=f.readline()
  while(s!=""):
    s=f.readline()
  while True:
    # zigbeeid=ser.readline()
    # zigbeeid=zigbeeid.decode()
    # if(zigbeeid!=" <item>黑色</item>"):     
     #   addzigbeeequ(zigbeeid)
    # time.sleep(1)
     s=f.readline()
     if(s!=""):
       s=s.strip('\n')
       print(s)
       ID=s.split(':')[0]
       statsu=s.split(':')[1]
       style=Get_Style(ID)
       if(style=='wifi'):
          Mqtt_Publish(s)
       if(style=='zigbee'):
          Uart_Send(s)
#***************************************
if __name__ == '__main__':
	mqtt_connect()
	fun()
cur.close()
connecting.close()

        

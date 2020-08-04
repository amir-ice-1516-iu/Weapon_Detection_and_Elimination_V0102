#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 06:16:39 2020

@author: rango
"""
import serial
import paho.mqtt.client as mqtt
import json
import time

class Handle_MQTT_and_Serial(object):
    def __init__(self):
        self.serialPort = "/dev/ttyATH0"
        self.serialBaud = 115200
        self.ser = serial.Serial(self.serialPort, self.serialBaud)
        self.ser.flushInput()
        self.stringFromSerial = "!!"
        self.connectedToBroker = False
        self.conf = {"mqHost"    : "10.130.1.1",
                     "mqPort"    : 1883,
                     "device_id" : "Arm0"
                    }
        self.connect_to_broker()
        
    def check_serial_stream(self):
        if(self.ser.inWaiting() > 0):
            self.stringFromSerial = str(self.ser.readline())
            print("Received from MCU "+self.stringFromSerial)
            return True
        else:
            self.stringFromSerial = "!!"
            return False
        
    def on_connect(self,client, userdata, flags, rc):
        #print("Connected to broker")
        print("MQTT Connected")
    
    def on_disconnect(self,client, userdata, rc):
        #print("Disconnected from broker")
        print("MQTT Disconnected")
    
    def connect_to_broker(self):
        self.client = mqtt.Client()
        self.client.on_connect = self.on_connect
        self.client.on_disconnect = self.on_disconnect
        self.client.on_message = self.on_message
        print("Connecting To broker ")
        tried = 0
        while(not self.connectedToBroker and tried<500):
        	try:
        		self.client.connect(self.conf["mqHost"])
        		self.client.loop_start()
        		self.client.subscribe(self.conf["device_id"])
        		self.connectedToBroker = True
        		print("MQTT Connected")
        	except Exception as eConnection:
        		tried += 1
                print(eConnection)
                
    
    def on_message(self,client, userdata, msg):
        MQTT_Massage = json.loads(str(msg.payload))
        Keys = MQTT_Massage.keys()
        if "command" in Keys:
            Command = str(MQTT_Massage["command"])
            self.ser.write(Command.encode("utf-8"))
            waiting_time = time.time()
            while(time.time()-waiting_time<1):
                if self.check_serial_stream():
                    if self.connectedToBroker:
                        self.client.publish(self.conf["device_id"]+"/response",json.dumps({"response":self.stringFromSerial}))
                    break
                time.sleep(0.01)
                
        elif "target" in Keys:
            if str(MQTT_Massage["target"])=="ON":
                if len(str(MQTT_Massage["X"])) == 3 and len(str(MQTT_Massage["Y"])) == 3:    
                    Command = "X"+str(MQTT_Massage["X"])+"Y"+str(MQTT_Massage["Y"])
                    self.ser.write(Command.encode("utf-8"))
                    waiting_time = time.time()
                    while(time.time()-waiting_time<1):
                        if self.check_serial_stream():
                            if self.connectedToBroker:
                                self.client.publish(self.conf["device_id"]+"/response",json.dumps({"response":self.stringFromSerial}))
                                print("Response published")
                                break
                else:
                    print("Invalid Command")
    
    def routine_check(self):
        time.sleep(0.01)
                
    def __del__(self):
        pass

if __name__=='__main__':
    try:
        MidleWare = Handle_MQTT_and_Serial()
        while(True):
            MidleWare.routine_check()
    except Exception as eMainLoop:
        print("terminating")
        MidleWare.client.disconnect()
        print(eMainLoop)
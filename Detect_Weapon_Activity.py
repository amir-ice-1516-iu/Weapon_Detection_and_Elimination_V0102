#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 07:52:59 2020

@author: rango
"""
import threading
import paho.mqtt.publish as publish
import paho.mqtt.subscribe as subscribe
import paho.mqtt.client as mqtt
import socket
import json

class Detect_Weapon_Activity(object):

    def __init__(self,GUI):
        self.GUI = GUI
        self.auto_target_selected = False
        self.auto_fire_selected = False
        self.aimed = False
        self.fired = False
    
    def internet(self,host="8.8.8.8", port=53, timeout=5):
        try:
            socket.setdefaulttimeout(timeout)
            socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
    		#print("Internet available")
            return True
        except socket.error as ex:
            print(ex)
            return False
    
    def on_connect(self,client, userdata, flags, rc):
        print("Connected to broker")
    
    def on_disconnect(self,client, userdata, rc):
        print("Disconnected from broker")
    
    def on_message(self,client, userdata, msg):
        if self.config["debug_mode"]:
            print(msg.topic+" "+str(msg.payload))        
        try:
            self.get_data = json.loads(msg.payload)
            self.messageReceivedFromBroker = True
            self.UART_Serial_Comm.serialReceiveFlag = True
        except:
            self.get_data = {}
    
    def connect_to_broker(self):
        self.client = mqtt.Client()
        self.client.on_connect = self.on_connect
        self.client.on_disconnect = self.on_disconnect
        self.client.on_message = self.on_message
        print("Connecting To broker ")
        while(not self.connectedToBroker):
            try:
                self.client.connect(self.mqHost, self.mqPort, 30)
                self.client.loop_start()
                self.client.subscribe(self.device_id)
                self.connectedToBroker = True
                print("Connected to broker")
            except:
                if(not self.mqttDisconnectionMsgShown):
                    self.connectedToBroker = False
                    print("Cannot connect to broker")
                    self.mqttDisconnectionMsgShown = True

    def __del__(self):
        pass
    
if __name__=='__main__':
    print("""Dummy Unit test :) """)
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 07:56:05 2020

@author  : Khandakar Amir Hossain
@contact : amirkhondokar@gmail.com
"""
import threading
from pyaudio_wrapper.audio_data import WavFileAudioData
import pyautogui
import paho.mqtt.client as mqtt
import json
import requests
import time

class Aim_Target_Fire(object):
    def __init__(self,GUI):        
        self.GUI = GUI
        self.next_angle = {"target": "ON",
                           "X": "090",
                           "Y": "090"}
        self.last_fired=0
        self.aim_count=0
        self.gun_cocking_audio = "./audios/gun-cocking.wav"
        self.gunshot_audio = "./audios/gun-gunshot.wav"
        self.empty_bullet_shell_audio = "./audios/empty-bullet-shell-fall.wav"
        self.arm_calibration_config = "config/arm_calibration.json"
        self.reload_simulation = WavFileAudioData(self.gun_cocking_audio)
        self.shot_simulation = WavFileAudioData(self.gunshot_audio)
        self.blank_shell_simulation = WavFileAudioData(self.empty_bullet_shell_audio) 
        self.reload = True
        self.fired_rounds = 0
        self.weapon_activated = False
        self.connectedToBroker = False
        self.invalid_angle_generated = False
        self.target_requested=False
        self.load_configuration()
        
        self.Ref_x = 320
        self.Ref_y = 180
        self.mapping_factor_x = 0.09375
        self.mapping_factor_y = 0.125
        self.update_maping_factor()
        self.publish_to_http = True
        self.last_gun_targeted_time=0
        self.last_fired = time.time()
        self.blank_shell_simulation = WavFileAudioData(self.empty_bullet_shell_audio)
        self.shot_simulation = WavFileAudioData(self.gunshot_audio)
        self.previous_angle_X="0"
        self.previous_angle_Y="0"
        if not self.publish_to_http:
            self.connect_to_broker()
        #self.cursor_window_object = pyglet.window.Window()
        #self.set_target_mouse_cursor()
        #self.set_default_mouse_cursor()
    def update_maping_factor(self):
        self.mapping_factor_x = self.GUI.PixelToDistanceRatioFactorRx.value()/(2*self.Ref_x)
        self.mapping_factor_y = self.GUI.PixelToDistanceRatioFactorRy.value()/(2*self.Ref_y)
        #print("#Mapping Factor X,Y = [{},{}]".format(self.mapping_factor_x,self.mapping_factor_y))
        
    def generate_angle(self,x,y):
        #print(x,y) 
        tempX = x-self.Ref_x
        tempY = y-self.Ref_y
        anglex = self.arm_cal_conf["angleX"]+tempX*self.mapping_factor_x
        angley = self.arm_cal_conf["angleY"]+tempY*self.mapping_factor_y
        #print("Mapping Factor X,Y = [{},{}]".format(self.mapping_factor_x,self.mapping_factor_y))
        #print("Generated Angle Sx,Sy =[{},{}]".format(anglex,angley))
        if anglex >59 and angley >59 and anglex <121 and angley<121:
            self.invalid_angle_generated = False
            self.next_angle["X"] = ""
            if anglex < 100:
                self.next_angle["X"] = "0"
            self.next_angle["X"] += str(int(anglex))
            self.next_angle["Y"] = ""
            if angley < 100:
                self.next_angle["Y"] = "0"
            self.next_angle["Y"] += str(int(angley))
        else:
            self.invalid_angle_generated = True
            self.GUI.BrokerStatusView.setText(self.GUI._translate("MainWindow","In Valid angle"))
    
    def load_configuration(self):
        with open(self.arm_calibration_config,"rb") as fp:
            self.arm_cal_conf = json.load(fp)
    
    def save_configuration(self):
        with open(self.arm_calibration_config,"w") as fp:
            json.dump(self.arm_cal_conf, fp)
    
    def on_connect(self,client, userdata, flags, rc):
        #print("Connected to broker")
        self.GUI.BrokerStatusView.setText(self.GUI._translate("MainWindow","MQTT Connected"))
    
    def on_disconnect(self,client, userdata, rc):
        #print("Disconnected from broker")
        self.GUI.BrokerStatusView.setText(self.GUI._translate("MainWindow","MQTT Disconnected"))
        
    def on_message(self,client, userdata, msg):
        MQTT_Massage = json.loads(str(msg.payload))
        if "response" in MQTT_Massage.keys():
            self.GUI.BrokerStatusView.setText(self.GUI._translate("MainWindow", MQTT_Massage["response"]))
            if MQTT_Massage["response"]=="OK" and self.GUI.AutoFireSelected.isChecked():
                self.simulate_fire()
        else:
            print(MQTT_Massage)
    
        #publish.single(self.arm_cal_conf["device_id"],json.dumps())
    def XI(self):
        self.arm_cal_conf["angleX"] += 1
        if self.publish_to_http:
            r = requests.post(url = self.arm_cal_conf["mqHost"]+"/request", data = {"command":"XI"})   
            # extracting response text  
            pastebin_url = r.text 
            #print("The pastebin URL is:%s"%pastebin_url) 
            self.GUI.BrokerStatusView.setText(self.GUI._translate("MainWindow", pastebin_url))
        else:
            self.client.publish(self.arm_cal_conf["device_id"],json.dumps({"command":"XI"}))
    
    def XD(self):
        self.arm_cal_conf["angleX"] -= 1
        if self.publish_to_http:
            r = requests.post(url = self.arm_cal_conf["mqHost"]+"/request", data = {"command":"XD"})   
            # extracting response text  
            pastebin_url = r.text 
            #print("The pastebin URL is:%s"%pastebin_url) 
            self.GUI.BrokerStatusView.setText(self.GUI._translate("MainWindow", pastebin_url))
        else:
            self.client.publish(self.arm_cal_conf["device_id"],json.dumps({"command":"XD"}))
    
    def YI(self):
        self.arm_cal_conf["angleY"] += 1
        if self.publish_to_http:
            r = requests.post(url = self.arm_cal_conf["mqHost"]+"/request", data = {"command":"YI"})   
            # extracting response text  
            pastebin_url = r.text 
            #print("The pastebin URL is:%s"%pastebin_url) 
            self.GUI.BrokerStatusView.setText(self.GUI._translate("MainWindow", pastebin_url))
        else:
            self.client.publish(self.arm_cal_conf["device_id"],json.dumps({"command":"YI"}))
    
    def YD(self):
        self.arm_cal_conf["angleY"] -= 1
        if self.publish_to_http:
            r = requests.post(url = self.arm_cal_conf["mqHost"]+"/request", data = {"command":"YD"})   
            # extracting response text  
            pastebin_url = r.text 
            #print("The pastebin URL is:%s"%pastebin_url) 
            self.GUI.BrokerStatusView.setText(self.GUI._translate("MainWindow", pastebin_url))
        else:
            self.client.publish(self.arm_cal_conf["device_id"],json.dumps({"command":"YD"}))
    
    def SetCenter(self):
        self.generate_angle(320,180)
        self.send_angle_to_arm(self.next_angle)
    
    def send_angle_to_arm(self,angle_command):
        if self.publish_to_http:
            if time.time()-self.last_gun_targeted_time>=self.GUI.Cam.aim_rate and not self.target_requested:
                self.target_requested=True
                if self.previous_angle_X!=angle_command["X"] and self.previous_angle_Y!=angle_command["Y"]: 
                    self.aim_count+=1
                    print("Requesting New Aim #{} : [AngleX={}, AngleY={}]".format(self.aim_count,angle_command["X"],angle_command["Y"]))
                    self.previous_angle_X=angle_command["X"]
                    self.previous_angle_Y=angle_command["Y"]
                    try:
                        r = requests.post(url = self.arm_cal_conf["mqHost"]+"/request", data = angle_command)
                        pastebin_url = r.text 
                        #print("The pastebin URL is:%s"%pastebin_url) 
                        self.GUI.BrokerStatusView.setText(self.GUI._translate("MainWindow", pastebin_url))
                    except Exception as eRequest:
                        print(eRequest)
                # extracting response text  
                
                self.last_gun_targeted_time = time.time()
                self.target_requested=False
            else:
                return
        else:
            self.GUI.ML_Algos.last_gun_targeted_time=time.time()
            self.client.publish(self.arm_cal_conf["device_id"],json.dumps(angle_command))
    
    def connect_to_broker(self):
        self.client = mqtt.Client()
        self.client.on_connect = self.on_connect
        self.client.on_disconnect = self.on_disconnect
        self.client.on_message = self.on_message
        print("Connecting To broker ")
        while(not self.connectedToBroker):
        	try:
        		self.client.connect(self.arm_cal_conf["mqHost"])
        		self.client.loop_start()
        		self.client.subscribe(self.arm_cal_conf["device_id"]+"/response",qos=0)
        		self.connectedToBroker = True
        		self.GUI.BrokerStatusView.setText(self.GUI._translate("MainWindow","MQTT Connected"))
        	except:
        		print("exception"),self.GUI.BrokerStatusView.setText(self.GUI._translate("MainWindow","MQTT Disconnected"))                

    def set_default_mouse_cursor(self):
        #self.cursor_default = self.cursor_window_object.get_system_mouse_cursor(pyglet.window.Window.CURSOR_CROSSHAIR)
        pass
    
    def set_target_mouse_cursor(self):
        #self.cursor_image = pyglet.image.load(self.cursor_image_file)
        #self.cursor_ico = pyglet.window.ImageMouseCursor(self.cursor_image, 16, 8)
        pass
    
    def select_manual_aim_mode(self):
        if self.GUI.ManualAimSelected.isChecked() :
            self.GUI.AutoAimSelected.setChecked(0)
            if not self.publish_to_http:
                if not self.connectedToBroker:
                    self.connect_to_broker()
            #self.cursor_window_object.set_mouse_cursor(self.cursor_ico)
        #print("settring custom cursor")
            
    def select_auto_aim_mode(self):
        if self.GUI.AutoAimSelected.isChecked() :
            self.GUI.ManualAimSelected.setChecked(0)
            if not self.publish_to_http:
                if not self.connectedToBroker:
                    self.connect_to_broker()
            #self.cursor_window_object.set_mouse_cursor(self.cursor_default)

    def aim_using_right_eye(self, event):
        if self.GUI.ManualAimSelected.isChecked(): 
            x,y = pyautogui.position()
            #print(" Mouse Raw Position       : X = {}, Y = {}".format(x,y))
            RPx = self.GUI.RightEyeView.x()
            RPy = self.GUI.RightEyeView.y()
            #print(" Frame Position           : X = {}, Y = {}".format(RPx,RPy))
            Mx = self.GUI.MainObj.x()
            My = self.GUI.MainObj.y()
            #print(" MainWindow Position      : X = {}, Y = {}".format(Mx,My))
            FrameX, FrameY = int((x-(Mx+RPx))*2.13333333), int((y-(My+RPy+36))*1.6363636)
            #print("Image Frame Position      : X = {}, Y = {}".format(FrameX,FrameY))
            #self.generate_angle(self.GUI.ML_Algos.last_gun_targeted_pos_x,self.GUI.ML_Algos.last_gun_targeted_pos_y)
            self.generate_angle(FrameX+20,FrameY)
            if not self.invalid_angle_generated:
                self.send_angle_to_arm(self.next_angle)
    
    def aim_using_left_eye(self, event):
        if self.GUI.ManualAimSelected.isChecked():
            x,y = pyautogui.position()
            #print(" Mouse Raw Position       : X = {}, Y = {}".format(x,y))
            LPx = self.GUI.LeftEyeView.x()
            LPy = self.GUI.LeftEyeView.y()
            #print(" Frame Position           : X = {}, Y = {}".format(LPx,LPy))
            Mx = self.GUI.MainObj.x()
            My = self.GUI.MainObj.y()
            #print(" MainWindow Position      : X = {}, Y = {}".format(Mx,My))
            FrameX, FrameY = int((x-(Mx+LPx))*2.133333333), int((y-(My+LPy+36))*1.6363636)
            #print("Image Frame Position      : X = {}, Y = {}".format(FrameX,FrameY))
            #self.generate_angle(self.GUI.ML_Algos.last_gun_targeted_pos_x,self.GUI.ML_Algos.last_gun_targeted_pos_y)
            self.generate_angle(FrameX,FrameY)
            if not self.invalid_angle_generated:
                self.send_angle_to_arm(self.next_angle)
            
    def aim_using_merged_eye(self, event):
        if self.GUI.ManualAimSelected.isChecked():
            x,y = pyautogui.position()
            #print(" Mouse Raw Position       : X = {}, Y = {}".format(x,y))
            LPx = self.GUI.Merged_View.x()
            LPy = self.GUI.Merged_View.y()
            #print(" Frame Position           : X = {}, Y = {}".format(LPx,LPy))
            Mx = self.GUI.MainObj.x()
            My = self.GUI.MainObj.y()
            #print(" MainWindow Position      : X = {}, Y = {}".format(Mx,My))
            FrameX, FrameY = int((x-(Mx+LPx))*2.133333333), int((y-(My+LPy+36))*1.6363636)
            #print("Image Frame Position      : X = {}, Y = {}".format(FrameX,FrameY))
            #self.generate_angle(self.GUI.ML_Algos.last_gun_targeted_pos_x,self.GUI.ML_Algos.last_gun_targeted_pos_y)
            self.generate_angle(FrameX,FrameY)
            if not self.invalid_angle_generated:
                self.send_angle_to_arm(self.next_angle)
            
    def aim(self):
        #print("aiming")
        self.GUI.ManualAimSelected.setChecked(False)
        self.GUI.AutoAimSelected.setChecked(False)
        if not self.publish_to_http:
            if not self.connectedToBroker:
                self.connect_to_broker()
        else:
            if self.GUI.ML_Algos.right_detected_time>self.GUI.ML_Algos.left_detected_time:
                threading.Thread(target=self.GUI.ML_Algos.auto_target,args=("right",)).start()
            else:
                threading.Thread(target=self.GUI.ML_Algos.auto_target,args=("left",)).start()
                
    def simulate_fire(self):
        thread = threading.Thread(target=self.parallel_fire_thread, args=())
        thread.start()
        
    def parallel_fire_thread(self):
        if time.time()-self.last_fired>=1:
            if self.weapon_activated: 
                try:
                    if self.fired_rounds % 9==0:
                        reload_simulation = WavFileAudioData(self.gun_cocking_audio)
                        reload_simulation.play()
                    self.fired_rounds += 1
                    self.GUI.RoundsFiredView.setText(self.GUI._translate("MainWindow", str(self.fired_rounds)))
                    self.last_fired = time.time()
                    self.shot_simulation.play()
                    self.blank_shell_simulation.play()
                    
                except Exception as eParallelFireSimulation:
                    print("parallel_fire_simulation_error")
                    print(eParallelFireSimulation)
            else:
                try:
                    self.GUI.RoundsFiredView.setText(self.GUI._translate("MainWindow", "Disarmed"))
                    reload_simulation = WavFileAudioData(self.gun_cocking_audio)
                    self.last_fired = time.time()
                    self.GUI.ML_Algos.target_requested=True
                    reload_simulation.play()
                    self.GUI.ML_Algos.target_requested=False
                    #self.last_fired = time.time()
                except Exception as eParallelFireSimulation:
                    print("parallel_fire_simulation_error")
                    print(eParallelFireSimulation)
                
    def toggole_weapon_activation(self):
        if self.weapon_activated:
            self.weapon_activated = False
            self.GUI.ActivateWeaponBtn.setText(self.GUI._translate("MainWindow", "Activate Weapon"))
        else:
            self.GUI.ActivateWeaponBtn.setText(self.GUI._translate("MainWindow", "Deactivate Weapon"))
            self.weapon_activated = True
        
    def __del__(self):
        pass
    
if __name__=='__main__':
    print("""Dummy Unit test :) """)

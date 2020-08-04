#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 06:06:55 2020

@author  : Khandakar Amir Hossain
@contact : amirkhondokar@gmail.com
"""
from PyQt5 import QtCore, QtGui, QtWidgets
import cv2
import time
import threading

class ML_Models(object):
    def __init__(self,GUI):
        self.Pretrained_Model_Path = "GDHCC.xml"
        self.GUI = GUI
        self.operate = 0
        self.gun_cascade = cv2.CascadeClassifier(self.Pretrained_Model_Path)
        self.font = cv2.FONT_HERSHEY_SIMPLEX
        self.RIGHT_GUN_DETECTED = False
        self.LEFT_GUN_DETECTED = False
        self.Left_PosX=0
        self.Right_PosX=0
        self.Left_PosY=0
        self.Right_PosY=0
        self.last_gun_targeted_left_pos_x  = 320
        self.last_gun_targeted_left_pos_y  = 180
        self.last_gun_targeted_right_pos_x = 320
        self.last_gun_targeted_right_pos_y = 180
        self.right_detected_time=0
        self.left_detected_time=0
        self.target_requested=False
        self.l_area=0
        self.r_area=0
        #print(self.gun_cascade.empty())
        
    def select_model(self):
        
        if self.operate ==0:
            self.GUI.SingleFrameOperationBtn.setText(self.GUI._translate("Weapon_Detection_and_Elemination_GUI_V102","Single Frame Operation"))
            self.GUI.RealTimeOperationBtn.setText(self.GUI._translate("Weapon_Detection_and_Elemination_GUI_V102","Real Time Operation"))
        elif self.operate ==-1:
            self.GUI.SingleFrameOperationBtn.setText(self.GUI._translate("Weapon_Detection_and_Elemination_GUI_V102","Stop Single Frame Op"))
        elif self.operate == 1:
            self.GUI.RealTimeOperationBtn.setText(self.GUI._translate("Weapon_Detection_and_Elemination_GUI_V102","Stop Real Time Op"))
            
            
    def single_frame_operation(self):
        if self.operate != 0:
            self.operate = 0
        else:
            self.operate = -1
        self.select_model()
        
    def realtime_operation(self):
        if self.operate != 0:
            self.operate = 0
        else:
            self.operate = 1
        self.select_model()
        
    def HCC(self):
        #temp_gray_left = cv2.cvtColor(self.GUI.Cam.left_eye_frame_with_marker, cv2.COLOR_BGR2GRAY)    
        #gun = self.gun_cascade.detectMultiScale(temp_gray_left, self.GUI.Tune_1_Value.value(), self.GUI.Tune_2_Value.value(), minSize = (int(self.GUI.Tune_3_Value.value()), int(self.GUI.Tune_3_Value.value())))
        #if len(gun) > 0:
        #    self.gun_exist_on_right_eye = True
        #for (x,y,w,h) in gun:
        #    if w<=self.GUI.Tune_4_Value.value() and h <=self.GUI.Tune_4_Value.value():
        #        self.GUI.left_eye_frame_with_marker = cv2.rectangle(self.GUI.left_eye_frame_with_marker,(x,y),(x+w,y+h),(255,0,0),2)
        #        break
        
        temp_gray_right = cv2.cvtColor(self.GUI.Cam.right_eye_frame_with_marker, cv2.COLOR_BGR2GRAY)
        temp_gray_left = cv2.cvtColor(self.GUI.Cam.left_eye_frame_with_marker, cv2.COLOR_BGR2GRAY)
        #plt.imshow(temp_gray_right,cmap='gray')
        #plt.show()
        #print(temp_gray_right.shape)
        try:
            a = float(self.GUI.Tune_1_Value.value())
            b = int(self.GUI.Tune_2_Value.value())
            s = int(self.GUI.Tune_3_Value.value())
            #print(a,b,s)
            for i in range(2):
                if i==0:
                    gun = self.gun_cascade.detectMultiScale(temp_gray_right, a, b, minSize = (s,s))
                    if len(gun) > 0:
                        self.gun_exist_on_right_eye = True
                else:
                    gun = self.gun_cascade.detectMultiScale(temp_gray_left, a, b, minSize = (s,s))
                    if len(gun) > 0:
                        self.gun_exist_on_left_eye = True
                
                for (x,y,w,h) in gun:
                    if w<= self.GUI.Tune_4_Value.value() and h <= self.GUI.Tune_4_Value.value():
                        if i==0:
                            if (x<320):
                                self.Right_PosX = 579-x
                            else:
                                self.Right_PosX = 259-(x-320)
                            self.Right_PosY=y
                            if self.Right_PosY<0:
                                self.Right_PosY=0
                            self.RIGHT_GUN_DETECTED = True
                            self.GUI.Cam.right_eye_frame_with_marker = cv2.rectangle(self.GUI.Cam.right_eye_frame_with_marker,(x,y),(x+w,y+h),(255,0,0),2)
                            self.GUI.Cam.right_eye_frame_with_marker = cv2.rectangle(self.GUI.Cam.right_eye_frame_with_marker,(x,y-9),(x+50,y+9),(200, 5, 200),18)
                            self.last_gun_targeted_right_pos_x = (x+int(w/2))
                            self.last_gun_targeted_right_pos_y = y+int(h/2)
                            self.GUI.Cam.right_eye_frame_with_marker = cv2.circle(self.GUI.Cam.right_eye_frame_with_marker,(self.last_gun_targeted_right_pos_x,self.last_gun_targeted_right_pos_y),6,(255, 255, 255),2)
                            self.last_gun_targeted_right_pos_x=640-self.last_gun_targeted_right_pos_x
                            self.right_detected_time=time.time()
                            self.r_area=w*h
                            
                            
                        
                        else:
                            if (x<320):
                                self.Left_PosX = 579-x
                            else:
                                self.Left_PosX = 259-(x-320)
                            self.Left_PosY=y
                            if self.Left_PosY<0:
                                self.Left_PosY=0
                            self.LEFT_GUN_DETECTED = True
                            self.GUI.Cam.left_eye_frame_with_marker = cv2.rectangle(self.GUI.Cam.left_eye_frame_with_marker,(x,y),(x+w,y+h),(255,0,0),2)
                            self.GUI.Cam.left_eye_frame_with_marker = cv2.rectangle(self.GUI.Cam.left_eye_frame_with_marker,(x,y-9),(x+50,y+9),(200, 5, 200),18)
                            self.last_gun_targeted_left_pos_x = (x+int(w/2))
                            self.last_gun_targeted_left_pos_y = y+int(h/2)
                            self.GUI.Cam.left_eye_frame_with_marker = cv2.circle(self.GUI.Cam.left_eye_frame_with_marker,(self.last_gun_targeted_left_pos_x,self.last_gun_targeted_left_pos_y),6,(255, 255, 255),2)
                            self.last_gun_targeted_left_pos_x=640-self.last_gun_targeted_left_pos_x
                            self.left_detected_time=time.time()
                            self.l_area=w*h
                            
                        #print("Gun Detected")
                        break
            if self.GUI.AutoAimSelected.isChecked():
                if self.l_area>self.r_area:
                    threading.Thread(target=self.auto_target,args=("right",)).start()
                else:
                    threading.Thread(target=self.auto_target,args=("left",)).start()
            #print("performing HCC")
        except Exception as eHCC:
            print("Unable to detect")
            print(eHCC)
    
    def auto_target(self,eye):
        #self.target_requested=True
        #cur_time = time.time()
        #if cur_time-self.last_gun_targeted_right_time >=self.GUI.Cam.aim_rate:
        if eye=="left":
            self.GUI.Fire_Arm.generate_angle(self.last_gun_targeted_left_pos_x,self.last_gun_targeted_left_pos_y)
        elif eye=="right":
            self.GUI.Fire_Arm.generate_angle(self.last_gun_targeted_left_pos_x,self.last_gun_targeted_left_pos_y)
        if not self.GUI.Fire_Arm.invalid_angle_generated:
            self.GUI.Fire_Arm.send_angle_to_arm(self.GUI.Fire_Arm.next_angle)
        threading.Thread(target=self.auto_fire).start()
        #self.target_requested=False
    
    def auto_fire(self):
        cur_time=time.time()
        if self.GUI.AutoFireSelected.isChecked() and cur_time-self.GUI.Fire_Arm.last_fired>10:
            #print(cur_time-self.GUI.Fire_Arm.last_fired)
            self.GUI.Fire_Arm.simulate_fire()
        
    def Resnet50(self):
        print("Operation through Resnet50")
        
    
    def Yolo(self):
        print("Operation through Yolo")
    
    def __del__(self):
        pass
    
if __name__=='__main__':
    print("Dummy Unit Test")

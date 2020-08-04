#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 11:21:37 2020

@author  : Khandakar Amir Hossain
@contact : amirkhondokar@gmail.com
"""
import cv2
import threading
from PyQt5 import QtCore, QtGui, QtWidgets
import json
import numpy as np

class Camera_Capture(object):                           # class from handelng camera video frame capture and show mechanism on GUI
    def __init__(self,GUI):
        self.GUI = GUI                                  # Qt GUI Widget object
        self.camera = {}                                # Camera dictionary to store opencv camera capture object
        self.calibrate_marker = True
        self.left_eye_frame = np.ones((640,360))        # Variable to store image frame from left camera
        self.right_eye_frame = np.ones((640,360))       # Variable to store image frame from left camera
        self.left_eye_frame_updated = False             # Variable that trigers new frame taken or not
        self.right_eye_frame_updated = False            # Variable that trigers new frame taken or not
        self.left_eye_frame_with_marker = np.ones((640,360))  # left camera frame with calibration marker +
        self.right_eye_frame_with_marker = np.ones((640,360)) # right camera frame wth calibration marker +
        self.merged_view_frame = np.ones((640,360))           # merged view of both calibrated frame
        self.capture_frame = False                      # Triger variable that will be used to enable or disable camera image capture mechanism
        self.fps = 25.0                                 # Camera captre rate at fps = frame per second
        self.single_frame_operation = False
        self.set_frame_rate(25.0)
        self.left_eye_index = 2                         # Setting default left camera index 2
        self.right_eye_index = 4                        # Setting default right camera index 4
        self.camera_calibration_config = "./config/camera_calibration.json"
        self.cam_cal_config = {}
        self.calibration_mode = False
        self.load_camera_calibration()
        
    def __del__(self):                                  # Destructor function defined explicitly to turn of camera capture in case of accidental exit with out stoping camera
       self.capture_frame = False
       self.single_frame_operation = False
    
    def set_frame_rate(self,fps=25.0):
        self.fps=fps
        self.interval = 1.0/self.fps
        self.fire_rate = self.interval*6
        self.aim_rate=self.interval*5
        if self.fps>15:
            self.aim_rate=self.interval*7
            
    def add_eye(self, EyeName="LeftEye", VideoIndex=0):
        if EyeName=="LeftEye":
            self.left_eye_index = VideoIndex
        elif EyeName=="RightEye":
            self.right_eye_index = VideoIndex
    
    def load_camera_calibration(self):
        try:
            with open(self.camera_calibration_config,"r") as fp:
                self.cam_cal_config = json.load(fp)
        except Exception as eCamCalConfig:
            print("Camera Calibration Configuration file doesn't exist")
            print("Please Save Camera Calibration Configuration before exiting")
            self.cam_cal_config = {}
            print(eCamCalConfig)
        Keys = self.cam_cal_config.keys()
        if "DistanceX" in Keys:
            self.GUI.DistanceX.setValue(self.cam_cal_config["DistanceX"])
            self.GUI.DxValue.setNum(self.cam_cal_config["DistanceX"])
        if "DistanceY" in Keys:
            self.GUI.DistanceY.setValue(self.cam_cal_config["DistanceY"])
            self.GUI.DyValue.setNum(self.cam_cal_config["DistanceY"])
        if "ZoomInLeft" in Keys:
            self.GUI.ZoomInLeft.setValue(self.cam_cal_config["ZoomInLeft"])
            self.GUI.ZLValue.setNum(self.cam_cal_config["ZoomInLeft"])
        if "ZoomInRight" in Keys:
            self.GUI.ZoomInRight.setValue(self.cam_cal_config["ZoomInRight"])
            self.GUI.ZRValue.setNum(self.cam_cal_config["ZoomInRight"])
        if "PixelToDistanceRatioFactorRx" in Keys:
            self.GUI.PixelToDistanceRatioFactorRx.setValue(self.cam_cal_config["PixelToDistanceRatioFactorRx"])
            self.GUI.RyValue.setNum(self.cam_cal_config["PixelToDistanceRatioFactorRx"])
        if "PixelToDistanceRatioFactorRy" in Keys:
            self.GUI.PixelToDistanceRatioFactorRy.setValue(self.cam_cal_config["PixelToDistanceRatioFactorRy"])
            self.GUI.RxValue.setNum(self.cam_cal_config["PixelToDistanceRatioFactorRy"])
        if "VideoFrameRate" in self.cam_cal_config.keys():
            self.GUI.VideoFrameRate.setValue(self.cam_cal_config["VideoFrameRate"])
            self.GUI.FPS_Value.setNum(self.cam_cal_config["VideoFrameRate"])
            self.set_frame_rate(self.cam_cal_config["VideoFrameRate"])
            
        if "SelectedModel" in Keys:
            self.GUI.SelectedModel.setCurrentIndex(self.cam_cal_config["SelectedModel"][0])
            if self.cam_cal_config["SelectedModel"][0] == 0:
                for i in range(1,5):
                    eval("self.GUI.Tune_"+str(i)+"_Value.setValue("+str(self.cam_cal_config["SelectedModel"][i])+")")
            elif self.cam_cal_config["SelectedModel"][0] == 1:
                pass # not implemented yet
            elif self.cam_cal_config["SelectedModel"][0] == 2:
                pass # not implemented yet
        
        
    def save_camera_calibration(self):
        self.cam_cal_config["DistanceX"] = self.GUI.DistanceX.value()
        self.cam_cal_config["DistanceY"] = self.GUI.DistanceY.value()
        self.cam_cal_config["ZoomInLeft"] = self.GUI.ZoomInLeft.value()
        self.cam_cal_config["ZoomInRight"] = self.GUI.ZoomInRight.value()
        self.cam_cal_config["PixelToDistanceRatioFactorRx"] = self.GUI.PixelToDistanceRatioFactorRx.value()
        self.cam_cal_config["PixelToDistanceRatioFactorRy"] = self.GUI.PixelToDistanceRatioFactorRy.value()
        self.cam_cal_config["VideoFrameRate"] = self.GUI.VideoFrameRate.value()
        Model_Conf = [self.GUI.SelectedModel.currentIndex()]
        for i in range(1,13):
            eval("Model_Conf.append(self.GUI.Tune_"+str(i)+"_Value.value())")
        print(Model_Conf)
        self.cam_cal_config["SelectedModel"] = Model_Conf
        with open(self.camera_calibration_config, 'w') as fp:
            json.dump(self.cam_cal_config, fp)
        self.GUI.Fire_Arm.save_configuration()
    
    def initiate_camera_resource(self):
        try:
            self.camera["LeftEye"] = cv2.VideoCapture(self.left_eye_index)
            self.camera["RightEye"] = cv2.VideoCapture(self.right_eye_index)
            self.eyes = list(self.camera.keys())
        except Exception as eCameraInitialize:
            print("Unable to Initialize Camera with index : LeftEye: {} RightEye: {} ".format(self.left_eye_index,self.right_eye_index))
            try:
                self.camera["LeftEye"] = cv2.VideoCapture(3)
                self.camera["RightEye"] = cv2.VideoCapture(5)
            except Exception as eReattempt:
                print("Reattempt also failed")
                #print(eReattempt)
                self.capture_frame = False
                self.single_frame_operation = False
            print(eCameraInitialize)
            
    def start_capture(self):
        if self.capture_frame:
            for eye in self.eyes:
                try:
                    grabbed , temp_frame = self.camera[eye].read()
                    if eye=="LeftEye" and grabbed:
                        self.left_eye_frame = temp_frame.copy()
                        self.left_eye_frame_updated = True
                    elif eye=="RightEye" and grabbed:
                        self.right_eye_frame = temp_frame.copy()
                        self.right_eye_frame_updated = True
                except Exception as eCamera_Read:
                    print("Unable to read frame")
                    #print(eCamera_Read)
                    self.capture_frame = False
            threading.Timer(self.interval, self.start_capture).start()
        else:
            print("Stopping frame capture thread")
            for eye in self.eyes:
                self.camera[eye].release()
                
    def calibrate_frames(self):
        if self.capture_frame or self.single_frame_operation:
            if self.GUI.ZoomInLeft.value() > 0 :
                self.cam_cal_config['ZL'] = self.GUI.ZoomInLeft.value()
                Xstart =(self.cam_cal_config['ZL'])
                Xstop  =-1*(self.cam_cal_config['ZL'])
                Ystart =int(0.5625*self.cam_cal_config['ZL']+0.5)
                Ystop  =int(-0.5625*self.cam_cal_config['ZL']+0.5)
                if Xstop ==0:
                    Xstop = -1
                if Ystop ==0:
                    Ystop = -1
                
                self.left_eye_frame_Zoomed_In = cv2.resize(self.left_eye_frame[Ystart:Ystop,Xstart:Xstop],(640,360))
                self.left_eye_frame_with_marker = cv2.flip(self.left_eye_frame_Zoomed_In,1)
            else:
                self.left_eye_frame_with_marker = cv2.flip(self.left_eye_frame,1)
            if self.GUI.ZoomInRight.value() > 0 :
                self.cam_cal_config['ZR'] = self.GUI.ZoomInRight.value()
                Xstart =(self.cam_cal_config['ZR'])
                Xstop  =-1*(self.cam_cal_config['ZR'])
                Ystart =int(0.5625*self.cam_cal_config['ZR']+0.5)
                Ystop  =int(-0.5625*self.cam_cal_config['ZR']+0.5)
                if Xstop ==0:
                    Xstop = -1
                if Ystop ==0:
                    Ystop = -1
                self.right_eye_frame_Zoomed_In = cv2.resize(self.right_eye_frame[Ystart:Ystop,Xstart:Xstop],(640,360))
                self.right_eye_frame_with_marker = cv2.flip(self.right_eye_frame_Zoomed_In,1)
            else:
                self.right_eye_frame_with_marker = cv2.flip(self.right_eye_frame,1)
                
            if self.GUI.SelectedModel.currentIndex() == 0 and self.GUI.ML_Algos.operate != 0:
                self.GUI.ML_Algos.HCC()
            elif self.GUI.SelectedModel.currentIndex() == 1 and self.GUI.ML_Algos.operate != 0:
                self.GUI.ML_Algos.Resnet50()
            elif self.GUI.SelectedModel.currentIndex() == 2 and self.GUI.ML_Algos.operate != 0:
                self.GUI.ML_Algos.Yolo()
            if self.GUI.CalibrationOperationMode.isChecked():
                self.left_eye_frame_with_marker = cv2.rectangle(self.left_eye_frame_with_marker,(317,0),(322,359),(52, 235, 58),2)
                self.left_eye_frame_with_marker = cv2.rectangle(self.left_eye_frame_with_marker,(0,177),(639,182),(52, 235, 58),2)
                self.right_eye_frame_with_marker = cv2.rectangle(self.right_eye_frame_with_marker,(317,0),(322,359),(52, 235, 58),2)
                self.right_eye_frame_with_marker = cv2.rectangle(self.right_eye_frame_with_marker,(0,177),(639,182),(52, 235, 58),2)
            
    def merge_frames(self):
        pass
    
    def show_views(self):
        if self.capture_frame or self.single_frame_operation:
            self.calibrate_frames()
            if self.camera["LeftEye"] and self.left_eye_frame_updated:
                temp_image = cv2.flip(self.left_eye_frame_with_marker,1)
                if self.GUI.ML_Algos.LEFT_GUN_DETECTED:
                    self.GUI.ML_Algos.LEFT_GUN_DETECTED = False
                    cv2.putText(temp_image,"GUN", (self.GUI.ML_Algos.Left_PosX,self.GUI.ML_Algos.Left_PosY), self.GUI.ML_Algos.font, 1,(255,255,255))
                temp_image = cv2.resize(temp_image, (300,220), interpolation = cv2.INTER_AREA)
                temp_image = QtGui.QImage(temp_image.data, temp_image.shape[1], temp_image.shape[0], QtGui.QImage.Format_RGB888).rgbSwapped()       
                self.GUI.LeftEyeView.setPixmap(QtGui.QPixmap.fromImage(temp_image))
                self.left_eye_frame_updated = False
            if self.camera["RightEye"] and self.right_eye_frame_updated:
                temp_image2 = cv2.flip(self.right_eye_frame_with_marker,1)
                if self.GUI.ML_Algos.RIGHT_GUN_DETECTED:
                    self.GUI.ML_Algos.RIGHT_GUN_DETECTED = False
                    cv2.putText(temp_image2,"GUN", (self.GUI.ML_Algos.Right_PosX,self.GUI.ML_Algos.Right_PosY), self.GUI.ML_Algos.font, 1,(255,255,255))
                temp_image2 = cv2.resize(temp_image2, (300,220), interpolation = cv2.INTER_AREA)
                temp_image2 = QtGui.QImage(temp_image2.data, temp_image2.shape[1], temp_image2.shape[0], QtGui.QImage.Format_RGB888).rgbSwapped()       
                self.GUI.RightEyeView.setPixmap(QtGui.QPixmap.fromImage(temp_image2))
                self.right_eye_frame_updated = False
            threading.Timer(self.interval, self.show_views).start()
        else:
            print("Stopping View thread")
            return
        
    def toggole_cam_capture(self):
        if self.capture_frame:
            print("Stopping Camera")
            self.GUI.CameraBtn.setText("Start Camera")
            self.capture_frame = False
        else:
            print("Starting Camera")
            self.GUI.CameraBtn.setText("Stop Camera")
            self.capture_frame =True
            self.initiate_camera_resource()
            self.start_capture()
            self.show_views()
            print(self.left_eye_frame.shape)
    
    def operation_mode(self):
        if not self.calibration_mode:
            self.calibration_mode = True
            self.GUI.DistanceX.setEnabled(True)
            self.GUI.DistanceY.setEnabled(True)
            self.GUI.ZoomInLeft.setEnabled(True)
            self.GUI.ZoomInRight.setEnabled(True)
            self.GUI.RefDistance.setEnabled(True)
            self.GUI.RefferenceDistance.setEnabled(True)
            self.GUI.EvaluationBtn.setEnabled(True)
            self.GUI.SaveCameraCalibrationBtn.setEnabled(True)
            self.GUI.PixelToDistanceRatioFactorRx.setEnabled(True)
            self.GUI.PixelToDistanceRatioFactorRy.setEnabled(True)
            self.GUI.ServoAngle.setEnabled(True)
            self.GUI.DecreaseServoAngleYBtn.setEnabled(True)
            self.GUI.IncreaseServoAngleYBtn.setEnabled(True)
            self.GUI.DecreaseServoAngleXBtn.setEnabled(True)
            self.GUI.IncreaseServoAngleXBtn.setEnabled(True)
            self.GUI.TargetOnCenterBtn.setEnabled(True)
            if self.GUI.SelectedModel.currentIndex() == 0:
                for i in range(1,5):
                    eval("self.GUI.Tune_"+str(i)+".setEnabled(True)")
                    eval("self.GUI.Tune_"+str(i)+"_Value.setEnabled(True)")
        else:
            self.calibration_mode = False
            self.GUI.DistanceX.setEnabled(False)
            self.GUI.DistanceY.setEnabled(False)
            self.GUI.ZoomInLeft.setEnabled(False)
            self.GUI.ZoomInRight.setEnabled(False)
            self.GUI.RefDistance.setEnabled(False)
            self.GUI.RefferenceDistance.setEnabled(False)
            self.GUI.EvaluationBtn.setEnabled(False)
            self.GUI.SaveCameraCalibrationBtn.setEnabled(False)
            self.GUI.PixelToDistanceRatioFactorRx.setEnabled(False)
            self.GUI.PixelToDistanceRatioFactorRy.setEnabled(False)
            self.GUI.ServoAngle.setEnabled(False)
            self.GUI.DecreaseServoAngleYBtn.setEnabled(False)
            self.GUI.IncreaseServoAngleYBtn.setEnabled(False)
            self.GUI.DecreaseServoAngleXBtn.setEnabled(False)
            self.GUI.IncreaseServoAngleXBtn.setEnabled(False)
            self.GUI.TargetOnCenterBtn.setEnabled(False)
            for i in range(1,13):
                eval("self.GUI.Tune_"+str(i)+".setEnabled(False)")
                eval("self.GUI.Tune_"+str(i)+"_Value.setEnabled(False)")
            
            
            
if __name__=='__main__':
    print("""Dummy Unit test :) """)

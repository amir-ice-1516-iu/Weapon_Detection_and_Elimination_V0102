#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 5 07:56:05 2020

@author  : Khandakar Amir Hossain
@contact : amirkhondokar@gmail.com
"""


from PyQt5 import QtCore, QtGui, QtWidgets
from Camera_Capture import Camera_Capture
from Detect_Weapon_Activity import Detect_Weapon_Activity
from Aim_Target_Fire import Aim_Target_Fire
from Calibrate_Camera import Calibrate_Camera
from ML_Models import ML_Models

class Ui_Weapon_Detection_and_Elemination_GUI_V102(object):
    def setupUi(self, Weapon_Detection_and_Elemination_GUI_V102):
        self.MainObj = Weapon_Detection_and_Elemination_GUI_V102
        Weapon_Detection_and_Elemination_GUI_V102.setObjectName("Weapon_Detection_and_Elemination_GUI_V102")
        Weapon_Detection_and_Elemination_GUI_V102.resize(1000, 530)
        
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Weapon_Detection_and_Elemination_GUI_V102.sizePolicy().hasHeightForWidth())
        Weapon_Detection_and_Elemination_GUI_V102.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(Weapon_Detection_and_Elemination_GUI_V102)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.LeftEyeView = QtWidgets.QLabel(self.centralwidget)
        self.LeftEyeView.setGeometry(QtCore.QRect(10, 10, 320, 240))
        self.LeftEyeView.setText("")
        self.LeftEyeView.setObjectName("LeftEyeView")
        self.RightEyeView = QtWidgets.QLabel(self.centralwidget)
        self.RightEyeView.setGeometry(QtCore.QRect(670, 10, 320, 240))
        self.RightEyeView.setText("")
        self.RightEyeView.setObjectName("RightEyeView")
        self.Merged_View = QtWidgets.QLabel(self.centralwidget)
        self.Merged_View.setGeometry(QtCore.QRect(340, 10, 320, 240))
        self.Merged_View.setText("")
        self.Merged_View.setObjectName("Merged_View")
        self.DistanceX = QtWidgets.QSlider(self.centralwidget)
        self.DistanceX.setGeometry(QtCore.QRect(10, 280, 25, 210))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DistanceX.sizePolicy().hasHeightForWidth())
        self.DistanceX.setSizePolicy(sizePolicy)
        self.DistanceX.setMaximum(255)
        self.DistanceX.setPageStep(1)
        self.DistanceX.setOrientation(QtCore.Qt.Vertical)
        self.DistanceX.setObjectName("DistanceX")
        self.DistanceX.setEnabled(False)
        self.DistanceY = QtWidgets.QSlider(self.centralwidget)
        self.DistanceY.setGeometry(QtCore.QRect(45, 280, 25, 210))
        self.DistanceY.setMaximum(255)
        self.DistanceY.setPageStep(1)
        self.DistanceY.setOrientation(QtCore.Qt.Vertical)
        self.DistanceY.setObjectName("DistanceY")
        self.DistanceY.setEnabled(False)
        self.SelectedModel = QtWidgets.QComboBox(self.centralwidget)
        self.SelectedModel.setGeometry(QtCore.QRect(110, 260, 250, 25))
        self.SelectedModel.setObjectName("SelectedModel")
        self.SelectedModel.addItem("")
        self.SelectedModel.addItem("")
        self.SelectedModel.addItem("")
        self.SelectedModel.addItem("")
        self.SelectedModel.setItemText(3, "")
        self.ClassGun = QtWidgets.QCheckBox(self.centralwidget)
        self.ClassGun.setGeometry(QtCore.QRect(670, 285, 220, 25))
        self.ClassGun.setChecked(True)
        self.ClassGun.setObjectName("ClassGun")
        self.ClassKnife = QtWidgets.QCheckBox(self.centralwidget)
        self.ClassKnife.setGeometry(QtCore.QRect(670, 310, 220, 25))
        self.ClassKnife.setObjectName("ClassKnife")
        self.ClassFighting = QtWidgets.QCheckBox(self.centralwidget)
        self.ClassFighting.setGeometry(QtCore.QRect(670, 335, 220, 25))
        self.ClassFighting.setObjectName("ClassFighting")
        self.ClassFace = QtWidgets.QCheckBox(self.centralwidget)
        self.ClassFace.setGeometry(QtCore.QRect(670, 360, 220, 25))
        self.ClassFace.setObjectName("ClassFace")
        self.ClassY = QtWidgets.QCheckBox(self.centralwidget)
        self.ClassY.setGeometry(QtCore.QRect(670, 385, 220, 25))
        self.ClassY.setObjectName("ClassY")
        self.ClassZ = QtWidgets.QCheckBox(self.centralwidget)
        self.ClassZ.setGeometry(QtCore.QRect(670, 410, 220, 25))
        self.ClassZ.setObjectName("ClassZ")
        self.SingleFrameOperationBtn = QtWidgets.QPushButton(self.centralwidget)
        self.SingleFrameOperationBtn.setGeometry(QtCore.QRect(150, 490, 170, 25))
        self.SingleFrameOperationBtn.setObjectName("SingleFrameOperationBtn")
        self.EvaluationBtn = QtWidgets.QPushButton(self.centralwidget)
        self.EvaluationBtn.setEnabled(False)
        self.EvaluationBtn.setGeometry(QtCore.QRect(465, 325, 95, 25))
        self.EvaluationBtn.setObjectName("EvaluationBtn")
        self.CameraBtn = QtWidgets.QPushButton(self.centralwidget)
        self.CameraBtn.setGeometry(QtCore.QRect(465, 490, 95, 25))
        self.CameraBtn.setObjectName("CameraBtn")
        self.RealTimeOperationBtn = QtWidgets.QPushButton(self.centralwidget)
        self.RealTimeOperationBtn.setGeometry(QtCore.QRect(670, 490, 190, 25))
        self.RealTimeOperationBtn.setObjectName("RealTimeOperationBtn")
        self.PixelToDistanceRatioFactorRx = QtWidgets.QSlider(self.centralwidget)
        self.PixelToDistanceRatioFactorRx.setGeometry(QtCore.QRect(965, 280, 25, 210))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PixelToDistanceRatioFactorRx.sizePolicy().hasHeightForWidth())
        self.PixelToDistanceRatioFactorRx.setSizePolicy(sizePolicy)
        self.PixelToDistanceRatioFactorRx.setMaximum(255)
        self.PixelToDistanceRatioFactorRx.setPageStep(1)
        self.PixelToDistanceRatioFactorRx.setOrientation(QtCore.Qt.Vertical)
        self.PixelToDistanceRatioFactorRx.setObjectName("PixelToDistanceRatioFactorRx")
        self.PixelToDistanceRatioFactorRx.setEnabled(False)
        self.PixelToDistanceRatioFactorRy = QtWidgets.QSlider(self.centralwidget)
        self.PixelToDistanceRatioFactorRy.setGeometry(QtCore.QRect(930, 280, 25, 210))
        self.PixelToDistanceRatioFactorRy.setMaximum(255)
        self.PixelToDistanceRatioFactorRy.setPageStep(1)
        self.PixelToDistanceRatioFactorRy.setOrientation(QtCore.Qt.Vertical)
        self.PixelToDistanceRatioFactorRy.setObjectName("PixelToDistanceRatioFactorRy")
        self.PixelToDistanceRatioFactorRy.setEnabled(False)
        self.Dx = QtWidgets.QLabel(self.centralwidget)
        self.Dx.setGeometry(QtCore.QRect(13, 260, 20, 17))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Dx.sizePolicy().hasHeightForWidth())
        self.Dx.setSizePolicy(sizePolicy)
        self.Dx.setObjectName("Dx")
        self.Dy = QtWidgets.QLabel(self.centralwidget)
        self.Dy.setGeometry(QtCore.QRect(48, 260, 20, 17))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Dy.sizePolicy().hasHeightForWidth())
        self.Dy.setSizePolicy(sizePolicy)
        self.Dy.setObjectName("Dy")
        self.Rx = QtWidgets.QLabel(self.centralwidget)
        self.Rx.setGeometry(QtCore.QRect(965, 260, 20, 17))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Rx.sizePolicy().hasHeightForWidth())
        self.Rx.setSizePolicy(sizePolicy)
        self.Rx.setObjectName("Rx")
        self.Ry = QtWidgets.QLabel(self.centralwidget)
        self.Ry.setGeometry(QtCore.QRect(933, 260, 20, 17))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Ry.sizePolicy().hasHeightForWidth())
        self.Ry.setSizePolicy(sizePolicy)
        self.Ry.setObjectName("Ry")
        self.DxValue = QtWidgets.QLabel(self.centralwidget)
        self.DxValue.setGeometry(QtCore.QRect(5, 490, 30, 17))
        self.DxValue.setText("")
        self.DxValue.setObjectName("DxValue")
        self.DyValue = QtWidgets.QLabel(self.centralwidget)
        self.DyValue.setGeometry(QtCore.QRect(42, 490, 30, 17))
        self.DyValue.setText("")
        self.DyValue.setObjectName("DyValue")
        self.RxValue = QtWidgets.QLabel(self.centralwidget)
        self.RxValue.setGeometry(QtCore.QRect(927, 490, 30, 17))
        self.RxValue.setText("")
        self.RxValue.setObjectName("RxValue")
        self.RyValue = QtWidgets.QLabel(self.centralwidget)
        self.RyValue.setGeometry(QtCore.QRect(965, 490, 30, 16))
        self.RyValue.setText("")
        self.RyValue.setObjectName("RyValue")
        self.ZoomInLeft = QtWidgets.QSlider(self.centralwidget)
        self.ZoomInLeft.setGeometry(QtCore.QRect(80, 280, 25, 210))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ZoomInLeft.sizePolicy().hasHeightForWidth())
        self.ZoomInLeft.setSizePolicy(sizePolicy)
        self.ZoomInLeft.setMaximum(128)
        self.ZoomInLeft.setPageStep(1)
        self.ZoomInLeft.setOrientation(QtCore.Qt.Vertical)
        self.ZoomInLeft.setObjectName("ZoomInLeft")
        self.ZoomInLeft.setEnabled(False)
        self.ZL = QtWidgets.QLabel(self.centralwidget)
        self.ZL.setGeometry(QtCore.QRect(85, 260, 20, 17))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ZL.sizePolicy().hasHeightForWidth())
        self.ZL.setSizePolicy(sizePolicy)
        self.ZL.setObjectName("ZL")
        self.ZoomInRight = QtWidgets.QSlider(self.centralwidget)
        self.ZoomInRight.setGeometry(QtCore.QRect(895, 280, 25, 210))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ZoomInRight.sizePolicy().hasHeightForWidth())
        self.ZoomInRight.setSizePolicy(sizePolicy)
        self.ZoomInRight.setMaximum(128)
        self.ZoomInRight.setPageStep(1)
        self.ZoomInRight.setOrientation(QtCore.Qt.Vertical)
        self.ZoomInRight.setObjectName("ZoomInRight")
        self.ZoomInRight.setEnabled(False)
        self.ZR = QtWidgets.QLabel(self.centralwidget)
        self.ZR.setGeometry(QtCore.QRect(900, 260, 20, 17))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ZR.sizePolicy().hasHeightForWidth())
        self.ZR.setSizePolicy(sizePolicy)
        self.ZR.setObjectName("ZR")
        self.ZLValue = QtWidgets.QLabel(self.centralwidget)
        self.ZLValue.setGeometry(QtCore.QRect(77, 490, 30, 17))
        self.ZLValue.setText("")
        self.ZLValue.setObjectName("ZLValue")
        self.ZRValue = QtWidgets.QLabel(self.centralwidget)
        self.ZRValue.setGeometry(QtCore.QRect(892, 490, 30, 17))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ZRValue.sizePolicy().hasHeightForWidth())
        self.ZRValue.setSizePolicy(sizePolicy)
        self.ZRValue.setText("")
        self.ZRValue.setObjectName("ZRValue")
        self.RefferenceDistance = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.RefferenceDistance.setEnabled(False)
        self.RefferenceDistance.setGeometry(QtCore.QRect(465, 290, 95, 25))
        self.RefferenceDistance.setObjectName("RefferenceDistance")
        self.RefDistance = QtWidgets.QLabel(self.centralwidget)
        self.RefDistance.setEnabled(False)
        self.RefDistance.setGeometry(QtCore.QRect(465, 260, 95, 25))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.RefDistance.sizePolicy().hasHeightForWidth())
        self.RefDistance.setSizePolicy(sizePolicy)
        self.RefDistance.setObjectName("RefDistance")
        self.DistanceMeasuredView = QtWidgets.QLabel(self.centralwidget)
        self.DistanceMeasuredView.setGeometry(QtCore.QRect(670, 435, 190, 25))
        self.DistanceMeasuredView.setObjectName("DistanceMeasuredView")
        self.AccuracyView = QtWidgets.QLabel(self.centralwidget)
        self.AccuracyView.setGeometry(QtCore.QRect(670, 460, 190, 25))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AccuracyView.sizePolicy().hasHeightForWidth())
        self.AccuracyView.setSizePolicy(sizePolicy)
        self.AccuracyView.setObjectName("AccuracyView")
        self.AimBtn = QtWidgets.QPushButton(self.centralwidget)
        self.AimBtn.setGeometry(QtCore.QRect(410, 490, 40, 25))
        self.AimBtn.setObjectName("AimBtn")
        self.FireBtn = QtWidgets.QPushButton(self.centralwidget)
        self.FireBtn.setGeometry(QtCore.QRect(575, 490, 40, 25))
        self.FireBtn.setObjectName("FireBtn")
        self.AutoFireSelected = QtWidgets.QCheckBox(self.centralwidget)
        self.AutoFireSelected.setGeometry(QtCore.QRect(625, 490, 30, 25))
        self.AutoFireSelected.setObjectName("AutoFireSelected")
        self.AutoAimSelected = QtWidgets.QCheckBox(self.centralwidget)
        self.AutoAimSelected.setGeometry(QtCore.QRect(370, 490, 30, 25))
        self.AutoAimSelected.setObjectName("AutoAimSelected")
        self.SelectClassesToDetect = QtWidgets.QLabel(self.centralwidget)
        self.SelectClassesToDetect.setGeometry(QtCore.QRect(670, 260, 220, 25))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SelectClassesToDetect.sizePolicy().hasHeightForWidth())
        self.SelectClassesToDetect.setSizePolicy(sizePolicy)
        self.SelectClassesToDetect.setObjectName("SelectClassesToDetect")
        self.ActivateWeaponBtn = QtWidgets.QPushButton(self.centralwidget)
        self.ActivateWeaponBtn.setGeometry(QtCore.QRect(160, 440, 148, 45))
        self.ActivateWeaponBtn.setObjectName("ActivateWeaponBtn")
        self.SaveCameraCalibrationBtn = QtWidgets.QPushButton(self.centralwidget)
        self.SaveCameraCalibrationBtn.setEnabled(False)
        self.SaveCameraCalibrationBtn.setGeometry(QtCore.QRect(425, 405, 175, 25))
        self.SaveCameraCalibrationBtn.setObjectName("SaveCameraCalibrationBtn")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(425, 355, 175, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.NormalOperationMode = QtWidgets.QRadioButton(self.groupBox)
        self.NormalOperationMode.setGeometry(QtCore.QRect(0, 3, 70, 30))
        self.NormalOperationMode.setChecked(True)
        self.NormalOperationMode.setObjectName("NormalOperationMode")
        self.CalibrationOperationMode = QtWidgets.QRadioButton(self.groupBox)
        self.CalibrationOperationMode.setGeometry(QtCore.QRect(75, 3, 95, 30))
        self.CalibrationOperationMode.setObjectName("CalibrationOperationMode")
        self.RoundsFiredView = QtWidgets.QLabel(self.centralwidget)
        self.RoundsFiredView.setGeometry(QtCore.QRect(575, 460, 80, 25))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.RoundsFiredView.sizePolicy().hasHeightForWidth())
        self.RoundsFiredView.setSizePolicy(sizePolicy)
        self.RoundsFiredView.setText("")
        self.RoundsFiredView.setObjectName("RoundsFiredView")
        self.VideoFrameRate = QtWidgets.QSlider(self.centralwidget)
        self.VideoFrameRate.setGeometry(QtCore.QRect(370, 285, 25, 185))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.VideoFrameRate.sizePolicy().hasHeightForWidth())
        self.VideoFrameRate.setSizePolicy(sizePolicy)
        self.VideoFrameRate.setMinimum(1)
        self.VideoFrameRate.setMaximum(25)
        self.VideoFrameRate.setPageStep(1)
        self.VideoFrameRate.setProperty("value", 20)
        self.VideoFrameRate.setOrientation(QtCore.Qt.Vertical)
        self.VideoFrameRate.setObjectName("VideoFrameRate")
        self.FPS = QtWidgets.QLabel(self.centralwidget)
        self.FPS.setGeometry(QtCore.QRect(370, 260, 25, 17))
        self.FPS.setObjectName("FPS")
        self.FPS_Value = QtWidgets.QLabel(self.centralwidget)
        self.FPS_Value.setGeometry(QtCore.QRect(367, 470, 30, 17))
        self.FPS_Value.setText("")
        self.FPS_Value.setObjectName("FPS_Value")
        self.Tune_1_Value = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.Tune_1_Value.setGeometry(QtCore.QRect(110, 310, 60, 25))
        self.Tune_1_Value.setObjectName("Tune_1_Value")
        self.Tune_1 = QtWidgets.QLabel(self.centralwidget)
        self.Tune_1.setGeometry(QtCore.QRect(110, 290, 60, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Tune_1.sizePolicy().hasHeightForWidth())
        self.Tune_1.setSizePolicy(sizePolicy)
        self.Tune_1.setObjectName("Tune_1")
        self.Tune_2_Value = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.Tune_2_Value.setGeometry(QtCore.QRect(173, 310, 60, 25))
        self.Tune_2_Value.setObjectName("Tune_2_Value")
        self.Tune_2 = QtWidgets.QLabel(self.centralwidget)
        self.Tune_2.setGeometry(QtCore.QRect(173, 290, 60, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Tune_2.sizePolicy().hasHeightForWidth())
        self.Tune_2.setSizePolicy(sizePolicy)
        self.Tune_2.setObjectName("Tune_2")
        self.Tune_3_Value = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.Tune_3_Value.setGeometry(QtCore.QRect(237, 310, 60, 25))
        self.Tune_3_Value.setObjectName("Tune_3_Value")
        self.Tune_3 = QtWidgets.QLabel(self.centralwidget)
        self.Tune_3.setGeometry(QtCore.QRect(237, 290, 60, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Tune_3.sizePolicy().hasHeightForWidth())
        self.Tune_3.setSizePolicy(sizePolicy)
        self.Tune_3.setObjectName("Tune_3")
        self.Tune_4_Value = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.Tune_4_Value.setGeometry(QtCore.QRect(300, 310, 60, 25))
        self.Tune_4_Value.setObjectName("Tune_4_Value")
        self.Tune_4 = QtWidgets.QLabel(self.centralwidget)
        self.Tune_4.setGeometry(QtCore.QRect(300, 290, 60, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Tune_4.sizePolicy().hasHeightForWidth())
        self.Tune_4.setSizePolicy(sizePolicy)
        self.Tune_4.setObjectName("Tune_4")
        self.Tune_7_Value = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.Tune_7_Value.setGeometry(QtCore.QRect(237, 360, 60, 25))
        self.Tune_7_Value.setObjectName("Tune_7_Value")
        self.Tune_6_Value = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.Tune_6_Value.setGeometry(QtCore.QRect(173, 360, 60, 25))
        self.Tune_6_Value.setObjectName("Tune_6_Value")
        self.Tune_5 = QtWidgets.QLabel(self.centralwidget)
        self.Tune_5.setGeometry(QtCore.QRect(110, 340, 60, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Tune_5.sizePolicy().hasHeightForWidth())
        self.Tune_5.setSizePolicy(sizePolicy)
        self.Tune_5.setObjectName("Tune_5")
        self.Tune_8_Value = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.Tune_8_Value.setGeometry(QtCore.QRect(300, 360, 60, 25))
        self.Tune_8_Value.setObjectName("Tune_8_Value")
        self.Tune_5_Value = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.Tune_5_Value.setGeometry(QtCore.QRect(110, 360, 60, 25))
        self.Tune_5_Value.setObjectName("Tune_5_Value")
        self.Tune_6 = QtWidgets.QLabel(self.centralwidget)
        self.Tune_6.setGeometry(QtCore.QRect(173, 340, 60, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Tune_6.sizePolicy().hasHeightForWidth())
        self.Tune_6.setSizePolicy(sizePolicy)
        self.Tune_6.setObjectName("Tune_6")
        self.Tune_7 = QtWidgets.QLabel(self.centralwidget)
        self.Tune_7.setGeometry(QtCore.QRect(237, 340, 60, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Tune_7.sizePolicy().hasHeightForWidth())
        self.Tune_7.setSizePolicy(sizePolicy)
        self.Tune_7.setObjectName("Tune_7")
        self.Tune_8 = QtWidgets.QLabel(self.centralwidget)
        self.Tune_8.setGeometry(QtCore.QRect(300, 340, 60, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Tune_8.sizePolicy().hasHeightForWidth())
        self.Tune_8.setSizePolicy(sizePolicy)
        self.Tune_8.setObjectName("Tune_8")
        self.Tune_11_Value = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.Tune_11_Value.setGeometry(QtCore.QRect(237, 410, 60, 25))
        self.Tune_11_Value.setObjectName("Tune_11_Value")
        self.Tune_10_Value = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.Tune_10_Value.setGeometry(QtCore.QRect(173, 410, 60, 25))
        self.Tune_10_Value.setObjectName("Tune_10_Value")
        self.Tune_9 = QtWidgets.QLabel(self.centralwidget)
        self.Tune_9.setGeometry(QtCore.QRect(110, 390, 60, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Tune_9.sizePolicy().hasHeightForWidth())
        self.Tune_9.setSizePolicy(sizePolicy)
        self.Tune_9.setObjectName("Tune_9")
        self.Tune_12_Value = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.Tune_12_Value.setGeometry(QtCore.QRect(300, 410, 60, 25))
        self.Tune_12_Value.setObjectName("Tune_12_Value")
        self.Tune_9_Value = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.Tune_9_Value.setGeometry(QtCore.QRect(110, 410, 60, 25))
        self.Tune_9_Value.setObjectName("Tune_9_Value")
        self.Tune_10 = QtWidgets.QLabel(self.centralwidget)
        self.Tune_10.setGeometry(QtCore.QRect(173, 390, 60, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Tune_10.sizePolicy().hasHeightForWidth())
        self.Tune_10.setSizePolicy(sizePolicy)
        self.Tune_10.setObjectName("Tune_10")
        self.Tune_11 = QtWidgets.QLabel(self.centralwidget)
        self.Tune_11.setGeometry(QtCore.QRect(237, 390, 60, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Tune_11.sizePolicy().hasHeightForWidth())
        self.Tune_11.setSizePolicy(sizePolicy)
        self.Tune_11.setObjectName("Tune_11")
        self.Tune_12 = QtWidgets.QLabel(self.centralwidget)
        self.Tune_12.setGeometry(QtCore.QRect(300, 390, 60, 20))
        for i in range(1,13):
            eval("self.Tune_"+str(i)+"_Value.setMinimum(-255.0)")
            eval("self.Tune_"+str(i)+"_Value.setMaximum(255.0)")
            eval("self.Tune_"+str(i)+".setEnabled(False)")
            eval("self.Tune_"+str(i)+"_Value.setEnabled(False)")
        self.ManualAimSelected = QtWidgets.QCheckBox(self.centralwidget)
        self.ManualAimSelected.setGeometry(QtCore.QRect(410, 460, 35, 25))
        self.ManualAimSelected.setObjectName("ManualAimSelected")
        self.IncreaseServoAngleXBtn = QtWidgets.QPushButton(self.centralwidget)
        self.IncreaseServoAngleXBtn.setEnabled(False)
        self.IncreaseServoAngleXBtn.setGeometry(QtCore.QRect(625, 315, 25, 25))
        self.IncreaseServoAngleXBtn.setDefault(True)
        self.IncreaseServoAngleXBtn.setObjectName("IncreaseServoAngleXBtn")
        self.DecreaseServoAngleXBtn = QtWidgets.QPushButton(self.centralwidget)
        self.DecreaseServoAngleXBtn.setEnabled(False)
        self.DecreaseServoAngleXBtn.setGeometry(QtCore.QRect(575, 315, 25, 25))
        self.DecreaseServoAngleXBtn.setDefault(True)
        self.DecreaseServoAngleXBtn.setObjectName("DecreaseServoAngleXBtn")
        self.TargetOnCenterBtn=QtWidgets.QPushButton(self.centralwidget)
        self.TargetOnCenterBtn.setEnabled(False)
        self.TargetOnCenterBtn.setGeometry(QtCore.QRect(600,315,25,25))
        self.TargetOnCenterBtn.setDefault(True)
        self.TargetOnCenterBtn.setObjectName("TargetOnCenterBtn")
        self.IncreaseServoAngleYBtn = QtWidgets.QPushButton(self.centralwidget)
        self.IncreaseServoAngleYBtn.setEnabled(False)
        self.IncreaseServoAngleYBtn.setGeometry(QtCore.QRect(600, 290, 25, 25))
        self.IncreaseServoAngleYBtn.setDefault(True)
        self.IncreaseServoAngleYBtn.setFlat(False)
        self.IncreaseServoAngleYBtn.setObjectName("IncreaseServoAngleYBtn")
        self.DecreaseServoAngleYBtn = QtWidgets.QPushButton(self.centralwidget)
        self.DecreaseServoAngleYBtn.setEnabled(False)
        self.DecreaseServoAngleYBtn.setGeometry(QtCore.QRect(600, 340, 25, 25))
        self.DecreaseServoAngleYBtn.setDefault(True)
        self.DecreaseServoAngleYBtn.setObjectName("DecreaseServoAngleYBtn")
        self.ServoAngle = QtWidgets.QLabel(self.centralwidget)
        self.ServoAngle.setEnabled(False)
        self.ServoAngle.setGeometry(QtCore.QRect(570, 260, 85, 25))
        
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Tune_12.sizePolicy().hasHeightForWidth())
        self.Tune_12.setSizePolicy(sizePolicy)
        self.Tune_12.setObjectName("Tune_12")
        self.BrokerStatusView = QtWidgets.QLabel(self.centralwidget)
        self.BrokerStatusView.setGeometry(QtCore.QRect(425, 430, 175, 25))
        self.BrokerStatusView.setText("nohunkypunky")
        self.BrokerStatusView.setObjectName("BrokerStatusView")
###############################################################################
        self._translate = QtCore.QCoreApplication.translate
        self.Cam = Camera_Capture(GUI=self)
        self.Cam.add_eye("LeftEye", 2)
        self.Cam.add_eye("RightEye", 4)
        self.Detect_Weapon = Detect_Weapon_Activity(GUI=self)
        self.Fire_Arm = Aim_Target_Fire(GUI=self)
        self.Camera_Calibration = Calibrate_Camera(GUI=self)
        self.ML_Algos = ML_Models(GUI=self)
###############################################################################
        Weapon_Detection_and_Elemination_GUI_V102.setCentralWidget(self.centralwidget)
        self.actionNormal_Mode = QtWidgets.QAction(Weapon_Detection_and_Elemination_GUI_V102)
        self.actionNormal_Mode.setObjectName("actionNormal_Mode")
        self.actionCalibration_Mode = QtWidgets.QAction(Weapon_Detection_and_Elemination_GUI_V102)
        self.actionCalibration_Mode.setObjectName("actionCalibration_Mode")

        self.retranslateUi(Weapon_Detection_and_Elemination_GUI_V102)
        self.DistanceX.valueChanged['int'].connect(self.DxValue.setNum)
        self.DistanceY.valueChanged['int'].connect(self.DyValue.setNum)
        self.ZoomInLeft.valueChanged['int'].connect(self.ZLValue.setNum)
        self.ZoomInRight.valueChanged['int'].connect(self.ZRValue.setNum)
        self.PixelToDistanceRatioFactorRy.valueChanged['int'].connect(self.RxValue.setNum)
        self.PixelToDistanceRatioFactorRx.valueChanged['int'].connect(self.RyValue.setNum)
        self.VideoFrameRate.valueChanged['int'].connect(self.FPS_Value.setNum)
        self.VideoFrameRate.valueChanged['int'].connect(self.Cam.set_frame_rate)
        
        self.CameraBtn.clicked.connect(self.Cam.toggole_cam_capture)
        self.ZoomInLeft.valueChanged['int'].connect(self.Cam.calibrate_frames)
        self.ZoomInRight.valueChanged['int'].connect(self.Cam.calibrate_frames)
        self.PixelToDistanceRatioFactorRx.valueChanged.connect(self.Fire_Arm.update_maping_factor)
        self.PixelToDistanceRatioFactorRy.valueChanged.connect(self.Fire_Arm.update_maping_factor)
        self.SaveCameraCalibrationBtn.clicked.connect(self.Cam.save_camera_calibration)
        self.FireBtn.clicked.connect(self.Fire_Arm.simulate_fire)
        self.AimBtn.clicked.connect(self.Fire_Arm.aim)
        self.ActivateWeaponBtn.clicked.connect(self.Fire_Arm.toggole_weapon_activation)
        self.NormalOperationMode.toggled.connect(self.Cam.operation_mode)
        self.SingleFrameOperationBtn.clicked.connect(self.ML_Algos.single_frame_operation)
        self.RealTimeOperationBtn.clicked.connect(self.ML_Algos.realtime_operation)
        self.ManualAimSelected.stateChanged.connect(self.Fire_Arm.select_manual_aim_mode)
        self.AutoAimSelected.stateChanged.connect(self.Fire_Arm.select_auto_aim_mode)
        self.LeftEyeView.mousePressEvent = self.Fire_Arm.aim_using_left_eye
        self.RightEyeView.mousePressEvent = self.Fire_Arm.aim_using_right_eye
        self.Merged_View.mousePressEvent = self.Fire_Arm.aim_using_merged_eye
        self.IncreaseServoAngleXBtn.clicked.connect(self.Fire_Arm.XI)
        self.IncreaseServoAngleYBtn.clicked.connect(self.Fire_Arm.YI)
        self.DecreaseServoAngleXBtn.clicked.connect(self.Fire_Arm.XD)
        self.DecreaseServoAngleYBtn.clicked.connect(self.Fire_Arm.YD)
        self.TargetOnCenterBtn.clicked.connect(self.Fire_Arm.SetCenter)
        QtCore.QMetaObject.connectSlotsByName(Weapon_Detection_and_Elemination_GUI_V102)

    def retranslateUi(self, Weapon_Detection_and_Elemination_GUI_V102):
        _translate = QtCore.QCoreApplication.translate
        Weapon_Detection_and_Elemination_GUI_V102.setWindowTitle(_translate("Weapon_Detection_and_Elemination_GUI_V102", "MainWindow"))
        self.SelectedModel.setItemText(0, _translate("Weapon_Detection_and_Elemination_GUI_V102", "Haar Cascade Classifier"))
        self.SelectedModel.setItemText(1, _translate("Weapon_Detection_and_Elemination_GUI_V102", "Resnet50"))
        self.SelectedModel.setItemText(2, _translate("Weapon_Detection_and_Elemination_GUI_V102", "Yolo"))
        self.ClassGun.setText(_translate("Weapon_Detection_and_Elemination_GUI_V102", "Gun"))
        self.ClassKnife.setText(_translate("Weapon_Detection_and_Elemination_GUI_V102", "Knife"))
        self.ClassFighting.setText(_translate("Weapon_Detection_and_Elemination_GUI_V102", "Fighting"))
        self.ClassFace.setText(_translate("Weapon_Detection_and_Elemination_GUI_V102", "Face"))
        self.ClassY.setText(_translate("Weapon_Detection_and_Elemination_GUI_V102", "ClassY"))
        self.ClassZ.setText(_translate("Weapon_Detection_and_Elemination_GUI_V102", "ClassZ"))
        self.SingleFrameOperationBtn.setText(_translate("Weapon_Detection_and_Elemination_GUI_V102", "Single Frame Operation"))
        self.EvaluationBtn.setText(_translate("Weapon_Detection_and_Elemination_GUI_V102", "Evaluate"))
        self.CameraBtn.setText(_translate("Weapon_Detection_and_Elemination_GUI_V102", "Start Camera"))
        self.RealTimeOperationBtn.setText(_translate("Weapon_Detection_and_Elemination_GUI_V102", "Real Time Operation"))
        self.Dx.setText(_translate("Weapon_Detection_and_Elemination_GUI_V102", "Dx"))
        self.Dy.setText(_translate("Weapon_Detection_and_Elemination_GUI_V102", "Dy"))
        self.Rx.setText(_translate("Weapon_Detection_and_Elemination_GUI_V102", "Ax"))
        self.Ry.setText(_translate("Weapon_Detection_and_Elemination_GUI_V102", "Ay"))
        self.ZL.setText(_translate("Weapon_Detection_and_Elemination_GUI_V102", "ZL"))
        self.ZR.setText(_translate("Weapon_Detection_and_Elemination_GUI_V102", "ZR"))
        self.RefDistance.setText(_translate("Weapon_Detection_and_Elemination_GUI_V102", "Ref Distance"))
        self.DistanceMeasuredView.setText(_translate("Weapon_Detection_and_Elemination_GUI_V102", "Distance Measured: "))
        self.AccuracyView.setText(_translate("Weapon_Detection_and_Elemination_GUI_V102", "Accuracy :"))
        self.AimBtn.setText(_translate("Weapon_Detection_and_Elemination_GUI_V102", "Aim"))
        self.FireBtn.setText(_translate("Weapon_Detection_and_Elemination_GUI_V102", "Fire"))
        self.AutoFireSelected.setText(_translate("Weapon_Detection_and_Elemination_GUI_V102", "A"))
        self.AutoAimSelected.setText(_translate("Weapon_Detection_and_Elemination_GUI_V102", "A"))
        self.SelectClassesToDetect.setText(_translate("Weapon_Detection_and_Elemination_GUI_V102", "Select Classes to Detect"))
        self.ActivateWeaponBtn.setText(_translate("Weapon_Detection_and_Elemination_GUI_V102", "Activate Weapon"))
        self.SaveCameraCalibrationBtn.setText(_translate("Weapon_Detection_and_Elemination_GUI_V102", "Save Camera Calibration"))
        self.NormalOperationMode.setText(_translate("Weapon_Detection_and_Elemination_GUI_V102", "Normal"))
        self.CalibrationOperationMode.setText(_translate("Weapon_Detection_and_Elemination_GUI_V102", "Calibration"))
        self.FPS.setText(_translate("Weapon_Detection_and_Elemination_GUI_V102", "FPS"))
        self.Tune_1.setText(_translate("Weapon_Detection_and_Elemination_GUI_V102", "Tune_01"))
        self.Tune_2.setText(_translate("Weapon_Detection_and_Elemination_GUI_V102", "Tune_02"))
        self.Tune_3.setText(_translate("Weapon_Detection_and_Elemination_GUI_V102", "Tune_03"))
        self.Tune_4.setText(_translate("Weapon_Detection_and_Elemination_GUI_V102", "Tune_04"))
        self.Tune_5.setText(_translate("Weapon_Detection_and_Elemination_GUI_V102", "Tune_05"))
        self.Tune_6.setText(_translate("Weapon_Detection_and_Elemination_GUI_V102", "Tune_06"))
        self.Tune_7.setText(_translate("Weapon_Detection_and_Elemination_GUI_V102", "Tune_07"))
        self.Tune_8.setText(_translate("Weapon_Detection_and_Elemination_GUI_V102", "Tune_08"))
        self.Tune_9.setText(_translate("Weapon_Detection_and_Elemination_GUI_V102", "Tune_09"))
        self.Tune_10.setText(_translate("Weapon_Detection_and_Elemination_GUI_V102", "Tune_10"))
        self.Tune_11.setText(_translate("Weapon_Detection_and_Elemination_GUI_V102", "Tune_11"))
        self.Tune_12.setText(_translate("Weapon_Detection_and_Elemination_GUI_V102", "Tune_12"))
        self.ManualAimSelected.setText(_translate("Weapon_Detection_and_Elemination_GUI_V102", "M"))
        self.IncreaseServoAngleXBtn.setText(_translate("Weapon_Detection_and_Elemination_GUI_V102", ">"))
        self.DecreaseServoAngleXBtn.setText(_translate("Weapon_Detection_and_Elemination_GUI_V102", "<"))
        self.TargetOnCenterBtn.setText(_translate("Weapon_Detection_and_Elemination_GUI_V102","C"))
        self.IncreaseServoAngleYBtn.setText(_translate("Weapon_Detection_and_Elemination_GUI_V102", "^"))
        self.DecreaseServoAngleYBtn.setText(_translate("Weapon_Detection_and_Elemination_GUI_V102", "v"))
        self.ServoAngle.setText(_translate("Weapon_Detection_and_Elemination_GUI_V102", "Servo Angle"))
        self.actionNormal_Mode.setText(_translate("Weapon_Detection_and_Elemination_GUI_V102", "Normal Mode"))
        self.actionCalibration_Mode.setText(_translate("Weapon_Detection_and_Elemination_GUI_V102", "Calibration Mode"))

        self.Cam.load_camera_calibration()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Weapon_Detection_and_Elemination_GUI_V102 = QtWidgets.QMainWindow()
    ui = Ui_Weapon_Detection_and_Elemination_GUI_V102()
    ui.setupUi(Weapon_Detection_and_Elemination_GUI_V102)
    Weapon_Detection_and_Elemination_GUI_V102.show()
    Return_Code = app.exec_()
    print("Exiting from gui")
    ui.Cam.capture_frame = False
    ui.Cam.single_frame_operation = False
    sys.exit(Return_Code)
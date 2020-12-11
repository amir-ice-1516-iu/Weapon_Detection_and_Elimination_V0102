# Weapon_Detection_and_Elimination_V0102
0. Observe images in folder "Circuit_Diagrams_and_Screen_shots" for clearification and demo 
Initial Prototype: https://drive.google.com/file/d/1-_B-KYTBl_ODTwAf7hcii62sPeNUS1HA/view?usp=sharing
GUI Demonstration: https://drive.google.com/file/d/1X-_2pPH39c2BelUElIT-0_LRTCY1aP_M/view?usp=sharing
1. Installation: <br>
  <t> $ sudo apt-get install python3-pip <br>
  <t> $ cd Weapon_Detection_and_Elimination_V0102 <br>
  <t> $ pip3 install -r requirements.txt <br>
<br>
2. Now upload MCU_Code_ESP.ino file to node MCU and connect two servo motor and one laser accordingly.<br>
<br>
3. Then connect <br>
    left USB camera<br>
  and wait for 10 seconds<br>
    right USB camera<br>
<br>
4. check camera feeds using cheese or other image capturing software.<br>
<br>
5. power on the fire arm node (NodeMCU and servos)[ make sure about the common ground of both servos and NodeMCU]<br>
<br>
6. check IP of the fire arm node (NodeMCU) using serial monitor with a baud rate of 115200<br>
<br>
7. Finally start the GUI program by typing command as follows <br>
  <t> $ python3 Exp_GUI_test_V0102.py<br>
<br>
8. If required do some software calibration for camera and fire arm node and save calibration <br>
   and use in normal mode<br>
<br>
9. Now play with the features of Weapon Detection and Elimination<br>

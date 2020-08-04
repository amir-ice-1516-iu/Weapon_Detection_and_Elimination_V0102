# Weapon_Detection_and_Elimination_V0102
1. Installation:\n
  $ sudo apt-get install python3-pip\n
  $ cd Weapon_Detection_and_Elimination_V0102\n
  $ pip3 install -r requirements.txt\n
2. Now upload MCU_Code_ESP.ino file to node MCU and connect two servo motor and one laser accordingly.

3. Then connect 
    left USB camera
  and wait for 10 seconds
    right USB camera
4. check camera feeds using cheese or other image capturing software.

5. power on the fire arm node (NodeMCU and servos)[ make sure about the common ground of both servos and NodeMCU]
6. check IP of the fire arm node (NodeMCU) using serial monitor with a baud rate of 115200
7. Finally start the GUI program by typing command as follows

  \t$ python3 Exp_GUI_test_V0102.py

8. If required do some software calibration for camera and fire arm node and save calibration 
   and use in normal mode
9. Now play with the features of Weapon Detection and Elimination

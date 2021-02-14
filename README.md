# Weapon_Detection_and_Elimination_V0102<br>
  <t> A prototype that takes live image feeds from camera and detects <br>
  <t> guns( unauthorized weapon ) and locates the center position of the <br>
  <t> gun. Then sends signal to an electromechanical fire arm to target <br>
  <t> a laser pointer(Dummy fire arm) on that gun and waits for fire <br>
  <t> command from authority . Besides there’s an extra feature to <br>
  <t> manually target on any  random position by just simply clicking on <br>
  <t> the live video frame in the designed GUI for the device.<br>
  <br>
0. Observe images in folder "Circuit_Diagrams_and_Screen_shots" for clearification and demo <br>
  <t> Initial Prototype: https://drive.google.com/file/d/1gASbtAKnxIejWa7tDE7ymffy53rzsErD/view?usp=sharing <br>
  <t> GUI Demonstration: i.  https://drive.google.com/file/d/1uewJqxqe6S0Sc7AacSzhLSi0T06yAiSz/view?usp=sharing <br>
  <t> GUI Demonstration: ii. https://drive.google.com/file/d/1ZmnTItYIykayfw3n3Yi8O9ZAP5Sw8yZT/view?usp=sharing <br>
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

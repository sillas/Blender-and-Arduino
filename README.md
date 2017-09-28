# Blender-and-Arduino
Simple integration of Blender with Arduino.

This method is used to integrate an Arduino microcontroller with Blender Software. It's consist of three parts: The Arduino Code, The python Script in Blender and the pySerial Script.

The Arduino Microcontroller sends data throught serial port to pySerial, who writes these data on a "swap" file (a simple pure text file).
The Python script in the Blender, reads these files and control the 3D Model.
* The pySerial Script writes data to file at the same time that the Blender script reads ones.

Instructions:
Arduino Circuit:
 - Connect a potentiometer on the AN0 pin of your Arduino like this: 
 http://1.bp.blogspot.com/-_zcNGBwINrg/VlzAmbPZXiI/AAAAAAAACRA/5Ngm-40Fb3A/s320/Capturar.PNG. 
 - Connect the Arduino to your computer.

1 - Open the Arduino IDE and write the "ArduinoCode1" Sketch to your Arduino (Tested in Arduino UNO);
2 - Install the pySerial (https://pypi.python.org/pypi/pyserial);
3 - Run "getSerial.py"
4 - Open "Model.blend" and Press "P" to run the Game Engine.
5 - Rotate the potentiometer to see the 3D Model moves her mouth.
Press ESC to terminate.

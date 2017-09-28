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



Copyright (c) 2017 sillassamyr@gmail.com

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

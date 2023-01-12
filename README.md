# HID-Conversion-For-CH340-Arduino
As most of sim fans needs to make custom panels to level up their gaming experience, most of them need to get genuine arduino or arduino leonardo to be able to register their arduino as HID device. I decided to do this 5 minute of job to be able to use my CH340 chip Arduino in my custom thruster project. 

Using this code is very simple first things first we need to install needed libraries. You can use pip install commands given below.
for serial library:
                    pip install pyserial
for vgamepad library:
                    pip install vgamepad

After installing libraries you need to flash your arduino with given code and do some simplest circuitry as given below.


![Example Potentiometer Connection Schematic](https://user-images.githubusercontent.com/57843246/212181727-73cf8283-2da3-4b1c-a641-dd688abbad49.png)

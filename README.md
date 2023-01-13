# HID-Conversion-For-CH340-Arduino
As most of sim fans needs to make custom panels to level up their gaming experience, most of them need to get genuine arduino or arduino leonardo to be able to register their arduino as HID device. I decided to do this 5 minute of job to be able to use my CH340 chip Arduino in my custom thruster project. 
## Guideline for This Project
1. Installing Presuquities
   -Python Libraries
   -Arduino IDE
   -Python IDE or even Notepad
2. Installing Arduino Code
3. Setting the Python Code


### Installing Presuquities
Using this code is very simple, first things first we need to install required libraries for Python. You can use pip install commands given below.
for serial library:
                    pip install pyserial
for vgamepad library:
                    pip install vgamepad

After installing libraries you need to flash your arduino with given code. In order to flash given Arduino code we need to install Arduino IDE to your computer. You can install Arduino IDE by visiting:
>https://www.arduino.cc/en/software

After Installing Arduino IDE lets continue with Arduino circuitry. Please be carefull while connecting your potentiometer to your board and complete the circuit in accordance with the figure given below.

![Example Potentiometer Connection Schematic](https://user-images.githubusercontent.com/57843246/212181727-73cf8283-2da3-4b1c-a641-dd688abbad49.png)


In order to make changes to our main Python code you can use a IDE familiar to you or you may prefer not to install anything and do the change on Notepad. Either you install an IDE or not we need to change a little part of our code but dont worry, i flashed the part you need to change.


### Installing Arduino Code

Eventually we may proceed to upload our Arduino code to our board. Please open the folder given in Repository with Arduino IDE and just press Upload button on top left part of the window. After you see **Done uploading** message you can assume your card started to work properly in order to measure the position of our potentiometer. You can crosscheck your board with serial monitor if your board measures the pot or not. Please hit the **Tools** menu located top left of the IDE window. In that menu find **Port** section and note down the COMport number that you uploaded the Arduino code.

### Setting the Python Code

In final steps of our setup, we need to change just a little variable in order to make code compatible with our PC. 
Here is the part you need to change
>PORT = "5" #Enter The Port Number you noted down HERE. Example usage: "5"

You just need to change **5** to **your COM port number** in order to make sure your system works. 

## Final Words

It was a 5 min project, that my friend and me just wanted to not to stuck to hardware problems. I am open for suggestions and please feel free to use and comment our program. 

Thanks for inspiration Burak

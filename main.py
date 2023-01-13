import serial
import vgamepad as vg
import time


# \\\\\
# \\\\\\\\\\\\
PORT = "5"  # Enter The Port Number you noted down HERE. Example usage: "5"
# ////////////
# /////

control = 0
System = True
gamepad = vg.VX360Gamepad()
Reconnect = True


def main():
    global Reconnect
    global control
    global System
    try:
        serialPort = serial.Serial(port=("COM" + PORT), baudrate=115200,
                                   bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE)
    except:
        print("\nChoosen Port doesn't exist or cannot be reached. This can be either malfunctioned cable or Arduino."
              " Please choose another comport for your Arduino and try again")
        if not Reconnect:
            print("\nProgram ended due to errors listed above. Please investigate the given problems before trying again.")
            time.sleep(10)
            raise SystemExit
        else:
            control = control + 1
            time.sleep(0.5)
            if control < 10:
                main()
            else:
                Reconnect = False


    serialString = ""  # Used to hold data coming over UART
    print("\nConnection Succesfull")
    control = 0

    while System:
        try:
            # Read data out of the buffer until a carraige return / new line is found
            serialString = serialPort.readline()
            ard_num = serialString.decode('Ascii')
            # Convertion of String to Integer in order to comply with library
            ard_num = int(ard_num)
            gamepad.right_joystick(x_value=0, y_value=ard_num)
            # enter the new value we get from arduino.
            gamepad.update()
            # update the status of our virtual gamepad.
        except (ValueError, UnboundLocalError, TypeError, serial.serialutil.SerialException) as error:
            print("\n" + str(error) + " has occured")
            control = control + 1
            time.sleep(0.5)
            main()


main()
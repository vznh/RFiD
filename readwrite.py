# Code for reading and writing RFID cards.
# This is used when the computer is out of boot to code only.
# Needs to be used when rPi is in boot to startup mode only.

import RPi.GPIO as g 
import SimpleMFRC522 as s

reader = s.s() # rfid reader
reading = True

option = input("read or write this RFID card") # choice for reading / writing

if option == "read":
    while reading:
        print("you are now reading this RFID card")
        serial, text = reader.reading() # serial # of RFID card and text (if there is any) on card
        print(f"serial number: {serial}\n") 
        print(f"attached to card: {text}")
        reading=False
    GPIO.cleanup() # cleans up reader so next one isn't jumbled
    exit()

elif option == "write":
    reading = False
    ttbw = input("Type new data:\n") # text to be written
    print("\nPlease place your RFID object.")
    reader.write(ttbw)
    reading = True
    while reading:
        serial, text = reader.reading()
        if ttbw in text: # checks if ttbw was actually written. if not, omits error message
            outcome = True
        if outcome == True:
            print(f"Successful. Card has been written {ttbw}.")
        else:
            print(f"Failed. Retry.")
        reading = False
        GPIO.cleanup()
        exit()

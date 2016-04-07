#!/usr/bin/python
import RPi.GPIO as GPIO
import time 
#=========================================

LED = 23

ON = 1
OFF = 0  

#=========================================

def pins(pin_num, time_on):    
    GPIO.output(pin_num, int_ON)
    time.sleep(time_on)
    GPIO.output(pin_num, int_OFF)      
#=========================================
def lights(pin_num, time_interval):
    
    light_pin(pin_num, time_interval/2)
    time.sleep(time_interval/2)
    
    light_pin(pin_num, time_interval/2)
    time.sleep(time_interval/2)
    
    light_pin(pin_num, time_interval/2)
    time.sleep(time_interval/2)
    
    time.sleep(5)
    
    light_pin(pin_num, time_interval/2)
    time.sleep(time_interval/2)
    
    light_pin(pin_num, time_interval/2)
    time.sleep(time_interval/2)
    
    light_pin(pin_num, time_interval/2)
    time.sleep(time_interval/2)
    
    light_pin(pin_num, time_interval/2)
    time.sleep(time_interval/2)
    
    time.sleep(2)
    
    
#=========================================

def main():
    # Set GPIO numbering mode to 
    GPIO.setmode(GPIO.BOARD)
    
    GPIO.setup(LED, GPIO.OUT)
    
    try :
        while 1:
            lights(LED, .3)

    except KeyboardInterrupt:
        print("Done")
    
    GPIO.cleanup()

#=========================================

main()










from machine import PWM,Pin,ADC
from time import sleep

# these variables assign the pins for the potentiometer
pot_pin = 28
pot_convert = ADC(pot_pin)

# these variables define the necessary values for the LED, from the appropriate pin to the frequency and PWM values
led_pin = 15
red_led = PWM(Pin(led_pin))
red_led.freq(1000)
red_led.duty_u16(0)

while True:
    # gathers value of potentiometer, assigns to pot_val variable in bits, then gets exponential value and assigns brightness value according to that
    pot_val = pot_convert.read_u16()
    exp_val = (16 / 65550) * pot_val
    bright_val = (2) ** exp_val

    # prints the values for the potentiometer, the exponential value, and the brightness value each on independent lines
    print("Potentiometer value: ", pot_val, "\nExponent value: ", exp_val, "\nBrightness value: ", bright_val, "\n")
    
    # assigns red_led value to whatever the brightness value is, which is an exponent of 2 to the power of the exp_val variable
    red_led.duty_u16(int(bright_val))

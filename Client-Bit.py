# Imports go at the top
from microbit import *
import radio
import math
import utime

radio.config(group=98, power=1)

radio.on()
id = 2
safe = True
timer = 0
run_timer = False
close_contact = False
list_people = set()
social_distant = True

# function to map signal stength to LED brightness (taken from microbit.org website)
def mapValues(value, fromMin, fromMax, toMin, toMax):
    fromRange = fromMax - fromMin
    toRange = toMax - toMin
    valueScaled = float(value - fromMin) / float(fromRange)
    return toMin + (valueScaled * toRange)

while True:
    if button_a.is_pressed():
        safe = not safe
        sleep(500)
    
    if safe and not close_contact and not run_timer and social_distant:
        radio.send(str(id) + ';' + str(list(list_people))[1:-1])
        display.show(Image("09999:"
                           "90000:"
                           "09990:"
                           "00009:"
                           "99990"))
    elif not safe and not run_timer and social_distant:
        
        radio.send(str(-id) + ';' + str(list(list_people))[1:-1])
        display.show(Image("90009:"
                           "90009:"
                           "90009:"
                           "09090:"
                           "00900"))
    elif close_contact and not run_timer and social_distant:
        ...
        display.show(Image("09999:"
                           "90000:"
                           "90000:"
                           "90000:"
                           "09999"))
    
    elif not social_distant:
        if safe:
            radio.send(str(id) + ';' + str(list(list_people))[1:-1])
        else:
            radio.send(str(-id) + ';' + str(list(list_people))[1:-1])
        display.show(Image("00900:"
                           "00900:"
                           "00900:"
                           "00000:"
                           "00900"))
    elif run_timer and timer <= 25:
        timer += 1
        display.show(timer)
        sleep(1000)
    
    if button_b.is_pressed() or timer >= 20:
        timer = 0
        run_timer = not run_timer
        sleep(500)

    received = radio.receive_full()
    message = radio.receive()
    
    try:
        signal = received[1]
        timestamp = received[2] // 1000
        sig_norm = mapValues(signal, -91, -27, 0, 1)
    except Exception as e:
        try:
            signal = signal
            timestamp = timestamp
            sig_norm = sig_norm
        except:
            signal = 0
            timestamp = 0
            sig_norm = 0
    
    curr_time = utime.ticks_ms()
    
    if received and message:
        message = message.split(';')[0]
        message = int(message)

        if not social_distant:
            try:
                list_people.remove(abs(message))
                list_people.add(message)
            except:
                list_people.add(message)

        # print(sig_norm)
                
        for i in list_people:
            if i < 0:
                close_contact = True

    if sig_norm < 0.05 or curr_time - timestamp > 2000:
        social_distant = True
    elif sig_norm > 0.15:
        social_distant = False
    
    print(list_people)
        
    
    
        

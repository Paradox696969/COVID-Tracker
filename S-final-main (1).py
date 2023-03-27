from microbit import *
import radio
import utime

radio.on()
dictIDs = {}
radio.config(group=98, power=1)

while True:
    
    try:
        message = radio.receive()
        prt_str = ''
        if isinstance(message, str):
            id, list = message.split(';')
            try:
                dictIDs[int(id)] = set(map(int, list.split(',')))
            except:
                dictIDs[int(id)] = set()
            try:
                prt_str = str(dictIDs)[1:-1]
                prt_str = prt_str.replace(',', ';')
                prt_str = prt_str.replace('{', '}')
                prt_str = prt_str.replace('}', ',')
            except Exception as e:
                print(e)
                prt_str = ''
    except:
        prt_str = ''

    
    print(prt_str)
    
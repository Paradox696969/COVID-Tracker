import serial
import json
import time

ser = serial.Serial()
ser.baudrate = 115200
ser.port = 'COM3'

ser.open()

while True:
    data = str(ser.readline().decode('utf8')).strip()
    list_data_unp = data.split(';')
    try:
        for l in range(len(list_data_unp)):
            list_data_unp[l] = list_data_unp[l].split(':')
            list_data_unp[l][0] = int(list_data_unp[l][0])
    except:
        ...
    try:
        if round(time.time()) % 10 == 0:
                try:
                    with open('data.json') as f:
                        dataDict = json.load(f)
                except:
                    dataDict = {}
                # print(dataDict)
                for i in list_data_unp:
                    if len(i) > 1:
                        try:
                            dataDict[str(abs(int(i[0])))] = list(set(dataDict[str(abs(int(i[0])))] + i[1].split(',')[1:-1]))
                        except KeyError:
                            dataDict[str(abs(int(i[0])))] = list(set(i[1].split(',')[1:-1]))
                tempDict = dataDict.copy()
                # print(dataDict)
                for key in tempDict:
                    if key not in ['CloseContacts', 'Infected']:
                        for i in tempDict[key]:
                            id = int(i)
                            if id < 0:
                                try:
                                    dataDict['CloseContacts'] = set(dataDict['CloseContacts'])
                                    dataDict['Infected'] = set(dataDict['Infected'])
                                    dataDict['CloseContacts'].add(key)
                                    dataDict['Infected'].add(str(id))
                                    dataDict['CloseContacts'] = list(dataDict['CloseContacts'])
                                    dataDict['Infected'] = list(dataDict['Infected'])
                                except Exception as e:
                                    print(e)
                                    dataDict['CloseContacts'] = list({key})
                                    dataDict['Infected'] = list({str(id)})
                                    ...
        with open('data.json', 'w') as f:
                json.dump(dataDict, f)
    except Exception as e:
        print(e)
        ...
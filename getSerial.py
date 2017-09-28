import serial, time

port = serial.Serial('COM3', 9600) #change the COM port
time.sleep(1.8)

wdt = time.time()

print 'runing'
while True:
    try:
        port.write('a')
        if (port.inWaiting() > 0):
            value = port.readline().decode("ascii")
            #print value

            with open("r.txt", 'w') as fl:
                fl.write(value)
                fl.close()

        else:
            if time.time() - wdt >= 10:
                wdt = time.time()
                port.write('a')
                print '..'

    except KeyboardInterrupt:
        print 'FIM'
        break

port.close()

from gpiozero import MotionSensor, LED, Buzzer                                                             

led = LED(17)                                                                                                  
buz = Buzzer(3)
pir = MotionSensor(4)
#  pir.wait_for_motion()
#  print("Motion detected!")
n = 0
while True:
    pir.wait_for_motion()
    n += 1
    # LED blink for 3 sec
    cnt = 0
    while cnt < 3:
        if cnt % 2 == 1:
            led.on()
        else:
            led.off()
        cnt += 1
        sleep(1)

    # Beep for 1 sec
    cnt = 0
    while cnt < 1:
        buz.on()
        cnt += 1
        sleep(1)
        buz.off()

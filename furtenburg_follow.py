
from pynput.mouse import Button, Controller as mouseController
from pynput.keyboard import Key, Controller as keyController
import time
import pyautogui
import random

for u in range(10):
    mouse = mouseController()
    keyboard = keyController()

    num3 = random.randint(3600,6000)
    #num3 = 1
    timespent = num3/60

    print("wait time =", timespent)

    time.sleep(num3)
    
    mouse.position = (1240, 377)
    mouse.click(Button.left, 2)
    time.sleep(1)
    mouse.position = (1240, 377)
    mouse.click(Button.left, 2)

    keyboard.press(Key.enter)
    keyboard.release(Key.enter)


    mouse.position = (208, 751)
    mouse.click(Button.left, 2)


    time.sleep(1)


    for char in "chrome":
        keyboard.press(char)
        keyboard.release(char)
        time.sleep(0.12)


    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

    time.sleep(5)


    mouse.position = (260, 60)
    mouse.click(Button.left, 1)

    for char in "https://www.instagram.com/furtenburg_inc/":
        keyboard.press(char)
        keyboard.release(char)
        time.sleep(0.12)

    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

    time.sleep(8)




    mouse.position = (824, 222)
    mouse.click(Button.left, 1)


    time.sleep(2)

    num11 = random.randint(50,100)
    mouse.position = (875, 591)
    for i in range(num11):
        mouse.click(Button.left, 1)
        time.sleep(0.2)

    o = 805
    p = 310   
    num10 = random.randint(20,50)
    print("unfollowed =", num10)
    for x in range(num10):
        

        
        time.sleep(3)
        mouse.position = (o, p)
        mouse.click(Button.left, 1)    
        
        p += 2

        time.sleep(2)

        mouse.position = (683, 479)
        mouse.click(Button.left, 1)

        time.sleep(3)

        mouse.position = (875, 591)

        for i in range(6):
            mouse.click(Button.left, 1)
            time.sleep(0.15)



    mouse.position = (1341, 13)
    mouse.click(Button.left, 1)




    mouse = mouseController()
    keyboard = keyController()


    mouse.position = (192, 753)
    mouse.click(Button.left, 2)


    time.sleep(1)


    for char in "chrome":
        keyboard.press(char)
        keyboard.release(char)
        time.sleep(0.12)


    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

    time.sleep(5)


    mouse.position = (227, 46)
    mouse.click(Button.left, 1)

    num1 = random.randint(1,20)
    num2 = random.randint(300, 700)

    path0 = ""
    mp = (0, 0)
    path1 = "https://www.instagram.com/p/CLng8wNpRjJ/"
    path2 = "https://www.instagram.com/p/CLhG-hzp9Pj/"
    path3 = "https://www.instagram.com/p/CLfYcvkAt1w/"
    path4 = "https://www.instagram.com/p/CLiIpKLpIO4/"
    path5 = "https://www.instagram.com/p/CLZKtvwHpe2/"
    path6 = "https://www.instagram.com/p/CLmiKYmIx8c/" 
    path7 = "https://www.instagram.com/p/CLnGYbuD02u/"
    path8 = "https://www.instagram.com/p/CLc1YxRneKV/"
    path9 = "https://www.instagram.com/p/CLW72_WBwEy/" 
    path10 = "https://www.instagram.com/p/CLzMaueHxvd/"
    path11 = "https://www.instagram.com/p/CLkE8V6npkJ/"
    path12 = "https://www.instagram.com/p/CL4PG-pqudn/"
    path13 = "https://www.instagram.com/p/CL36gnbBk8r/"
    path14 = "https://www.instagram.com/p/CL1bPP_H8qJ/"
    path15 = "https://www.instagram.com/p/CL3E_ZppIOG/"
    path16 = "https://www.instagram.com/p/CL2BpHPnaXX/"
    path17 = "https://www.instagram.com/p/CL1u7M1prZU/"
    path18 = "https://www.instagram.com/p/CL0W5wtn8Bd/"
    path19 = "https://www.instagram.com/p/CLc-WdGg32w/"
    path20 = "https://www.instagram.com/p/CLCZm9fgbh8/"

    print("option out of 20 = ", num1)
    print("scroll distance = ", num2)
    if num1 == 1:
        path0 = path1
        mp = (774, 650)
    if num1 == 2:
        path0 = path2
        mp = (776, 651)
    if num1 == 3:
        path0 = path3
        mp = (836, 647)
    if num1 == 4:
        path0 = path4
        mp = (830, 610)
    if num1 == 5:
        path0 = path5
        mp = (829, 650)
    if num1 == 6:
        path0 = path6
        mp = (827, 651)
    if num1 == 7:
        path0 = path7
        mp = (825, 654)
    if num1 == 8:
        path0 = path8
        mp = (828, 640)
    if num1 == 9:
        path0 = path9
        mp = (710, 648)
    if num1 == 10:
        path0 = path10
        mp = (789, 652)
    if num1 == 11:
        path0 = path11
        mp = (834, 654)
    if num1 == 12:
        path0 = path12
        mp = (837, 651)
    if num1 == 13:
        path0 = path13
        mp = (830, 652)
    if num1 == 14:
        path0 = path14
        mp = (769, 653)
    if num1 == 15:
        path0 = path15
        mp = (778, 648)
    if num1 == 16:
        path0 = path16
        mp = (829, 655)
    if num1 == 17:
        path0 = path17
        mp = (777, 650)
    if num1 == 18:
        path0 = path18
        mp = (832, 653)
    if num1 == 19:
        path0 = path19
        mp = (828, 652)
    if num1 == 20:
        path0 = path20
        mp = (830, 653)



    for char in path0:
        keyboard.press(char)
        keyboard.release(char)
        time.sleep(0.12)

    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

    time.sleep(9)

    mouse.position = mp
    mouse.click(Button.left, 1)
    time.sleep(6)

        
    scrollspeed = random.randint(0.2, 0.8)
    mouse.position = (872, 590)
    for i in range(num2):
        mouse.click(Button.left, 1)
        time.sleep(scrollspeed)

    o = 815
    p = 271 

    follow = random.randint(15, 30)
    print("followed =", follow)
    for x in range(follow):
        
        time.sleep(1)
        
        
        mouse.position = (o, p)
        mouse.click(Button.left, 1)  
        time.sleep(0.3142)
        mouse.position = (o, p+50)
        mouse.click(Button.left, 1)     
        time.sleep(0.332)
        mouse.position = (o, p+50)
        mouse.click(Button.left, 1)
        time.sleep(0.345)
        mouse.position = (o, p+50)
        mouse.click(Button.left, 1)

        
        p += 2

        time.sleep(1)



        mouse.position = (872, 590)

        time.sleep(1)


        for i in range(6):
            mouse.click(Button.left, 1)
            time.sleep(0.2)

    

    mouse.position = (1340, 12)
    mouse.click(Button.left, 1)
    





  
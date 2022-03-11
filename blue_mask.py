from pynput.mouse import Button, Controller as mouseController
from pynput.keyboard import Key, Controller as keyController
import time
import pyautogui
import random
import cv2
import numpy as np
from PIL import Image
import imutils

for u in range(1):
    mouse = mouseController()
    keyboard = keyController()

    num3 = random.randint(3600,5400)
    #num3 = 1
    timespent = num3/60
    print("wait time =", timespent)
    
    


    #print("wait time =", timespent/60)
    timespent = 0
    time.sleep(timespent)
    
    # # mouse.position = (117, 1057)
    # # mouse.click(Button.left, 1)

    # # time.sleep(2)
   
    # # for char in "chrome":
    # #     keyboard.press(char)
    # #     keyboard.release(char)
    # #     time.sleep(0.12)
    

    # keyboard.press(Key.enter)
    # keyboard.release(Key.enter)

    # time.sleep(5)

    # mouse.position = (237, 60)
    # mouse.click(Button.left, 2)
    # time.sleep(random.randint(2,4))


    #time.sleep(2)
    #ray1 = random.randint(10,20)

    # for char in "https://www.instagram.com/techtyrant":
    #     keyboard.press(char)
    #     keyboard.release(char)
    #     ray1 = random.randint(10,20)
    #     time.sleep(ray1/100)


    # keyboard.press(Key.enter)
    # keyboard.release(Key.enter)

    # time.sleep(random.randint(10,13))


    # mouse.position = (1117, 238)
    # mouse.click(Button.left, 1)


    # time.sleep(random.randint(2,4))
    # total = 0
    # unfollowed = 0
    # # #num11 = random.randint(100,200) 
    # num11 = random.randint(10,30)   #####################################
    # mouse.position = (1150, 746)
    # for i in range(num11):
    #     mouse.click(Button.left, 1)
    #     scroll = random.randint(20,30)
    #     time.sleep(scroll/100)
    
        
    # #cv2.imshow("Screenshot", imutils.resize(image, width=600))
    
    # o = 1087
    # p = 461   
    # num10 = random.randint(4,5)
    # # print("unfollowed =", num10)
    # #for x in range(num10):
    # while(total<16):
    #     unfollowed = 0
        
    #     time.sleep(random.randint(1,2))
    #     mouse.position = (o, p)
    #     mouse.click(Button.left, 1)
    #     time.sleep(random.randint(1,2))

    #     mouse.position = (959, 640)
    #     mouse.click(Button.left, 1)
    #     time.sleep(random.randint(1,2))

    #     mouse.position = (o, p+50)
    #     mouse.click(Button.left, 1)
    #     time.sleep(random.randint(1,2))

    #     mouse.position = (959, 640)
    #     mouse.click(Button.left, 1)
    #     time.sleep(random.randint(1,2))

    #     mouse.position = (o, p+80)
    #     mouse.click(Button.left, 1)
    #     time.sleep(random.randint(1,2))

    #     mouse.position = (959, 640)
    #     mouse.click(Button.left, 1)
    #     time.sleep(random.randint(1,2))

    #     mouse.position = (o, p+145)
    #     mouse.click(Button.left, 1)
    #     time.sleep(random.randint(1,2))

    #     mouse.position = (959, 640)
    #     mouse.click(Button.left, 1)
    #     time.sleep(random.randint(1,2))

    #     mouse.position = (o, 654)
    #     mouse.click(Button.left, 1)
    #     time.sleep(random.randint(1,2))

    #     mouse.position = (959, 640)
    #     mouse.click(Button.left, 1)
    #     time.sleep(random.randint(1,2))

    #     mouse.position = (o, 711)
    #     mouse.click(Button.left, 1)
    #     time.sleep(random.randint(1,2))

    #     mouse.position = (959, 640)
    #     mouse.click(Button.left, 1)

    #     time.sleep(random.randint(2,3))

    #     mouse.position = (1150, 746)

    #     pyautogui.screenshot("Desktop/soft/blue.png", region=(1000, 440, 135, 320))
    #     img = cv2.imread("Desktop/soft/blue.png")
    #     hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    #     lower_range = np.array([50,50,50])
    #     upper_range = np.array([130,255,255])

    #     mask = cv2.inRange(hsv, lower_range, upper_range)
    #     number_w = np.sum(mask == 255)
    #     number_b = np.sum(mask == 0)
    #     cv2.imshow('image', img)
    #     cv2.imshow('mask', mask)
    #     # print('Number of white pixels:', number_w)
    #     # print('Number of black pixels:', number_b)

    #     if(1650 < number_w < 1800):
    #         unfollowed = 1
    #     if(1800 < number_w < 3600):
    #         unfollowed = 2
    #     if(3600 < number_w < 5300):
    #         unfollowed = 3
    #     if(5300 < number_w < 7100):
    #         unfollowed = 4
    #     if(7100 < number_w < 9000):
    #         unfollowed = 5
    #     if(9000 < number_w < 11000):
    #         unfollowed = 6
    #     if(11900 < number_w < 15000):
    #         unfollowed = 7

    #     total = total + unfollowed
        
    #     print("unfollowed",unfollowed)
    #     print("totalu",total)

    #     for i in range(10):
    #         mouse.click(Button.left, 1)
    #         scroll = (random.randint(20,30))
    #         time.sleep(scroll/100)

    # print("totalll",total)

    # cv2.waitKey(0)

    # mouse.position = (1133, 375)
    # mouse.click(Button.left, 1)

    # time.sleep(random.randint(2,3))



    # ###############################################################################################
    # # mouse = mouseController()
    # # keyboard = keyController()



    # # mouse.position = (1316, 100)
    # # mouse.click(Button.left, 2)

    # # time.sleep(random.randint(2,3))


    # # mouse.position = (1913, 1070)
    # # mouse.click(Button.left, 2)
    # # time.sleep(random.randint(2,3))

    # # for i in range(random.randint(0,10)):
    # #     mouse.click(Button.left, 1)
    # #     time.sleep(0.15)

    # # # time.sleep(1)

    # # time.sleep(random.randint(2,3))
    

    # # mouse.position = ((628, 310))
    # # mouse.click(Button.left, 1)

    # # time.sleep(random.randint(2,3))


    # # im22 = pyautogui.screenshot(region=(0, 0, 1920, 1080))
    # # im22.save(r"Desktop\soft\screen1.png")         
    # # #path11 = ("Desktop\soft\screen1.png")

    # # path11 = cv2.imread("Desktop\soft\screen1.png")

    # # boundaries = [
	# # ([200, 200, 200], [255, 255, 255])
    # # ]           

    # # time.sleep(random.randint(2,3))

    # # for (lower, upper) in boundaries:
    # #     # create NumPy arrays from the boundaries
    # #     lower = np.array(lower, dtype = "uint8")
    # #     upper = np.array(upper, dtype = "uint8")
    # #     # find the colors within the specified boundaries and apply
    # #     # the mask
    # #     mask = cv2.inRange(path11, lower, upper)
    # #     output = cv2.bitwise_and(path11, path11, mask = mask)
    # #     # show the images
    # #     #cv2.imshow("images", np.hstack([path11, output]))
    # #     cv2.imshow('original',path11)
    # #     cv2.imshow('mask',output)
    # #     cv2.waitKey(0)

    # ###############################################################################################
    # # mouse.position = (1896, 14)
    # # mouse.click(Button.left, 1)

    # # time.sleep(3)

    # # mouse.position = (117, 1057)
    # # mouse.click(Button.left, 1)

    # # time.sleep(3)
   
    # # for char in "chrome":
    # #     keyboard.press(char)
    # #     keyboard.release(char)
    # #     time.sleep(0.12)


    # keyboard.press(Key.enter)
    # keyboard.release(Key.enter)

    # time.sleep(5)


    mouse.position = (179, 50)
    mouse.click(Button.left, 1)

    num1 = random.randint(1,20)
    num2 = random.randint(200, 400)

    path0 = ""
    mp = (0, 0)
    path1 = "https://www.instagram.com/p/CZbMOsvosGj/"
    path2 = "https://www.instagram.com/p/CZeY0ZQtxBN/"
    path3 = "https://www.instagram.com/p/CZhKOHoI_-Q/"
    path4 = "https://www.instagram.com/p/CZe3vO_LY15/"
    path5 = "https://www.instagram.com/p/CZmZBtWPSDY/"
    path6 = "https://www.instagram.com/p/CZhXjW2rDJW/" 
    path7 = "https://www.instagram.com/p/CZe3-reBf4m/"
    path8 = "https://www.instagram.com/p/CZWYYTMLqPq/"
    path9 = "https://www.instagram.com/p/CZjJRiwgZvC/" 
    path10 = "https://www.instagram.com/p/CZeSTTeDuND/"
    path11 = "https://www.instagram.com/p/CZYTdujpUIs/"
    path12 = "https://www.instagram.com/p/CZWqoXqN4I4/"
    path13 = "https://www.instagram.com/p/CZkAa7yAc8Z/"
    path14 = "https://www.instagram.com/p/CZgVm4Vr_hh/"
    path15 = "https://www.instagram.com/p/CZqmbQdAibY/"
    path16 = "https://www.instagram.com/p/CZeHVGxpUkF/"
    path17 = "https://www.instagram.com/p/CZj9jpjJgQd/"
    path18 = "https://www.instagram.com/p/CZgGCRxrCKz/"
    path19 = "https://www.instagram.com/p/CZg2dkTAmJg/"
    path20 = "https://www.instagram.com/p/CZgM4auDfTK/"

    print("option out of 20 = ", num1)
    print("scroll distance = ", num2)
    if num1 == 1:
        path0 = path1
        mp = (988, 668)
    if num1 == 2:
        path0 = path2
        mp = (1056, 669)
    if num1 == 3:
        path0 = path3
        mp = (1117, 663)
    if num1 == 4:
        path0 = path4
        mp = (1112, 665)
    if num1 == 5:
        path0 = path5
        mp = (1125, 665)
    if num1 == 6:
        path0 = path6
        mp = (1060, 667)
    if num1 == 7:
        path0 = path7
        mp = (997, 663)
    if num1 == 8:
        path0 = path8
        mp = (1054, 666)
    if num1 == 9:
        path0 = path9
        mp = (1062, 669)
    if num1 == 10:
        path0 = path10
        mp = (1129, 666)
    if num1 == 11:
        path0 = path11
        mp = (1120, 664)
    if num1 == 12:
        path0 = path12
        mp = (1111, 653)
    if num1 == 13:
        path0 = path13
        mp = (1058, 651)
    if num1 == 14:
        path0 = path14
        mp = (1118, 667)
    if num1 == 15:
        path0 = path15
        mp = (1053, 664)
    if num1 == 16:
        path0 = path16
        mp = (1118, 669)
    if num1 == 17:
        path0 = path17
        mp = (1125, 536)
    if num1 == 18:
        path0 = path18
        mp = (1076, 652)
    if num1 == 19:
        path0 = path19
        mp = (1059, 650)
    if num1 == 20:
        path0 = path20
        mp = (1052, 664)



    for char in path0:
        keyboard.press(char)
        keyboard.release(char)
        time.sleep(0.12)

    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

    time.sleep(random.randint(9,11))

    mouse.position = mp
    mouse.click(Button.left, 1)
    time.sleep(6)

    total = 0
    # unfollowed = 0

    #num11 = random.randint(num2)   
    num11 = random.randint(100,200)    ##############
    mouse.position = (1150, 746)
    for i in range(num11):
        mouse.click(Button.left, 1)
        scroll = (random.randint(20,30))
        time.sleep(scroll/100)
    
    o = 1087
    p = 461   
    num10 = random.randint(3,5)
    #print("followed =", num10)
    # #for x in range(num10):
    while(total<16):
    
        unfollowed = 0
         
        time.sleep(1)
        mouse.position = (o, p)
        mouse.click(Button.left, 1)
        time.sleep(1)

        mouse.position = (o, p+50)
        mouse.click(Button.left, 1)
        time.sleep(1)

        mouse.position = (o, p+80)
        mouse.click(Button.left, 1)
        time.sleep(1)

        mouse.position = (o, p+145)
        mouse.click(Button.left, 1)
        time.sleep(1)

        mouse.position = (o, 654)
        mouse.click(Button.left, 1)
        time.sleep(1)

        mouse.position = (o, 711)
        mouse.click(Button.left, 1)
        time.sleep(1)

        mouse.position = (1150, 746)

        pyautogui.screenshot("Desktop/soft/blue.png", region=(1000, 400, 135, 360))
        img = cv2.imread("Desktop/soft/blue.png")
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

        lower_range = np.array([50,50,50])
        upper_range = np.array([130,255,255])

        mask = cv2.inRange(hsv, lower_range, upper_range)
        number_w = np.sum(mask == 255)
        number_b = np.sum(mask == 0)
        cv2.imshow('image', img)
        cv2.imshow('mask', mask)
        print('Number of white pixels:', number_w)
        print('Number of black pixels:', number_b)

        if(49000 > number_b > 47500):
            unfollowed = 6
        if(47500 > number_b > 45900):
            unfollowed = 5
        if(45900 > number_b > 44000):
            unfollowed = 4
        if(44000 > number_b > 42000):
            unfollowed = 3
        if(42000 > number_b > 40000):
            unfollowed = 2
        if(40000 > number_b > 38214):
            unfollowed = 1
        if(38214 > number_b > 40000):
            unfollowed = 0
    

        total = total + unfollowed
        
        print("followed",unfollowed)
        print("totalf",total)
        #cv2.waitKey(0)

        for i in range(10):
            mouse.click(Button.left, 1)
            time.sleep(0.15)

    print("totallf",total)
    cv2.waitKey(0)

    # mouse.position = (1895, 10)
    # mouse.click(Button.left, 1)
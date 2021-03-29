


import time
import pyautogui
import random
import sys
from PIL import Image
import pytesseract
import numpy as np 


pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

#im2 = pyautogui.screenshot('screen.png')

im2 = pyautogui.screenshot(region=(900, 200, 300, 50))

im2.save(r"C:\Users\User\Desktop\scripts\screen\screen.png")

path1 = 'Desktop\scripts\screen\screen.png'

def parse_k(string):
    if 'k' in string:
        val = int(string.split('k')[0])
        val *= 1000
        return val
    if ',' in string:
        return int(string.replace(',', ''))
    else:
        return int(string)


def calculate_ratio(following, followers):
    print(following, followers)
    ratio = following/followers
    print(ratio)
    if ratio > 1.5:
        print("follow")
        print("like")
    elif ratio > .75:
        if following > 500:
            print("follow")
        else:
            print("like")
    else:
        if followers < 100:
            print("follow")
        else:
            return False


def ocr_core(filename):
  
    text = pytesseract.image_to_string(Image.open(filename)) 
    return text

whole = (ocr_core(path1))
print(whole)

w1 = whole.split('following')[0]
followers,following = w1.split('followers')



followers = parse_k(followers)
following = parse_k(following)
#print(followers,following)

calculate_ratio(following, followers)
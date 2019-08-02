from PIL import ImageGrab, ImageOps
import pyautogui
import time
import numpy as np

class Coordinates():
    replayBtn=(479,456)
    dinosaur=(187,472)


def restartGame():
    pyautogui.click(Coordinates.replayBtn)
    pyautogui.keyDown('down')

def pressSpace():
    pyautogui.keyUp('down')
    pyautogui.keyDown('space')
    time.sleep(0.18)
    pyautogui.keyUp('space')
    pyautogui.keyDown('down')

def imageGrabtree():
    box=(Coordinates.dinosaur[0]+28 ,Coordinates.dinosaur[1]+13,Coordinates.dinosaur[0]+120   ,Coordinates.dinosaur[1]+37)
    image=ImageGrab.grab(box) 
    grayImage=ImageOps.grayscale(image)
    a= np.array(grayImage.getcolors())                                                     
    print(a.sum())
    return a.sum()
           
if __name__ == "__main__":
    restartGame()
    while True:
        if(imageGrabTree()!=6325):
            pressSpace()   
            time.sleep(0.1)

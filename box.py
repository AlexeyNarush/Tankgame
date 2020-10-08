import settings
import random

# Main class 
# Global parameters of the boxes 
class Box:
    def __init__(self, x, y, img):
        self.X = x
        self.Y = y 
        self.img = img
        self.hp = 1
        self.collis = 0  
    def destroy(self):
        self.hp += 1
        if self.hp == 4:
            return True
        self.img = eval("settings.box" + str(self.hp) + "Img")
        return False

# Sequence that generates the ammount of boxes and choose there possitions 
# Ammount of boxes picked randomly from 70 to 100 
# Position of the boxes are random exept for the plases where players starts 
def createBoxes():
    number = random.randint(70, 100)
    map = []
    boxes = []
    for i in range(number):
        x = random.randint (0, 11) * settings.block
        y = random.randint (0, 11) * settings.block
        while (x , y) == (0 , 0) or (x, y) == (settings.width - settings.block, settings.height - settings.block) or (x, y) in map:
            x = random.randint (0, 11) * settings.block
            y = random.randint (0, 11) * settings.block
        map.append((x, y))
        boxes.append(Box(x, y, settings.box1Img))
    return boxes 

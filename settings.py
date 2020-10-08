import pygame

# Settings of the screen
height = 600
width = 600
FPS = 60

# Greed block settings
H = height // 12
W = width // 12
block = height // 12

# Parameters of the tank1
tank1 = './img/tank1.png'
t1Img = pygame.image.load(tank1)
t1Img = pygame.transform.scale(t1Img, (W, H))
t1Img = pygame.transform.rotate(t1Img, 180)

# Parameters of the tank2
tank2 = './img/tank2.png'
t2Img = pygame.image.load(tank2)
t2Img = pygame.transform.scale(t2Img, (W, H))

# Parameters of the box before it was hit
box1 =  './img/Box1.png'
box1Img = pygame.image.load(box1)
box1Img = pygame.transform.scale(box1Img, (W, H))

# Parameters of the box after it was hit one time
box2 =  './img/Box2.png'
box2Img = pygame.image.load(box2)
box2Img = pygame.transform.scale(box2Img, (W, H))

# Parameters of the box after it was hit two times
box3 =  './img/Box3.png'
box3Img = pygame.image.load(box3)
box3Img = pygame.transform.scale(box3Img, (W, H))

# Parameters of the HP representating image
heart =  './img/heart.png'
heartImg = pygame.image.load(heart)
heartImg = pygame.transform.scale(heartImg, (30, 30))

# Parameters of the tank images
t1Icon = pygame.transform.scale(t1Img, (34, 34))
t2Icon = pygame.transform.scale(t2Img, (34, 34))


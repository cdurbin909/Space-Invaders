import pygame
import random
import math

# initialize pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 600))

# load the background image
bg = pygame.image.load("background.jpg")

# Title and Icon
pygame.display.set_caption("Pygame Practice Window")
icon = pygame.image.load('Controller.png')
pygame.display.set_icon(icon)

# Player
PlayerImg = pygame.image.load('battleship.png')
playerX = 370
playerY = 480
playerXchange = 0

# Enemy
EnemyImg = []
enemyX = []
enemyY = []
enemyXchange = []
enemyYchange = []
numEnemies = 6
for i in range(numEnemies):
    EnemyImg.append(pygame.image.load('ufo.png'))
    enemyX.append(random.randint(0, 768))
    enemyY.append(0)
    enemyXchange.append(0.4)
    enemyYchange.append(0.2)

# Bullet
bulletImg = pygame.image.load('laser.png')
bulletX = random.randint(0, 768)
bulletY = 480
bulletXchange = 0
bulletYchange = 2
bulletState = "ready"

score = 0


# function that shows the player
def player(x, y):
    screen.blit(PlayerImg, (x, y))


# function that shows the enemy
def enemy(x, y, z):
    screen.blit(EnemyImg[z], (x, y))


# function that shows the background
def background():
    screen.blit(bg, (0, 0))


def fireBullet(x, y):
    global bulletState
    bulletState = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))


def isCollision(eX, eY, bX, bY):
    distance = math.sqrt((math.pow(eX - bX, 2)) + (math.pow(eY - bY, 2)))
    if distance < 27:
        return True
    else:
        return False

    # Game Loop


running = True
while running:
    screen.fill((0, 0, 0))
    background()

    # gets the keypresses
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                playerXchange = -.75
            if event.key == pygame.K_d:
                playerXchange = .75
            if event.key == pygame.K_SPACE and bulletState == "ready":
                bulletX = playerX
                fireBullet(bulletX, bulletY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or pygame.K_d:
                if event.key != pygame.K_SPACE:
                    playerXchange = 0

    # adds the player and enemy changes to their position
    playerX += playerXchange

    # boundaries for the player and enemies
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    # Enemy movement
    for i in range(numEnemies):
        enemyX[i] += enemyXchange[i]
        enemyY[i] += enemyYchange[i]
        if enemyX[i] <= 0:
            enemyXchange[i] *= -1
        elif enemyX[i] >= 768:
            enemyXchange[i] *= -1

        # Collision
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            bulletY = 480
            bulletState = "ready"
            score += 10
            print(score)
            enemyX[i] = random.randint(0, 768)
            enemyY[i] = 0

        enemy(enemyX[i], enemyY[i], i)

    # bullet movement
    if bulletState == "fire":
        fireBullet(bulletX, bulletY)
        bulletY -= bulletYchange
        if bulletY <= 0:
            bulletState = "ready"
            bulletY = 480

    # shows the player and enemy using the functions from earlier
    player(playerX, playerY)
    pygame.display.update()

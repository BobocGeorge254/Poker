import pygame
import random
import time


f = [0] * 100
#Random card
def RandomCard():
    card = random.randint(1,13)
    sign = random.randint(1,4)
    if f[sign * 13 + card] == 0 :
        f[sign * 13 + card] = 1
        if card == 1 :
            card = 'A'
        elif card == 11 :
            card = 'J'
        elif card == 12 :
            card = 'Q'
        elif card == 13 :
            card = 'K'
        elif card == 10 :
            card = '10'
        else :
            card = card + 48
            card = chr(card)

        if sign == 1 :
            sign = "Frunza"
        elif sign == 2 :
            sign = "Inima"
        elif sign == 3 :
            sign = "Trefla"
        else :
            sign = "Romb"
        time.sleep(1)
        return card + " " + sign
    else :
        return False

#Initialization
pygame.init()
screen = pygame.display.set_mode((860,700))
background = pygame.image.load("background.jpg")


#Title and icon
pygame.display.set_caption("Bubo Poker Casino Royal")
icon = pygame.image.load("poker-cards.png")
pygame.display.set_icon(icon)

#Draw a card
def card(cardImg, dim_x, dim_y):
    screen.blit(cardImg,(dim_x,dim_y))


#Give cards
def player(dx,dy):
    x = RandomCard()
    while x == False :
        x = RandomCard()
    nume_carte = x + ".png"
    cardImg = pygame.image.load(nume_carte)
    card(cardImg, dx, dy)
    pygame.display.update()
    x = RandomCard()
    while x == False:
        x = RandomCard()
    nume_carte = x + ".png"
    cardImg = pygame.image.load(nume_carte)
    card(cardImg, dx + 120, dy)
    pygame.display.update()

#Give flop
def flop(dx,dy) :
    x = RandomCard()
    while x == False:
        x = RandomCard()
    nume_carte = x + ".png"
    cardImg = pygame.image.load(nume_carte)
    card(cardImg, dx, dy)
    pygame.display.update()
    x = RandomCard()
    while x == False:
        x = RandomCard()
    nume_carte = x + ".png"
    cardImg = pygame.image.load(nume_carte)
    card(cardImg, dx + 120, dy)
    pygame.display.update()
    x = RandomCard()
    while x == False:
        x = RandomCard()
    nume_carte = x + ".png"
    cardImg = pygame.image.load(nume_carte)
    card(cardImg, dx + 240, dy)
    pygame.display.update()
    x = RandomCard()
    while x == False:
        x = RandomCard()
    nume_carte = x + ".png"
    cardImg = pygame.image.load(nume_carte)
    card(cardImg, dx + 360, dy)
    pygame.display.update()
    x = RandomCard()
    while x == False:
        x = RandomCard()
    nume_carte = x + ".png"
    cardImg = pygame.image.load(nume_carte)
    card(cardImg, dx + 480, dy)
    pygame.display.update()


font = pygame.font.Font('freesansbold.ttf',32)
def show_name(nume,dx,dy):
    player = font.render(nume, True, (255,255,255))
    screen.blit(player,(dx,dy))

#Looping of the game
running = True
generate = False
while running :
    screen.fill((16,16,16))
    show_name("Grogo",85,10)
    show_name("Mihai", 640, 10)
    show_name("Vixneju", 85, 655)
    show_name("Bubo", 640, 655)
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            running = False
    time.sleep(1)
    if generate == False :
        player(50,50)
        player(600,50)
        player(50,500)
        player(600,500)
        flop(125, 275)
        generate = True
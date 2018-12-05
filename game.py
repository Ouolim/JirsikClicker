import random, pygame, sys
from usefulThings import *
from pygame.locals import *

def rot_center(image, angle):
    """rotate an image while keeping its center and size"""
    orig_rect = image.get_rect()
    rot_image = pygame.transform.rotate(image, angle)
    rot_rect = orig_rect.copy()
    rot_rect.center = rot_image.get_rect().center
    rot_image = rot_image.subsurface(rot_rect).copy()
    return rot_image
def otoceni():
    """i have a special function for image rotate because of easy change"""
    global Uhel
    Uhel += 1
    if Uhel == 360: Uhel = 0
    return Uhel
def sprav_postup():
    """If a score has less items for buyables, this adds fixes the list"""
    global postup
    for i1 in range(1, 3):
        for i in range(postup[i1]+1):
            if len(postup) <= 2*i+3:
                postup.append(0)
                postup.append(0)
def jenaJirsovi(x, y):
    """A function that tells if mouse is over the image or not"""
    global WINDOWWIDTH, WINDOWHEIGHT, imageweight, imageheight

    leftcornerx = x > WINDOWWIDTH / 2 - imageweight / 2
    leftcornery = y > WINDOWHEIGHT / 2 - imageheight / 2
    rightcornerx = x < WINDOWWIDTH / 2 + imageweight / 2
    rightcornery = y < WINDOWHEIGHT / 2 + imageheight / 2
    if leftcornerx and leftcornery and rightcornerx and rightcornery:
        return 1
    else:
        return 0
def jenaBoxu(x, y):
  if x >= 0 and x <=300 and y >= 50:
      return "left"
  if x >= 600 and x <=900 and y >= 50:
      return "right"
  else:
      return 0
def vykresli(postup):
    obrazovka.fill(BGCOLOR)
    pygame.draw.line(obrazovka, LineColor, (300, 0), (300, 600), LineWidth)
    pygame.draw.line(obrazovka, LineColor, (600, 0), (600, 600), LineWidth)
    pygame.draw.line(obrazovka, LineColor, (0, 50), (900, 50), LineWidth)
    obrazovka.blit(TextClicker, ObdelnikClicker)
    obrazovka.blit(TextShop, ObdelnikShop)
    ObdelnikSpaseni = TextSpaseni.get_rect()
    ObdelnikSpaseni.center = (450, WINDOWHEIGHT - 30)
    obrazovka.blit(TextSpaseni, ObdelnikSpaseni)
    obrazovka.blit(TextSin, ObdelnikSin)
    obrazovka.blit(hlavy[otoceni()], (WINDOWWIDTH / 2 - imageweight / 2, WINDOWHEIGHT / 2 - imageweight / 2))
    obrazovka.blit(TextSPS, ObdelnikSPS)
    vykreslishop() #TODO: Zpřehlednit ASAP
    vykresliclicker() #TODO: Zpřehlednit ASAP
    pygame.display.update()
def vykresliclicker():
    global boxyClicker
    ObdelnikKup = TextKup.get_rect()
    sirkaboxu = 550/postup[1]
    boxu = postup[1]

    if boxyClicker == []:
        for i in range(boxu):
            boxyClicker.append((15, i * sirkaboxu + 95, 15 + ObdelnikKup.width, i * sirkaboxu + 95 + sirkaboxu - 54))

    for i in range(boxu):
        pygame.draw.line(obrazovka, LineColor, (0, i * sirkaboxu + 50), (300, i * sirkaboxu + 50), LineWidth)
        TextvClicker = fontObj.render(JmenaClickeru[i], True, TextColor, BGCOLOR)
        ObdelnikTextvClicker = TextvClicker.get_rect()
        ObdelnikTextvClicker.topleft = (10,  i * sirkaboxu + 60)
        obrazovka.blit(TextvClicker, ObdelnikTextvClicker)
        pygame.draw.rect(obrazovka, ButtonsColor, (15,  i * sirkaboxu + 95, ObdelnikKup.width, sirkaboxu-54),0)

        ObdelnikKup.center = ((30 + ObdelnikKup.width)/2, (i * sirkaboxu + 95 + i * sirkaboxu + 95 + sirkaboxu - 53)/2)
        obrazovka.blit(TextKup, ObdelnikKup)
def vykreslishop():
    global boxyShop, TextKup
    boxyShop = []
    boxyClicker = []
    sirkaboxu = 550/postup[2]
    boxu = postup[2]
    ObdelnikKup = TextKup.get_rect()
    if boxyShop==[]:
        for i in range(boxu):

            boxyShop.append((600 + 15, i * sirkaboxu + 95, ObdelnikKup.width + 600 + 15, sirkaboxu - 54 + i * sirkaboxu + 95))

    for i in range(boxu):

        pygame.draw.line(obrazovka, LineColor, (600, i * sirkaboxu + 50), (900, i * sirkaboxu + 50), LineWidth)
        TextvShopu = fontObj.render(JmenaShopu[i], True, TextColor, BGCOLOR)
        ObdelnikTextvShop = TextvShopu.get_rect()
        ObdelnikTextvShop.topleft = (610,  i * sirkaboxu + 55)
        obrazovka.blit(TextvShopu, ObdelnikTextvShop)

        ObdelnikKup = TextKup.get_rect()
        if CenyShopu[i]>postup[0]: barva=UnbuyableButtonsColor
        else: barva=ButtonsColor
        pygame.draw.rect(obrazovka, barva, (600 + 15, i * sirkaboxu + 95, ObdelnikKup.width, sirkaboxu - 54), 0)

        TextKup = fontObj.render("Kup!", True, TextColor, barva)
        ObdelnikKup = TextKup.get_rect()
        ObdelnikKup.center = (600 + (30 + ObdelnikKup.width) / 2, (i * sirkaboxu + 95 + i * sirkaboxu + 95 + sirkaboxu - 53) / 2)
        obrazovka.blit(TextKup, ObdelnikKup)

        Cena=CenyShopu[i]
        Ucinnost=UcinostShopu[i]
        TextCena = fontCena.render(("Cena je " + str(round(Cena, 2))), True, TextColor, BGCOLOR)
        TextUcinnost = fontCena.render(("+" + str(round(Ucinnost, 2)) + " Spasení za vteřinu"), True, TextColor, BGCOLOR)
        ObdelnikCena = TextCena.get_rect()
        ObdelnikUcinnost = TextUcinnost.get_rect()
        ObdelnikCena.topright = (890,  i * sirkaboxu + 60)
        ObdelnikUcinnost.topright = (890, i * sirkaboxu + 90)
        obrazovka.blit(TextCena, ObdelnikCena)
        obrazovka.blit(TextUcinnost, ObdelnikUcinnost)
def nactisoubor():
    global postup
    try:
        f = open("save.txt", "r")
        soubor = f.readlines()
        for index in range(len(soubor)):
            postup.append(int(soubor[index]))
        f.close()
    except FileNotFoundError:
        postup = [0, 1, 1]

    try:
        postup[2] = postup[2]
    except IndexError:
        # print("Neco se rozbilo, v souboru nic neni")
        postup = [0, 1, 1]
        sprav_postup()
def Shop(x, y):
    global SpasPS, boxyShop, CenyShopu, UcinostShopu, TextSPS, ObdelnikSPS
    cisloboxu=0
    for index,obal in enumerate(boxyShop):
        #print(obal, x , y)
        if x > obal[0] and y > obal[1] and x < obal[2] and y < obal[3]: cisloboxu=int(index)
    if CenyShopu[cisloboxu] > postup[0]: return 0
    else: postup[0]-=CenyShopu[cisloboxu]
    print(cisloboxu)
    sprav_postup()

    if postup[cisloboxu*2+4] ==0:
        postup[2] += 1
    postup[cisloboxu * 2 + 4] +=1

    if cisloboxu*2+4+2 >= len(postup):
        print("Spravuju")
        sprav_postup()
    SpasPS += UcinostShopu[cisloboxu]
    TextSPS = fontSPS.render(("Dostáváš " + str(round(SpasPS, 2)) + " Spasení za vteřinu"), True, YELLOW, BGCOLOR)
    ObdelnikSPS = TextSPS.get_rect()
    ObdelnikSPS.center = (450, 520)
    CenyShopu[cisloboxu] = CenyShopu[cisloboxu] * 2
    UcinostShopu[cisloboxu] = UcinostShopu[cisloboxu] * 1.3
    vykresli(postup)

JmenaShopu = ["Uklízečka", "Školník", "Bufetářka", "Baštář", "Filip", "Hadravová", "Říďa", "Janek", "IN CASE OF EMEGENCY"]
JmenaClickeru = ["Bageta z bufetu", "Roztáhnutí žaluzií", "Smazaní tabule", "Úklid sklepa", "Vítězství Náboje", "Vítězství Majálesu"]
CenyShopu = [8**x for x in range(len(JmenaShopu))]
CenyClickeru = []
UcinostShopu = [0.1, 2, 10, 113, 1000, 4294, 10000, -1, -1]
postup = []
boxyClicker=[]
boxyShop=[]
SpasPS=0


pocitadlosekundy=0
Uhel=0
FPS = 30  # frames per second, the general speed of the program
WINDOWWIDTH = 900  # size of window's width in pixels
WINDOWHEIGHT = 600  # size of windows' height in pixels
imageheight = 137
FPS = 30


BGCOLOR = BLACK
ButtonsColor = NAVYBLUE
UnbuyableButtonsColor=GREY
TextColor = WHITE
LineColor = GREEN
LineWidth = 2

pygame.init()
fontObj = pygame.font.Font("AbhayaLibre-Medium.ttf", 30)
fontCena = pygame.font.Font("AbhayaLibre-Medium.ttf", 15)
fontSPS = pygame.font.Font("AbhayaLibre-Medium.ttf", 20)
pygame.display.set_caption("JirsíkClicker")
obrazovka = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))

HLAVA = pygame.image.load('Hlava.jpg')
imageweight, imageheight = HLAVA.get_rect().size

nactisoubor()
sprav_postup()

hlavy = []
for i in range(360):
    hlavy.append(rot_center(HLAVA, i))
for i in range(postup[2]):
    for _ in range(postup[i*2+4]):
        SpasPS += UcinostShopu[i]
        CenyShopu[i] = CenyShopu[i] * 2
        UcinostShopu[i] = UcinostShopu[i] * 1.3

TextSpaseni = fontObj.render(("Máš " + str(round(postup[0])) + " Spasení"), True, TextColor, BGCOLOR)
ObdelnikSpaseni = TextSpaseni.get_rect()
ObdelnikSpaseni.center = (450, WINDOWHEIGHT - 30)
TextClicker = fontObj.render("Clicker", True, TextColor, BGCOLOR)
ObdelnikClicker = TextClicker.get_rect()
ObdelnikClicker.center = (150, 30)
TextShop = fontObj.render("Shop", True, TextColor, BGCOLOR)
ObdelnikShop = TextShop.get_rect()
ObdelnikShop.center = (750, 30)
TextSin = fontObj.render("Síň Spasení", True, TextColor, BGCOLOR)
ObdelnikSin = TextSin.get_rect()
ObdelnikSin.center = (450, 30)
TextKup = fontObj.render("Kup!", True, TextColor, ButtonsColor)
ObdelnikKup = TextKup.get_rect()
TextSPS = fontSPS.render(("Dostáváš " + str(round(SpasPS, 2)) + " Spasení za vteřinu"), True, YELLOW, BGCOLOR)
ObdelnikSPS = TextSPS.get_rect()
ObdelnikSPS.center = (450, 520)


i=0












while True:
    MouseClicked = 0
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            f = open("save.txt", "w")
            for i in postup: f.write(str(round(i))), f.write("\n")
            f.close()
            sys.exit()
        elif event.type == MOUSEMOTION:
            mousex, mousey = event.pos
        elif event.type == MOUSEBUTTONUP:
            mousex, mousey = event.pos
            MouseClicked = True

    if MouseClicked:
        if jenaJirsovi(mousex, mousey):
            postup[0] += 1
            print(postup[0])
            TextSpaseni = fontObj.render(("Máš " + str(round(postup[0])) + " Spasení"), True, TextColor, BGCOLOR)
            ObdelnikSpaseni = TextSpaseni.get_rect()
            ObdelnikSpaseni.center = (450, WINDOWHEIGHT - 30)

        elif jenaBoxu(mousex, mousey) !=0:
            if jenaBoxu(mousex, mousey) == "right":     Shop(mousex, mousey)#TODO: Shop
            #else: Clicker(mousex, mousey)#TODO: Clicker


    vykresli(postup)
    FPSCLOCK.tick(FPS)
    pocitadlosekundy+=1
    if pocitadlosekundy == FPS:
        postup[0] += SpasPS
        TextSpaseni = fontObj.render(("Máš " + str(round(postup[0])) + " Spasení"), True, TextColor, BGCOLOR)
        ObdelnikSpaseni.center = (450, WINDOWHEIGHT - 30)
        pocitadlosekundy = 0
        print(postup)
    i -= 1
    if i == -1:
        i = 359

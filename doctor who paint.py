#-------------------------------General Initialization----------------------------------------------
from pygame import *
from math import *
from random import *
from glob import *
screen= display.set_mode((1200,682))
icon = image.load('pictures/dwlogo.jpg')
display.set_caption ("DOCTOR WHO: EXTERMIPAINT!")
display.set_icon(icon)
#--------------------------------LOADING/BLITTING PICTURES, DEFINING RECTS-------------------------------------
#general things
patchup = image.load('pictures/patchup.jpg') #to cover up things
background = image.load("pictures/exterminate4photoshop.jpg")
screen.blit(background,(0,0))
backup = image.load('pictures/exterminate3photoshop2.jpg')      #blitted over the things that pop up after Rectangles are selected on the TARDIS
backgroundscreen = image.load('pictures/backgroundscreen.png')
#Canvas
canvasRect = Rect(170,30,850,465)
draw.rect(screen, (255,255,255),canvasRect)
#Tardis
tardis = image.load("pictures/tardiss.png") #the selection manual
screen.blit(tardis,(2,27))
#Colour Palette/Spectrum
colourspectrum = image.load("pictures/colourspectrum2.jpg")
cspectrum = screen.blit(colourspectrum,(1035,40))
#Screwdriver Rect
screwdriverRect = Rect(23,168,50,51)
screwdriver = image.load('pictures/screwdriver.png')
screen.blit(screwdriver,(40,168))
#stamp Rect
stampRect = Rect(23,229,51,51)
stampR = image.load('pictures/dw.png')
screen.blit(stampR,(33,227))
#Music Rect
musicRect = Rect(94,229,52,51)
musicR = image.load('pictures/recorder.png')
musicR2 = image.load('pictures/note.png')
screen.blit(musicR,(100,228))
screen.blit(musicR2,(115,250))
#shape Rect
shapeRect = Rect(94,168,52,51)
shapeR = image.load('pictures/pandorica.png')
screen.blit(shapeR,(97,170))
#pencil Tool
pencilRect = Rect(30,395,45,44)
pencil1 = image.load('pictures/pencil2.png') #black and white
pencil2 = image.load('pictures/pencil3.png') #coloured
#Eraser tool
eraserRect = Rect(95,395,45,44)
eraser1 = image.load('pictures/eraser1.png') 
eraser2 = image.load('pictures/eraser2.png') 
#Brush tool
brushRect = Rect(30,460,67,51)
brush1 = image.load('pictures/brush1.png')
brush2 = image.load('pictures/brush2.png') 
#SquareBrush tool
sbrushRect = Rect(110,455,30,30)
sbrush2 = image.load('pictures/sbrush.png')
sbrush1 = image.load('pictures/sbrush2.png')
sbrush3 = image.load('pictures/sbrush3.png')
#CircleBrush tool
cbrushRect = Rect(110,485,30,30)
cbrush1 = image.load('pictures/cbrush1.png')
cbrush2 = image.load('pictures/cbrush2.png')
cbrush3 = image.load('pictures/cbrush3.png')
#Spraypaint tool
spraypaintRect = Rect(30, 530, 46,48)
spraypaint1 = image.load('pictures/spraypaint2.jpg')
spraypaint2 = image.load('pictures/spraypaint.jpg')
#Eyedropper tool
eyedropperRect = Rect(95,533,44,44)
eyedropper1 = image.load('pictures/eyedropper1.png')
eyedropper2 = image.load('pictures/eyedropper2.png')
#fillbucket tool
fillRect = Rect(30,595,45,46)
fill1 = image.load('pictures/fillbucket1.png')
fill2 = image.load('pictures/fillbucket.png')
#DrawingLine tool
lineRect = Rect(40,110,50,50)
#Shapes tool
rectangleRect = Rect(65,381,40,40)
ellipseRect = Rect(65,436,40,40)
polygonRect = Rect(65,491,40,40)
filledRect = Rect(65,546,40,40)
lineRect = Rect(65,601,40,40)
rectangle = image.load('pictures/rectangle.jpg') 
ellipse = image.load('pictures/ellipse.jpg')
polygon = image.load('pictures/polygon.jpg')
rectangle2 = image.load('pictures/rectangle2.jpg')
ellipse2 = image.load('pictures/ellipse2.jpg')
polygon2 = image.load('pictures/polygon2.jpg')
filledon = image.load('pictures/filledon.png')
filledoff = image.load('pictures/filledoff.png')
line = image.load('pictures/line.jpg')
line2 = image.load('pictures/line2.jpg')
#Save button
saveRect = Rect(1030,575,50,17)
#load button
loadRect = Rect(1090,575,50,17)
#Music buttons
musicstart = image.load('pictures/musicpause.png')
musicpause = image.load('pictures/musicstart.png')
musicstart2 = image.load('pictures/musicpause2.png')
musicpause2 = image.load('pictures/musicstart2.png')
musicpp = Rect(60,395,40,40)
#stamps
stamp1 = image.load('pictures/dalekbw.png') #black and white stamps
stamp2 = image.load('pictures/silencebw.png')
stamp3 = image.load('pictures/cybermanbw.png')
stamp5 = image.load('pictures/smithnewbw.png')
stamp6 = image.load('pictures/pondbw.png')
stamp7 = image.load('pictures/colemanbw.png')
stamp8 = image.load('pictures/feztardisbw.png')
stamp1c = image.load('pictures/dalek.png') #coloured stamps
stamp2c = image.load('pictures/silence.png')
stamp3c = image.load('pictures/cyberman.png')
stamp5c = image.load('pictures/smithnew.png')
stamp6c = image.load('pictures/pond.png')
stamp7c = image.load('pictures/coleman.png')
stamp8c = image.load('pictures/feztardis.png')
pond = [image.load('pictures/pond1.png'),image.load('pictures/pond2.png'),image.load('pictures/pond3.png')] #stamps organized in lists
dalek = [image.load('pictures/dalek1.png'),image.load('pictures/dalek2.png'),image.load('pictures/dalek3.png')] #in order of size
coleman = [image.load('pictures/coleman1.png'),image.load('pictures/coleman2.png'),image.load('pictures/coleman3.png')]
smith = [image.load('pictures/smithnew1.png'),image.load('pictures/smith2.png'),image.load('pictures/smith3.png')]
silence = [image.load('pictures/silence1.png'),image.load('pictures/silence2.png'),image.load('pictures/silence3.png')]
feztardis = [image.load('pictures/feztardis1.png'),image.load('pictures/feztardis2.png'),image.load('pictures/feztardis3.png')]
cybermen = [image.load('pictures/cybermen1.png'),image.load('pictures/cybermen2.png'),image.load('pictures/cybermen3.png')]
small = image.load('pictures/small1.png')       #stamp sizes
medium = image.load('pictures/medium.png')
large = image.load('pictures/large.png')
small2 = image.load('pictures/small2.png')
medium2 = image.load('pictures/medium2.png')
large2 = image.load('pictures/large2.png')
smallRect = screen.blit(small,(115,565))
mediumRect = screen.blit(medium,(115,590))
largeRect = screen.blit(large,(115,615))
stampsizeR = image.load('pictures/size.png')
stamp1Rect = screen.blit(stamp1,(13,380))
stamp2Rect = screen.blit(stamp2,(62,380))
stamp3Rect = screen.blit(stamp3,(110,380))
stamp5Rect = screen.blit(stamp5,(62,440))
stamp6Rect = screen.blit(stamp6,(100,440))
stamp7Rect = screen.blit(stamp7,(13,465))
stamp8Rect = screen.blit(stamp8,(60,560))
stampsizeR = image.load('pictures/size.png')
#things for the helpscreen
allonsyRect = Rect(150,575,250,60)
allonsy1 = image.load('pictures/allonsy1.png')
allonsy2 = image.load('pictures/allonsy2.png')
helpscreen = image.load('pictures/confused.png')
blackscreen = image.load('pictures/blackscreen.png')
#things for the backgrounds selection screen
backgroundRect = Rect(23,290,52,51)
backgroundR = image.load('pictures/backgroundRect.png')
screen.blit(backgroundR,(25,290))
backgrounds = [image.load('pictures/timelordpatternS.jpg'),image.load('pictures/crackS.jpg'),image.load('pictures/tardisblackandwhiteS.jpg'),image.load('pictures/tardisbackgroundS.jpg'),image.load('pictures/galifreyS.jpg'),image.load('pictures/timevortexS.jpg')]
backgroundsc = [image.load('pictures/timelordpatternSc.jpg'),image.load('pictures/crackSc.jpg'),image.load('pictures/tardisblackandwhiteSc.jpg'),image.load('pictures/tardisbackgroundSc.jpg'),image.load('pictures/galifreySc.jpg'),image.load('pictures/timevortexSc.jpg')]
backgroundpos = [(20,260),(420,260),(820,260),(20,470),(420,470),(820,470)] #these three lists are corresponding
background1 = Rect(20,260,365,200)
background2 = Rect(420,260,365,200)
background3 = Rect(820,260,365,200)
background4 = Rect(20,470,365,200)
background5 = Rect(420,470,365,200)
background6 = Rect(820,470,365,200)
geronimos = [image.load('pictures/geronimop.png'),image.load('pictures/geronimo.png')]
geronimoRect = Rect(1000,150,200,60) #geronimo, this is clicked when the user wants to exit the screen
backgroundlist =[image.load('pictures/timelordpattern.jpg'),image.load('pictures/crack.jpg'),image.load('pictures/tardisblackandwhite.jpg'),image.load('pictures/tardisbackground.jpg'),image.load('pictures/galifrey.jpg'),image.load('pictures/timevortex.jpg')]                                              
backgroundpic = -1                                               #no current backgrounds selected
#random colour or normal modes selection
randomcolour1 = image.load('pictures/random1.png')
normal = image.load('pictures/normal.png')
randomcolourRect = Rect(1030,635,75,19)
#keyboards shortcut page
shortcut = image.load('pictures/keyboards.png')
fantasticRect = Rect(25,625,300,50)
fantastic1 = image.load('pictures/fantastic1.png')
fantastic2 = image.load('pictures/fantastic2.png')
#--------------------------FONT----------------------------
font.init()
courier = font.SysFont("courier new", 16)
courieru = font.SysFont("courier new", 16) #underlined
couriers = font.SysFont('courier new',14) #small
courieru.set_underline(True)
#-------------------------------General Variables (Default) -------------------------------------------
running = True

currentc = (0,0,0) #current colour (pencil colour)
eraserc = (255,255,255) #eraser colour
size = 1 
Rectangle = ""              #this will later be indicating which box is selected on the TARDIS (the police box)
tools = "pencil" 
musicS = "pause" 
songt = "" #selected song title
song = "" #selected song
stampsize =1
#music
init()  
music = 0 #setting the first song in the music list as the default music
mx,my = (0,0)
#for polygon tool
spots = []
points = []
delpoints = []
#redo
redo = []
#undo
blank = screen.subsurface(canvasRect).copy()
undo = [blank]
musicpos = 0
#flags
randomflagc = False #when this is selected, applicable tools will be in a random colour mode
shortcutflag = False
helpflag = False
filled = False #the shapes are not filled
sizeflag = False #verify if the tool requires size
run = True #to indicate if the rest of the program is running - for backgrounds
run2 = True                                                     #for helpRect
run3 = True                                                     #for keyboard shortcut
keyboardflag = False
counting = 0
rcontrol_pressed = False
lcontrol_pressed = False
#---------------------STRAX FIELD REPORT/CURRENT STATUS---------------
straxcolour = (44,24,220)
strax = courier.render('STRAX FIELD', True, (88,135,200))
report = courier.render('REPORT:', True,(88,135,200))
screen.blit(strax,(1030,295))
screen.blit(report,(1030,315))
currentPic = courier.render("weapon-",True, straxcolour)
screen.blit(currentPic,(1030,335))
currentsizePic = courier.render("current size-", True, straxcolour)
screen.blit(currentsizePic,(1030,375))
poscPic = courier.render('location-',True,straxcolour)
screen.blit(poscPic,(1030,415))
currentmusicPic = courier.render('battle tune-', True, straxcolour)
screen.blit(currentmusicPic,(1030,455))
screens = [image.load('pictures/loadscreen.png'),image.load('pictures/canvasblock.png')] #canvasblock is the savescreen
#---------------------FUNCTIONS-------------------------------------------------------------------
def getName(screen,load):
    ans = ""                    #what the user enters
    back = screen.copy()
    textArea = Rect(0,400,1200,25) #where the user will be entering things
    typing = True
    if load: screen.blit(screens[0],(0,0))    #loadscreen
    else: screen.blit(screens[1],(0,0))   #savescreen
    while typing:
        for e in event.get():
            if e.type == QUIT:
                event.post(e)
                return ""
            if e.type == KEYDOWN:
                if e.key == K_BACKSPACE:
                    if len(ans)>0: ans = ans[:-1]
                elif e.key == K_KP_ENTER or e.key == K_RETURN : 
                    typing = False
                    save = True
                elif e.key < 256: ans += e.unicode
        
        txtPic = courier.render(ans, True, (0,0,0))
        draw.rect(screen,(88,113,200),textArea)         
        draw.rect(screen,(0,0,223),textArea,4)
        screen.blit(txtPic,(textArea.x+3,textArea.y+2))
        display.flip()
    screen.blit(back,(0,0))
    return ans

def inputtext():            #same idea as getName
    text = ""
    tmx,tmy = mouse.get_pos()
    textscreencopy = screen.copy()
    textArea = Rect(tmx,tmy,1020-tmx,size+15)
    textBack = screen.subsurface(textArea).copy()
    typingtext = True
    couriertext = font.SysFont('courier new',size+10)
    while typingtext:
        for e in event.get():
            if e.type == QUIT:
                event.post(e)
                return ''
            if e.type == KEYDOWN:
                if e.key == K_BACKSPACE:
                    if len(text)>0:
                        text = text[:-1]
                elif e.key == K_KP_ENTER or e.key == K_RETURN : 
                    typingtext = False
                elif e.key < 256:
                    text += e.unicode
        textPic = couriertext.render(text,True,currentc)
        screen.blit(textBack,textArea)
        screen.blit(textPic,(textArea.x+3,textArea.y+2))
        display.flip()
    screen.blit(textscreencopy,(0,0))
    return text

def collidefunc(n):       #HIGHLIGHTING FUNCTION FOR RECTS              
    if n.collidepoint(mx,my): draw.rect(screen,(50,50,255),n,2)
    else: draw.rect(screen,(33,68,129),n,2)

def collidefunc2(n):        #HIGHLIGHTING FUNCTION FOR ICONS
    if n.collidepoint(mx,my): draw.rect(screen,(0,0,255),n,3)
    else: draw.rect(screen,(255,255,255),n,3)

#-----------------------------------------------------------------
while running:
    mx,my = mouse.get_pos() #one of the points
    pressoncel = False #right key pressed
    pressoncer = False #left key pressed
    #SHORTCUTS
    saveshort = False
    loadshort = False
    undoshort = False
    newshort = False
    redoshort = False
    randomshort = False
    for e in event.get():
        if e.type == QUIT: running = False
        if e.type == KEYDOWN:
            if e.key == K_UP: size += 1
            if e.key == K_DOWN:
                if size != 1: size -= 1
            if e.key == K_RCTRL: rcontrol_pressed = True
            if e.key == K_LCTRL: lcontrol_pressed = True
            if rcontrol_pressed or lcontrol_pressed:
                if e.key == K_s: saveshort = True
                if e.key == K_o: loadshort = True
                if e.key == K_z: undoshort = True
                if e.key == K_y: redoshort = True
                if e.key == K_n: newshort = True
                if e.key == K_k: shortcut = True
                if e.key == K_r: randomshort = True
        if e.type == KEYUP:
            if e.key == K_RCTRL: rcontrol_pressed = False
            if e.key == K_LCTRL: lcontrol_pressed = False
        if e.type == MOUSEBUTTONDOWN:
            screencopy = screen.copy()
            start = mx,my
            if e.button == 1: pressoncel = True
            if e.button == 3: pressoncer = True
            
        if e.type == MOUSEBUTTONUP:
            if canvasRect.collidepoint(mx,my) and run and run2:
                canvaspic = screen.subsurface(canvasRect).copy()
                undo.append(canvaspic)
                redo = []
                delpoints = []

    nmx,nmy = mouse.get_pos()
    mb = mouse.get_pressed()
#-----------------------------------------------------------------
    #New
    if run and run2 and run3:           #if everything is running
        dash = courier.render('-',True,(0,128,192))
        newRect = Rect(1150,535,30,20)
        undoRect = Rect(1030,535,30,20)
        redoRect = Rect(1090,535,30,20)
        textRect = Rect(1030,615,30,20)
        helpRect = Rect(1090,615,30,20)
        shortcutRect = Rect(1105,5,60,20)
        #new
        if newRect.collidepoint(mx,my): newPic = courier.render("NEW",True, (21,39,147))
        else: newPic = courier.render("NEW",True, (80,98,207))
        screen.blit(patchup,(1150,535))
        screen.blit(newPic,(1150,535))
        #undo
        if undoRect.collidepoint(mx,my): undoPic = courier.render('UNDO',True,(21,39,147))
        else: undoPic = courier.render('UNDO', True,(80,98,207))
        screen.blit(patchup,(1030,535))
        screen.blit(undoPic,(1030,535))
        #redo
        if redoRect.collidepoint(mx,my): redoPic = courier.render('REDO',True,(21,39,147))
        else: redoPic = courier.render('REDO',True,(80,98,207))
        screen.blit(patchup,(1090,535))
        screen.blit(redoPic,(1090,535))
        #save
        if saveRect.collidepoint(mx,my): saveTxt = courier.render('SAVE', True,(0,0,255))
        else: saveTxt = courier.render('SAVE', True, (0,255,255))
        screen.blit(patchup,(1030,575))
        screen.blit(saveTxt,(1030,575))
        #load
        if loadRect.collidepoint(mx,my): loadTxt = courier.render('LOAD',True,(0,0,255))
        else: loadTxt = courier.render('LOAD', True,(0,255,255))
        screen.blit(patchup,(1090,575))
        screen.blit(loadTxt,(1090,575))
        screen.blit(dash,(1075,575))
        #text
        if textRect.collidepoint(mx,my): textTxt = courier.render('TEXT',True,(0,0,255))
        else: textTxt = courier.render('TEXT',True,(0,255,255))
        screen.blit(patchup,(1030,615))
        screen.blit(textTxt,(1030,615))
        #shortcuts
        if shortcutRect.collidepoint(mx,my):
            shortcutText = courier.render('SHORTCUTS',True,(0,0,255))
            if mb[0] == 1:
                shortcutflag = True
                run3 = False                                #NOW THE REST OF THE PROGRAM WON'T BE RUNNING
                shortcutText = courier.render('SHORTCUTS',True,(0,255,255))
                savescreencopy = screen.copy()
                screen.blit(shortcut,(0,0))
        else: shortcutText = courier.render('SHORTCUTS',True,(0,255,255))
        screen.blit(patchup,(1105,5))
        screen.blit(patchup,(1155,5))
        screen.blit(shortcutText,(1105,5))
        #help
        if helpRect.collidepoint(mx,my):
            helpTxt = courier.render('HELP',True,(0,0,255))
            if mb[0] == 1:
                helpflag = True
                run2 = False                                    #NOW THE REST OF THE PROGRAM WON'T BE RUNNING
                helpTxt = courier.render('HELP',True,(0,255,255))
                savescreencopy = screen.copy()
                screen.blit(blackscreen,(0,0))
                screen.blit(helpscreen,(0,0))
        else: helpTxt = courier.render('HELP',True,(0,255,255))
        screen.blit(patchup,(1090,615))
        screen.blit(helpTxt,(1090,615))
        #--------------------------RANDOM COLOURS-------------------------
        if randomflagc == False and run and run2 and run3:                    #normal mode
            screen.blit(patchup,(1030,635))
            screen.blit(patchup,(1080,635))
            screen.blit(normal,(1030,635))
            if randomcolourRect.collidepoint(mx,my):
                screen.blit(patchup,(1030,635))
                screen.blit(patchup,(1080,635))
                screen.blit(randomcolour1,(1030,635))
                if pressoncel:
                    randomflagc = True
        elif randomflagc and run and run2 and run3:               #random mode
            screen.blit(patchup,(1030,635))
            screen.blit(patchup,(1080,635))
            screen.blit(randomcolour1,(1030,635))
            if randomcolourRect.collidepoint(mx,my):
                screen.blit(patchup,(1030,635))
                screen.blit(patchup,(1080,635))
                screen.blit(normal,(1030,635))
                if pressoncel:
                    randomflagc = False
        if randomshort == True: randomflagc = True
    #---------------------------------------------------------------------TARDIS RECTANGLE TOOLS SELECTION---------------------------
        #----------------------SCREWDRIVER RECT----------------------
        if Rectangle == "screwdriver":
            draw.rect(screen,(0,0,255),screwdriverRect,1)
            screen.blit(backup,(4,371))  
            #---------------------pencil selection-------------
            if tools == "pencil": screen.blit(pencil2,(30,395))
            else:
                screen.blit(pencil1,(30,395))
                collidefunc2(pencilRect)
            if pencilRect.collidepoint(mx,my) and pressoncel: tools = "pencil"
            #--------------------eraser selection---------------
            if tools == "eraser": screen.blit(eraser2,(95,395))
            else:
                screen.blit(eraser1,(95,395))
                collidefunc2(eraserRect)
            if eraserRect.collidepoint(mx,my) and pressoncel:
                    tools = "eraser"
                    sizeflag = True
            #-------------------brush selection----------------
            screen.blit(sbrush1,(110,455))
            screen.blit(cbrush1,(110,485))
            if tools == "square brush":
                screen.blit(sbrush2,(110,455))
                screen.blit(cbrush1,(110,485))
                screen.blit(brush2,(30,460))
            elif tools == "circle brush":
                screen.blit(cbrush2,(110,485))
                screen.blit(sbrush1,(110,455))
                screen.blit(brush2,(30,460))
            else: screen.blit(brush1,(30,460))   
            if sbrushRect.collidepoint(mx,my):
                if mb[0] == 1:
                    tools = "square brush"
                    draw.rect(screen,(255,255,255),brushRect,3)
                    sizeflag = True
                else:
                    draw.rect(screen,(0,0,255),brushRect,3)
                    screen.blit(sbrush3,(110,455))
            elif cbrushRect.collidepoint(mx,my):
                if mb[0] == 1:
                    tools = "circle brush"
                    draw.rect(screen,(255,255,255),brushRect,3)
                    sizeflag = True
                else:
                    draw.rect(screen,(0,0,255),brushRect,3)
                    screen.blit(cbrush3,(110,485))
            #-------------------spraypaint selection----------
            if tools == "spraypaint": screen.blit(spraypaint2,(30,530))
            else:
                screen.blit(spraypaint1,(30,530))
                collidefunc2(spraypaintRect)
            if spraypaintRect.collidepoint(mx,my) and pressoncel: tools = "spraypaint"
            #-------------------eyedropper selection-------------
            if tools == "eyedropper": screen.blit(eyedropper2,(95,533))
            else:
                screen.blit(eyedropper1,(95,533))
                collidefunc2(eyedropperRect)
            if eyedropperRect.collidepoint(mx,my) and pressoncel:
                tools = "eyedropper"
            #------------------fill selection----------------
            if tools == "fill": screen.blit(fill2,(30,595))
            else:
                screen.blit(fill1,(30,595))
                collidefunc2(fillRect)
            if fillRect.collidepoint(mx,my) and pressoncel: tools = "fill"
        else:
            if run and run2 and run3: collidefunc(screwdriverRect)
        #----------------------STAMP RECT-----------------------
        if Rectangle == "stamp":
            tools = 'stamps'
            draw.rect(screen,(0,0,255),stampRect,1)
            screen.blit(backup,(4,371))
            #draw.rect(screen,(255,0,255),choiceRect,1)
            if stamp1Rect.collidepoint(mx,my):
                screen.blit(stamp1c,(13,380))
                if mb[0] == 1: stamp = "dalek stamp"
            else: screen.blit(stamp1,(13,380))
            if stamp2Rect.collidepoint(mx,my):
                screen.blit(stamp2c,(62,380))
                if mb[0] == 1: stamp = "silent stamp"
            else: screen.blit(stamp2,(62,380))
            if stamp3Rect.collidepoint(mx,my):
                screen.blit(stamp3c,(110,380))
                if mb[0] == 1: stamp = "cyberman stamp"
            else: screen.blit(stamp3,(110,380))
            if stamp5Rect.collidepoint(mx,my):
                screen.blit(stamp5c,(62,440))
                if mb[0] == 1: stamp = "11th doctor stamp"
            else: screen.blit(stamp5,(62,440))
            if stamp6Rect.collidepoint(mx,my):
                screen.blit(stamp6c,(100,440))
                if mb[0] == 1: stamp = "amelia pond stamp"
            else: screen.blit(stamp6,(100,440))
            if stamp7Rect.collidepoint(mx,my):
                screen.blit(stamp7c,(13,465))
                if mb[0] == 1: stamp = "clara stamp"
            else: screen.blit(stamp7,(13,465))
            if stamp8Rect.collidepoint(mx,my):
                screen.blit(stamp8c,(60,560))
                if mb[0] ==1: stamp = "DW logo stamp"
            else: screen.blit(stamp8,(60,560))
            if smallRect.collidepoint(mx,my) and mb[0] ==1: stampsize = 0
            if mediumRect.collidepoint(mx,my) and mb[0] ==1: stampsize = 1
            if largeRect.collidepoint(mx,my) and mb[0] ==1: stampsize = 2
            if stampsize == 0: screen.blit(small2,(115,565))
            else:
                screen.blit(small,(115,565))
                collidefunc2(smallRect)
            if stampsize == 1: screen.blit(medium2,(115,590))
            else:
                screen.blit(medium,(115,590))
                collidefunc2(mediumRect)
            if stampsize == 2: screen.blit(large2,(115,615))
            else:
                screen.blit(large,(115,615))
                collidefunc2(largeRect)
            screen.blit(stampsizeR,(140,565))
        else:
            if run and run2 and run3: 
                collidefunc(stampRect)
                stamp = ""
        #-----------------------SHAPE RECT---------------------
        if Rectangle == "shape":
            draw.rect(screen,(0,0,255),shapeRect,1)
            screen.blit(backup,(4,371)) 
            #draw.rect(screen,(255,0,255),choiceRect,1)
            if rectangleRect.collidepoint(mx,my) and mb[0] ==1: tools = "rectangle"
            if polygonRect.collidepoint(mx,my) and mb[0] == 1: tools = "polygon"
            if ellipseRect.collidepoint(mx,my) and mb[0] == 1: tools = "ellipse"
            if lineRect.collidepoint(mx,my) and mb[0] ==  1:
                tools = "line"
                size = True
            if tools == "rectangle":screen.blit(rectangle2,(65,381))
            else:
                screen.blit(rectangle,(65,381))
                collidefunc2(rectangleRect)
            if tools == "ellipse": screen.blit(ellipse2,(65,436))
            else:
                screen.blit(ellipse,(65,436))
                collidefunc2(ellipseRect)
            if tools == "polygon": screen.blit(polygon2,(65,491))
            else:
                screen.blit(polygon,(65,491))
                collidefunc2(polygonRect)
            if filled == False:
                screen.blit(filledoff,(65,546))
                collidefunc2(filledRect)
                if filledRect.collidepoint(mx,my) and pressoncel: filled = True
            elif filled == True:
                screen.blit(filledon,(65,546))
                collidefunc2(filledRect)
                if filledRect.collidepoint(mx,my) and pressoncel: filled = False
            if tools == "line": screen.blit(line2,(65,601))
            else:
                screen.blit(line,(65,601))
                collidefunc2(lineRect)
        else:
            if run and run2 and run3: 
                collidefunc(shapeRect)
        #--------------------MUSIC RECT------------------
        if Rectangle == "music":                            #MUSIC SELECTION
            music1Rect = Rect(19,455,85,15)
            if song == "music1":
                music1Pic = couriers.render("doomsday", True, (242,150,151))
                songt = "DOOMS DAY"
            else:
                music1Pic = couriers.render("doomsday",True, (88,113,142))
                if music1Rect.collidepoint(mx,my):
                    music1Pic = couriers.render("doomsday",True, (174,150,242))
                    if pressoncel:
                        song = "music1"
                        mixer.music.load('doomsday.mp3')
                        musicS = "start"
                        mixer.music.play()
            music2Rect = Rect(19,485,130,15)
            if song == "music2":
                music2Pic = couriers.render("i am the doctor", True, (242,150,151))
                songt = "I AM THE DOCTOR"
            else:
                music2Pic = couriers.render("i am the doctor", True, (88,113,142))
                if music2Rect.collidepoint(mx,my):
                    music2Pic = couriers.render("i am the doctor", True, (174,150,242))
                    if pressoncel:
                       song =  "music2"
                       mixer.music.load('IamtheDoctor.mp3')
                       musicS = "start"
                       mixer.music.play()
            music3Rect = Rect(19,515,120,15)
            if song == "music3":
                music3Pic = couriers.render("abigail's song", True, (242,150,151))
                songt = "ABIGAIL'S SONG"
            else:
                music3Pic = couriers.render("abigail's song", True,(88,113,142))
                if music3Rect.collidepoint(mx,my):
                    music3Pic = couriers.render("abigail's song", True,(174,150,242))
                    if pressoncel:
                        song = "music3"
                        mixer.music.load('AbigailsSong.mp3')
                        musicS = "start"
                        mixer.music.play()
            music4Rect = Rect(19,545,100,15)
            if song == "music4":
                music4Pic = couriers.render("ten's theme", True, (242,150,151))
                songt = "TEN'S THEME"
            else:
                music4Pic = couriers.render("ten's theme", True, (88,113,142))
                if music4Rect.collidepoint(mx,my):
                    music4Pic = couriers.render("ten's theme", True, (174,150,242))
                    if pressoncel:
                        song = "music4"
                        mixer.music.load('TensTheme.mp3')
                        musicS = "start"
                        mixer.music.play()
            music5Rect = Rect(19,575,140,15)
            if song == "music5":
                music5Pic = couriers.render("this is gallifrey", True, (242,150,151))
                songt = "THIS IS GALLIFREY"
            else:
                music5Pic = couriers.render("this is gallifrey", True, (88,113,142))
                if music5Rect.collidepoint(mx,my):
                    music5Pic = couriers.render("this is gallifrey", True, (174,150,242))
                    if pressoncel:
                        song = "music5"
                        mixer.music.load('ThisIsGallifrey.mp3')
                        musicS = "start"
                        mixer.music.play()
            draw.rect(screen,(0,0,255),musicRect,1)
            screen.blit(backup,(4,371))
            #DECIDING IF MUSIC IS PLAYING OR NOT
            if musicS == "pause":
                screen.blit(musicpause,(60,395))
                if musicpp.collidepoint(mx,my):
                    screen.blit(musicstart2,(60,395))
                    if pressoncel:
                        if mixer.music.get_busy(): mixer.music.unpause()
                        else: mixer.music.play()
                        musicS = "start"
            elif musicS == "start":
                screen.blit(musicstart,(60,395))
                if musicpp.collidepoint(mx,my):
                    screen.blit(musicpause2,(60,395))
                    if pressoncel:
                        mixer.music.pause()
                        musicS = "pause"

            screen.blit(music1Pic,(19,455)) #blitting the song titles on
            screen.blit(music2Pic,(19,485))
            screen.blit(music3Pic,(19,515))
            screen.blit(music4Pic,(19,545))
            screen.blit(music5Pic,(19,575))
            
        else:
            if run and run2 and run3: 
                collidefunc(musicRect)
        #------------------OPENING SCREENS-----------------
    if helpflag == True:        #if the helpscreen is selected to open
        allonsy = False
        if allonsyRect.collidepoint(mx,my):
            screen.blit(allonsy1,(150,575))
            if mb[0] == 1: allonsy = True
        else: screen.blit(allonsy2,(150,575))
        if allonsy:         #if the user wants to close the screen
            run2 = True
            helpflag = False
            screen.blit(savescreencopy,(0,0))
    if shortcutflag == True:    #if the shortcut screen is selected to open
        fantastic = False
        if fantasticRect.collidepoint(mx,my):
            screen.blit(fantastic1,(25,625))
            if mb[0] == 1: fantastic = True
        else: screen.blit(fantastic2,(25,625))
        if fantastic:       #same idea as allonsy
            run3 = True
            shortcutflag = False
            screen.blit(savescreencopy,(0,0))
    if Rectangle == 'backgrounds' and run2 and run3: #if the backgrounds screen is selected to open
        geronimo = False
        run = False
        screen.blit(backgroundscreen,(0,0))
        if backgroundpic == 0:                                                  #BACKGROUDNS SELECTION
            screen.blit(backgrounds[0],backgroundpos[0])
            draw.rect(screen,straxcolour,background1,3)
        else:
            if background1.collidepoint(mx,my):
                screen.blit(backgrounds[0],backgroundpos[0])
                if mb[0] == 1: backgroundpic = 0
            else: screen.blit(backgroundsc[0],backgroundpos[0])
        if backgroundpic == 1:
            screen.blit(backgrounds[1],backgroundpos[1])
            draw.rect(screen,straxcolour,background2,3)
        else:
            if background2.collidepoint(mx,my):
                screen.blit(backgrounds[1],backgroundpos[1])
                if mb[0] == 1: backgroundpic = 1
            else: screen.blit(backgroundsc[1],backgroundpos[1])
        if backgroundpic == 2:
            screen.blit(backgrounds[2],backgroundpos[2])
            draw.rect(screen,straxcolour,background3,3)
        else:
            if background3.collidepoint(mx,my):
                screen.blit(backgrounds[2],backgroundpos[2])
                if mb[0] == 1: backgroundpic = 2
            else: screen.blit(backgroundsc[2],backgroundpos[2])
        if backgroundpic == 3:
            screen.blit(backgrounds[3],backgroundpos[3])
            draw.rect(screen,straxcolour,background4,3)
        else:
            if background4.collidepoint(mx,my):
                screen.blit(backgrounds[3],backgroundpos[3])
                if mb[0] == 1: backgroundpic = 3
            else: screen.blit(backgroundsc[3],backgroundpos[3])
        if backgroundpic == 4:
            screen.blit(backgrounds[4],backgroundpos[4])
            draw.rect(screen,straxcolour,background5,3)
        else:
            if background5.collidepoint(mx,my):
                screen.blit(backgrounds[4],backgroundpos[4])
                if mb[0] == 1: backgroundpic = 4
            else: screen.blit(backgroundsc[4],backgroundpos[4])
        if backgroundpic == 5:
            screen.blit(backgrounds[5],backgroundpos[5])
            draw.rect(screen,straxcolour,background6,3)
        else:
            if background6.collidepoint(mx,my):
                screen.blit(backgrounds[5],backgroundpos[5])
                if mb[0] == 1: backgroundpic = 5
            else: screen.blit(backgroundsc[5],backgroundpos[5])
        if geronimoRect.collidepoint(mx,my):
            screen.blit(geronimos[0],(1000,150))
            if mb[0] == 1: geronimo = True
        else: screen.blit(geronimos[1],(1000,150))
        if geronimo:                                        #same idea as allonsy, closing the screen
            run = True
            Rectangle = ''
            screen.blit(savescreencopy,(0,0))
            if backgroundpic != -1:
                screen.blit(backgroundlist[backgroundpic],(170,30))
                undo.append(backgroundlist[backgroundpic])
    else:    
        if run and run2 and run3:
            collidefunc(backgroundRect)
    #------------------NOTHING SELECTED-------------------
        if Rectangle == "":
            screen.blit(backup,(4,371))

    #-----------------------------------------------------------------
        if pressoncel:
            if screwdriverRect.collidepoint(mx,my):
                if Rectangle == "screwdriver": Rectangle = ""
                else: Rectangle = "screwdriver"
            elif stampRect.collidepoint(mx,my):
                if Rectangle == "stamp": Rectangle = ""
                else: Rectangle = "stamp"
            elif shapeRect.collidepoint(mx,my):
                if Rectangle == "shape": Rectangle = ""
                else: Rectangle = "shape"
            elif musicRect.collidepoint(mx,my):
                if Rectangle == "music": Rectangle = ""
                else: Rectangle = "music"
            elif backgroundRect.collidepoint(mx,my):
                if Rectangle == 'backgrounds': Rectangle = ''
                else:
                    Rectangle = 'backgrounds'
                    savescreencopy = screen.copy()
            if textRect.collidepoint(mx,my):
                tools = 'text'
                sizeflag = True
                
        if newRect.collidepoint(mx,my) and pressoncel or newshort: 
            draw.rect(screen,(255,255,255),canvasRect)
                
        if undoRect.collidepoint(mx,my) and pressoncel or undoshort:
            if len(undo) > 1:
                redo.append(undo[-1]) 
                if len(points) > 0:     #Activated if a polygon is in progress at this time
                    delpoints.append(points[-1])    #Add the undone vertex in the list in case user decides to redo
                    points.remove(points[-1])   #Remove last vertex to allow a new line to be drawn
                    ptnum -= 1      #Keep vertex number in sync with vertices changes
                if len(undo) > 1:   #Make sure a blank canvas is kept within the list at all times
                    undo.remove(undo[-1])
                screen.blit(undo[-1],(170,30))
            
        if redoRect.collidepoint(mx,my) and pressoncel or redoshort:
            if len(redo) > 0:
                undo.append(redo[-1])
                screen.blit(redo[-1],(170,30))
                redo.remove(redo[-1])
                if len(delpoints) > 0:  #If a polygon is being drawn and there was one or more undone vertex/vertices
                    points.append(delpoints[-1]) #Add the undone vertex back in the list for the polygon
                    delpoints.remove(delpoints[-1]) #Remove the redone point from the deleted vertices list
                    ptnum += 1  #Keep up with the vertex number
                
        if loadRect.collidepoint(mx,my) and pressoncel or loadshort:
            txt = getName(screen,True)
            if txt in glob("*"):    #To prevent crashing from unfound image
                loaded = image.load(txt)
                screen.set_clip(canvasRect)
                screen.blit(loaded,(170,30))
                loadedpic = screen.subsurface(canvasRect).copy()
                screen.set_clip(None) 
                undo.append(loadedpic)  #Since loadRect is not in the canvas, it was not taken into account for undo/redo
                
        if saveRect.collidepoint(mx,my) and pressoncel or saveshort:
                txt = getName(screen,False)
                if len(txt) > 0:    #To prevent crashing from no input
                    if len(txt) < 4 or txt[-4]!= ".png" and txt[-4]!= ".jpg" and txt[-4]!= ".gif": #Check if an extension is already in place
                        image.save(screen.subsurface(canvasRect),txt+".png")    #If not add one one for them
                    else: image.save(screen.subsurface(canvasRect),txt)   #If so just save the imageimage.save(screen.subsurface(canvasRect),"myPic.png")

#-------------------------------------ACTUALLY DRAWING------------------------------
        if canvasRect.collidepoint(mx,my):                                                        
            screen.set_clip(canvasRect)
            if mb[0]==1:
                if tools == "pencil":
                    draw.line(screen,currentc,(nmx,nmy),(mx,my),1)
                if tools == "line":
                    screen.blit(screencopy,(0,0))
                    if randomflagc == True: draw.line(screen,(randint(0,255),randint(0,255),randint(0,255)),start,(mx,my),size*2) #random mode
                    else: draw.line(screen,currentc,start,(mx,my),size*2) #normal mode
          
                if tools == "rectangle":
                    screen.blit(screencopy,(0,0))                   
                    if abs(start[0]-mx)>=2 and abs(start[1]-my)>=2: #Boundary to prevent crashing due to border width > actual circle
                        rc =Rect(min(start[0], mx),min(start[1], my), abs(start[0]-mx),abs(start[1]-my))
                        if filled == False:                           #By picking the smaller of the two: [start[0/1],mx/y], there is no worry of drawing
                            if randomflagc == False:draw.rect(screen, currentc, rc,1)  #backwards rectangles since the rc will always be drawn from the point closest to (0,0)
                            else: draw.rect(screen,(randint(0,255),randint(0,255),randint(0,255)),rc,1)
                        else:
                            if randomflagc == False: draw.rect(screen, currentc, rc)
                            else: draw.rect(screen,(randint(0,255),randint(0,255),randint(0,255)),rc)
                if tools == "ellipse":
                    screen.blit(screencopy, (0,0))
                    if abs(start[0]-mx)>=2 and abs(start[1]-my)>=2: #Boundary to prevent crashing due to border width > actual circle
                        elpse=Rect(min(start[0], mx),min(start[1], my), abs(start[0]-mx),abs(start[1]-my))
                        if filled == False:                           #By picking the smaller of the two: [start[0/1],mx/y], there is no worry of drawing
                            if randomflagc == False:draw.ellipse(screen, currentc, elpse,1)  #backwards rectangles since the elpseRect will always be drawn from the point closest to (0,0)
                            else: draw.ellipse(screen,(randint(0,255),randint(0,255),randint(0,255)),elpse,1)
                        else:
                            if randomflagc == False: draw.ellipse(screen, currentc, elpse)
                            else: draw.ellipse(screen,(randint(0,255),randint(0,255),randint(0,255)),elpse)
                if tools == "circle brush" or tools == "eraser" or tools == "square brush":
                    dx = nmx - mx  #delta-x             #saved their colours, I grouped them together
                    dy = nmy - my  #delta-y
                    D = int(((dx)**2 + (dy)**2)**.5) #Distance between current cursor position and previous c.p.
                    if D == 0:
                        if tools == "eraser": draw.circle(screen,eraserc,(mx,my),size)
                        elif tools == "circle brush":
                            if randomflagc == False: draw.circle(screen,currentc,(mx,my),size)
                            else: draw.circle(screen,(randint(0,255),randint(0,255),randint(0,255)),(mx,my),size)
                        elif tools == "square brush":
                            if randomflagc == False: draw.rect(screen,currentc,(mx-size,my-size,size*2,size*2)) #-size*2 so the centre of the square is where the mouse is
                            else: draw.rect(screen,(randint(0,255),randint(0,255),randint(0,255)),(mx-size,my-size,size*2,size*2))
                    else:
                        for num in range(D+1):
                            fx = int(mx + (dx/D)*num)     #Filled-in y-coordinate: original distance + the nth y-cord. along the path
                            fy = int(my + (dy/D)*num)     #Filled-in x-coordinate: original distance + the nth x-cord. along the path
                            if tools == "eraser": draw.circle(screen,eraserc,(fx,fy),size)
                            elif tools == "circle brush":
                                if randomflagc == False: draw.circle(screen,currentc,(fx,fy),size)
                                else: draw.circle(screen,(randint(0,255),randint(0,255),randint(0,255)),(fx,fy),size)
                            elif tools == "square brush":
                                if randomflagc == False: draw.rect(screen,currentc,(fx-size,fy-size,size*2,size*2)) #same idea as the other line
                                else: draw.rect(screen,(randint(0,255),randint(0,255),randint(0,255)),(fx-size,fy-size,size*2,size*2))
                   
                if tools == "spraypaint":                   #two points will be selected every run because if only one point is selected, it's hard to tell
                    x = randint(mx-size,mx+size)
                    y = randint(my-size,my+size)    
                    x2 = randint(mx-size,mx+size)
                    y2 = randint(my-size,my+size)
                    if (x-mx)**2 + (y-my)**2 <= size**2:
                        if randomflagc == False: screen.set_at((x,y),currentc)    #Formula to make sure the points are within the circle with radius = size, centre = mx,my
                        else: screen.set_at((x,y),(randint(0,255),randint(0,255),randint(0,255)))
                    if (x2-mx)**2 + (y2-my)**2 <= size**2:
                        if randomflagc == False: screen.set_at((x2,y2),currentc)
                        else: screen.set_at((x2,y2),(randint(0,255),randint(0,255),randint(0,255)))
                if tools == "fill":
                    ospot = mx,my       #ospot = original spot
                    spots.append(ospot)
                    replacedcol = screen.get_at(ospot) #Record the colour that is to be replaced
                    if replacedcol != currentc:  #Making sure the colour to be replaced is not the foreground colour already
                        while len(spots)>0:
                            cx,cy = spots.pop() #coloured-x,coloured-y
                            if screen.get_at((cx,cy)) == replacedcol and canvasRect.collidepoint(cx,cy): #Check if cx,cy is the right colour and within canvas
                                screen.set_at((cx,cy),currentc) #Change colour                        #to prevent bleeding into program backgorund
                                spots+=[(cx,cy-1),(cx,cy+1),(cx-1,cy),(cx+1,cy)] #Append points around the ospot into the list to be checked
                if tools == "eyedropper":
                    if mb[0] == 1: currentc = screen.get_at((mx,my))
                    if mb[2] == 1: eraserc = screen.get_at((mx,my))
                if stamp != '' and canvasRect.collidepoint(mx,my):              #blitting the stamps on-screen
                    if stamp == "dalek stamp":            
                        screen.blit(screencopy,(0,0))
                        dalekc=[(mx-56,my-105),(mx-68,my-131),(mx-81,my-155)]
                        screen.blit(dalek[stampsize],dalekc[stampsize])
                    if stamp == "silent stamp":
                        screen.blit(screencopy,(0,0))
                        silencec = [(mx-20,my-30),(mx-50,my-75),(mx-90,my-140)]
                        screen.blit(silence[stampsize],silencec[stampsize])
                    if stamp == "cyberman stamp":
                        screen.blit(screencopy,(0,0))
                        cybermenc = [(mx-48,my-53),(mx-73,my-79),(mx-92,my-106)]
                        screen.blit(cybermen[stampsize],cybermenc[stampsize])
                    if stamp == "11th doctor stamp":
                        screen.blit(screencopy,(0,0))
                        smithc = [(mx-42,my-95),(mx-40,my-111),(mx-52,my-145)]
                        screen.blit(smith[stampsize],smithc[stampsize])
                    if stamp == "amelia pond stamp":
                        screen.blit(screencopy,(0,0))
                        pondc = [(mx-44,my-95),(mx-53,my-105),(mx-65,my-130)]
                        screen.blit(pond[stampsize],pondc[stampsize])
                    if stamp == "clara stamp":
                        screen.blit(screencopy,(0,0))
                        colemanc = [(mx-32,my-108),(mx-39,my-111),(mx-51,my-155)]
                        screen.blit(coleman[stampsize],colemanc[stampsize])
                    if stamp == "DW logo stamp":
                        screen.blit(screencopy,(0,0))
                        feztardisc =[(mx-47,my-149),(mx-71,my-134),(mx-95,my-189)]
                        screen.blit(feztardis[stampsize],feztardisc[stampsize])
                if tools == 'text':
                    tmx,tmy = mouse.get_pos()
                    txt = inputtext()
                    courierFont = font.SysFont('courier new', size+10)
                    txtPic = courierFont.render(txt,True,currentc)
                    screen.blit(txtPic,(tmx,tmy))                               #blitting the actual text
                    textcanvaspic = screen.subsurface(canvasRect).copy()
                    undo.append(textcanvaspic)            
        screen.set_clip(None) 

#------------------------------------------------
            
        if tools == "polygon" and stamp == '':
            screen.set_clip() 
            if pressoncel and canvasRect.collidepoint(mx,my):
                ptnum += 1  #Counter begins to keep track of vertex number
                ptx,pty = mouse.get_pos()
                point = ptx,pty         #point = vertex
                points.append(point)
                if len(points) > 1: draw.line(screen, currentc,points[ptnum -2],points[ptnum-1],3)   #Consecutive lines that outlines the polygon
            if pressoncer and canvasRect.collidepoint(mx,my) and len(points)>2:
                draw.line(screen,currentc,points[0],points[-1],3)    #Connecting the last line to the first
                undo = undo[:-ptnum+1]  #if undo is pressed, the entier polygon disappears
                points = []     #
                ptnum = 0       #Reset the tool for next polygon/use
            screen.set_clip(None)

        else:
            if len(points) > 2:  #completing the polygon if another tool is selected
                draw.line(screen,currentc,points[0],points[-1],3)
                undo = undo[:-ptnum+1]  #
            points = []                 #Same as above
            ptnum = 0                   #
#-------------------CURRENT COLOUR--------------------------------             
    #current colour
        if canvasRect.collidepoint(nmx,nmy) or cspectrum.collidepoint(nmx,nmy):
            colour = screen.get_at((nmx,nmy))
            draw.circle(screen,(colour),(617,681),(32)) #current colour
            if cspectrum.collidepoint(nmx,nmy):
                if mb[0] == 1: currentc = colour
                if mb[2] == 1: eraserc = colour
            draw.circle(screen,(currentc),(617,681),(25)) #selected colour
            draw.circle(screen,(eraserc), (617,681), (14)) #eraser colour
#--------------------------STRAX FIELD REPORT---------------------
    #Current Tool
        ctoolPic = courier.render(tools, True,(88,113,142))
        for i in range(3):
            screen.blit(patchup,(1030+i*50,355))
        screen.blit(ctoolPic,(1030,355))
    #Current Size
        if sizeflag: sizePic = courier.render(str(size),True,(88,113,142))
        else: sizePic = courier.render("N/A", True, (88,113,142))
        screen.blit(patchup,(1030,395))
        screen.blit(sizePic,(1030,395))
    #current song
        songPic = courier.render(songt.lower(),True,(88,113,142))
        if musicS == "start":
            for i in range(3): screen.blit(patchup,(1030+i*50,475))
            screen.blit(songPic,(1030,475))
        else:
            for i in range(3): screen.blit(patchup,(1030+i*50,475))
    #current stamp
        stampPic = courier.render(stamp,True,(88,113,142))
        stampcPic = courier.render("current stamp -", True, straxcolour)
        if stamp != "":
            for i in range(4): screen.blit(patchup,(1030+i*50,495))
            for i in range(4): screen.blit(patchup,(1030+i*50,515))
            screen.blit(stampcPic,(1030,495))
            screen.blit(stampPic,(1030,515))
        else:
            for i in range(4): screen.blit(patchup,(1030+i*50,495))
            for i in range(4): screen.blit(patchup,(1030+i*50,515))
    #current position
        posPic = courier.render(('('+ str(mx) + ',' + str(my)+')'),True,(88,113,142))
        for i in range(5): screen.blit(patchup,(1030+i*40,435))
        screen.blit(posPic,(1030,435))
    display.flip()
quit()

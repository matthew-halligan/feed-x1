virsion_number = 'alpha 0.1.0'
credits_ = '      Programed with Python.\nCreated by 0-Zmaster_ScotlandCode.\n'
#defined for begening
backdropnum = [1, 3] # backdrop number, y button multiplier
buttnselect = [1, 1] #x, y buttons in button grid
notifier = 0 #notification timer in title screen
disforselect = None #distance for selecting
selected = False #ditermens if somthig was selected
seed = None #the code that genorates the world
entryline = 'seed input box'
def notifyed(txt):  #for creating notifications
    c.create_rectangle(1000, 25, 790, 90, fill='white', outline='blue')
    c.create_text(895, 60, text=txt, font=('Courier',13))
def instruct(txt): #for the instructions in the how to play menu
    c.create_rectangle(210, 0, 1000, 750, fill='#8a8a8a', outline='#8a8a8a')
    c.create_text(605, 375, text=txt, font=('Courier',15))

##modules
    
from tkinter import*
import time
import random
tk = Tk()
c = Canvas(tk, width=1000, height=750)
c.pack()
tk.title('''Feed-X''')

#keybinds 

## menu scrolling
def addy (event):#moves selector up the distance for selecting when up arrow is pressed
    if buttnselect [1] > 1:
        c.move(s, 0, -disforselect)
    if event.keysym == 'Up':
        buttnselect [1] -= 1
    if buttnselect [1] < 1:
        buttnselect [1] = 1
c.bind_all('<KeyPress-Up>', addy)

def suby (event):#moves selector down the distance for selecting when down arrow is pressed
    maxnum = backdropnum [1] 
    if buttnselect [1] < maxnum:
        c.move(s, 0, disforselect)
    if event.keysym == 'Down':
        buttnselect [1] += 1
    if buttnselect [1] > maxnum:
        buttnselect [1] = maxnum
c.bind_all('<KeyPress-Down>', suby)

### menu select
def select (event):#selects the option that the selector is selecting
    if event.keysym == 'Return':
        if buttnselect [1] == 2 and backdropnum [0] == 1:
            backdropnum [0] = 2
            backdropnum [1] = 3
        if buttnselect [1] == 9 and backdropnum [0] == 2 or buttnselect [1] == 1 and backdropnum [0] == 1:
            buttnselect [1] = 2
            backdropnum [0] = 3
        if backdropnum [0] > 2:
            global selected
            selected = True
c.bind_all('<KeyPress-Return>', select)

#title screen

##backround
c.create_rectangle(0, 0, 1000, 750, fill="#41da53", outline="#41da53")#1

##selector 1
s = c.create_rectangle(270, 240, 730, 300, fill='yellow', outline='yellow')#2 or #s for selector

##title (Feed-x)
c.create_text(500, 100, text='Feed - X',font=('Courier', 80))#3
c.create_text(860, 735, text='created by 0-Zmaster_ScotlandCode', font=('courier', 10), fill='brown')#4
c.create_text(100, 735, text='virsion: '+ virsion_number, font=('courier', 10), fill='brown')#5 

##play
c.create_rectangle(275, 245, 725, 295, fill='gray', outline='black')#6
c.create_text(500, 267, text='play',font=('Courier', 40))#7

##how to play
c.create_rectangle(275, 445, 725, 495, fill='gray', outline='black')#8
c.create_text(500, 467, text='How to play',font=('Courier', 40))

##credits
c.create_rectangle(275, 645, 725, 695, fill='gray', outline='black')
c.create_text(500, 667, text='credits',font=('Courier', 40))

tk.update()
disforselect = 200

while backdropnum [0] == 1:
    if notifier < 400:
        notifier += 1
    if notifier == 400:
        notifyed('use arrow keys to \n navigate menus \n and enter to select')
        notifier = 2000
    if buttnselect [1] == 3:
        c.create_rectangle(725, 505, 275, 640, fill='blue', outline='yellow')
        c.create_text(505, 585, text=credits_  , font=('Courier', 15), fill='black')
    elif buttnselect [1] == 2:
        c.create_rectangle(725, 505, 275, 640, fill='#41da53', outline='#41da53')
    
                
    tk.update()
    tk.update_idletasks()

    time.sleep(0.025)


#how to play screen
if backdropnum [0] == 2:
    c.create_rectangle(0, 0, 1000, 750, fill='#8a8a8a', outline='#8a8a8a')
    
    ##selector 2
    s = c.create_rectangle(5, 5, 205, 65, fill='yellow', outline='yellow')
    
    ##controls button
    c.create_rectangle(10, 10, 200, 60, fill='grey', outline='black')
    c.create_text(100, 35, text='Controls', font=('Courier', 15))
    
    ##general button
    c.create_rectangle(10, 70, 200, 120, fill='grey', outline='black')
    c.create_text(100, 90, text='General', font=('Courier', 15))

    ##world creation button
    c.create_rectangle(10, 130, 200, 180, fill='grey', outline='black')
    c.create_text(100, 150, text='World creation', font=('Courier', 15))

    ##updates button
    c.create_rectangle(10, 430, 200, 480, fill='grey', outline='black')
    c.create_text(100, 450, text='Updates', font=('Courier', 15))
    
    ##play button #2
    c.create_rectangle(10, 490, 200, 540, fill='grey', outline='black')
    c.create_text(100, 510, text='Play', font=('Courier', 15))
    
    backdropnum [1] = 9
    disforselect = 60
    buttnselect = [0, 1]
    tk.update()

while backdropnum [0] == 2:
    
    if buttnselect [1] == 1: #replace with keybinds at some point
        instruct('               Use W, A, S, and D to move\n(W to go up, A to go left, S to go down, and D to go right)\n\n     Use space to go up a form of virtical transport\n                  (stairs, laters, ect.)\n \n    Right click to use the item that you are holding\n  (bilding, shearing, feeding, etc.)\n\n          left click to attack and break blocks') #replace with keybinds in the future
    if buttnselect [1] == 2:
        instruct('''              you need to take care of your X's.\nthey need to have food, a resting place and they need to be happy.\n(use you sword to shear sheep and turn the wool into a bed for\n the X's. use your axe to cut down trees to make fences to\n contain sheep or make x's a bigger pen that will make them\n happier. pick znapples from znapple vines on trees for food)''')
    if buttnselect [1] == 3:
        instruct('''in the create menu by pressing create you can create a new world\n                       (coming soon)\n    any of the world saves that you have can be acsesed\n           by selecting the world save in the menu\n\n  by pressing shift before enter on a world save you can acses\n           the settings menu for the world save.''')
    if buttnselect [1] == 4 or buttnselect [1] == 7 or buttnselect [1] == 9:
        instruct('')
    if buttnselect [1] == 8:
        instruct('Check your email often for updates!')
    
    tk.update()
    tk.update_idletasks()
    
    time.sleep(0.025)

#world select menu
if backdropnum [0] == 3:
    c.create_rectangle(0, 0, 1000, 750, fill='#41da53')

    #selector 3
    s = c.create_rectangle(190, 60, 810, 120, fill='yellow', outline='yellow')
    
    #create button
    c.create_rectangle(195, 65, 805, 115, fill='gray', outline='black')
    c.create_text(500, 87, text='Create',font=('Courier', 40))

    #world save button 
    c.create_rectangle(195, 180, 805, 230, fill='gray', outline='black')
    c.create_text(500, 202, text='coming soon',font=('Courier', 40))

    #world save button 
    c.create_rectangle(195, 295, 805, 345, fill='gray', outline='black')
    c.create_text(500, 317, text='coming soon',font=('Courier', 40))
    
    #world save button 
    c.create_rectangle(195, 410, 805, 460, fill='gray', outline='black')
    c.create_text(500, 432, text='coming soon',font=('Courier', 40))
    
    #world save button 
    c.create_rectangle(195, 525, 805, 575, fill='gray', outline='black')
    c.create_text(500, 547, text='coming soon',font=('Courier', 40))

    #world create
    wolrd_createor = [c.create_rectangle(0, 575, 1000, 750, fill='#662828'), c.create_text(500, 675, text='''Enter a number to generate the world, or 'x' to go back''', font=('Courier', 15))]
    c.move(wolrd_createor [1], 0, 175)
    c.move(wolrd_createor [0], 0, 175)
    c.pack()
    
    backdropnum [0] = 3
    buttnselect [1] = 1
    backdropnum [1] = 5
    disforselect = 115
    selected = False

#the world defined section
##world saves
class worlds:
    pass


while backdropnum [0] == 3:
    
    
    if buttnselect [1] == 2 and selected == True and seed == None:
        selected = False
        
    elif buttnselect [1] == 1 and selected == True and seed == None:
        c.move(wolrd_createor [0] , 0, -175)
        c.move(wolrd_createor [1] , 0, -175)
        entryline = Entry(tk, width=50, borderwidth=4, bg='grey')
        entryline.pack()
        selected = False
    try :
        seed = entryline.get()
    except AttributeError:
        seed = seed
        
    if seed != None and selected == True:
            try:
                seed = int(seed)
                backdropnum [0] = 4
            except ValueError:
                c.move(wolrd_createor [0] , 0, 175)
                c.move(wolrd_createor [1] , 0, 175)
                entryline.destroy()
                entryline = None
                seed = None
                selected = False
    
    
    
    tk.update()
    tk.update_idletasks()
    
    time.sleep(0.025)


#the real defined section

notifier = 0
entryline.destroy()
entryline = None

##mobs

#pre-defined mobs      #
class x:
    def create(self, LeftFace = None):#x and y peramiters will not be here due to the goto command
        #       #          #          #it's eaiser to code and is more usefl
        if LeftFace != None:#the x looking left
            self.xbase = c.create_oval(488, 360, 513, 385, fill='green', outline='green')
            self.xmouth = c.create_polygon(498, 373, 489, 368, 489, 380, fill='black')
            self.xfoot = c.create_polygon(505, 385, 501, 385, 501, 388, 498, 392, 505, 392, fill='green', outline='black')
            self.xtail = c.create_polygon(513, 371, 518, 382, 506, 380, fill='green')
            self.xeye = c.create_oval(502, 363, 496, 369, fill='white')
            self.xi = c.create_oval(500, 366, 498, 368, fill='black')
            self.xibrow = c.create_rectangle(500, 363, 498, 363, fill='green', outline='green')
            c.pack()
            self.costume = 2
        else:#the x looking right
            self.xbase = c.create_oval(488, 360, 513, 385, fill='green', outline='green')
            self.xmouth = c.create_polygon(503, 373, 513, 368, 513, 380, fill='black')
            self.xfoot = c.create_polygon(496, 385, 500, 385, 500, 388, 503, 392, 496, 392, fill='green', outline='black')
            self.xtail = c.create_polygon(488, 371, 483, 382, 495, 380, fill='green')
            self.xeye = c.create_oval(499, 363, 505, 369, fill='white')
            self.xi = c.create_oval(501, 366, 503, 368, fill='black')
            self.xibrow = c.create_rectangle(501, 363, 503, 363, fill='green', outline='green')
            c.pack()
            self.costume = 1
        #position of x
        self.x = 500
        self.y = 375
    def move(self, x, y, SwitchCostume = None):#makes the x move
        c.move(self.xbase, x, y)
        c.move(self.xmouth, x, y)
        c.move(self.xfoot, x, y)
        c.move(self.xtail, x, y)
        c.move(self.xeye, x, y)
        c.move(self.xi, x, y)
        c.move(self.xibrow, x, y)
        tk.update()
        self.x += x
        self.y += y
        if SwitchCostume == None:
            if x < 0 and self.costume == 1:
                self.costumes('left')
            elif x > 0 and self.costume == 2:
                self.costumes('right')
    def costumes(self, direction):#changes the direction the x faces
        self.tempx = self.x
        self.tempy = self.y
        if direction == 'left':
            self.costume = None
            self.move(1500, 0)
            self.create(1)
            self.goto(self.tempx, self.tempy)
            self.costume = 2
        if direction == 'right':
            self.costume = None
            self.move(1500, 1500)
            self.create()
            self.goto(self.tempx, self.tempy)
            self.costume = 1
    def goto(self, x, y, curX = None, curY = None):#moves the x to a location that is specified
        if curY != None and curX != None:
            curX = self.tempx
            curY = self.tempy
        else:
            curX = self.x
            curY = self.y
        self.move(x-curX, y-curY, 1)
    def jump(self, DisForX, DisForY):
        pass
    

class player:
    def render(self, x = None, y = None):
        pass
    def move(self, x, y, SwitchCostume = None):
        pass
    def costumes(self, direction):
        pass
#c.create_rectangle(190, 182, 210, 208, fill='red')#shirt
#c.create_polygon(190, 182, 183, 182, 183, 199, 188, 199, 188, 192, fill='red', outline='black')#left arm
#c.create_polygon(210, 182, 217, 182, 217, 199, 212, 199, 212, 192, fill='red', outline='black')#right arm
#c.create_rectangle(198, 179, 202, 185, fill='#e4bd83')#neck
#c.create_rectangle(194, 180, 206, 165, fill='#e4bd83')#head
#c.create_polygon(190, 208, 210, 208, 210, 230, 203, 230, 203, 214, 197, 214, 197, 230, 190, 230, fill='#7077a5', outline='black')#legs    

#random-spawning mobs                 #
class mobs:
    pass
class peacemobs(mobs):
    pass
class meanmobs(mobs):
    pass
##blocks
class blocks:
    def brake(self):#might want to add particles for breaking blocks
        pass
    def place(self):
        pass
class fence(blocks):
    pass
class xbed(blocks):
    pass
class znapplesap(blocks):
    pass
##terrain
tree_list = []
class tree(blocks):
    def trunk(self, x, y):
        self.base = c.create_rectangle(x-6, y, x+6, y-40, fill='brown', outline='brown')
    def leaves(self, x, y):
        self.leaf = c.create_oval(x-17, y-33, x+17, y-65, fill='#2ea432', outline='#2ea432')
    def create(self, x, y, again = None):
        self.trunk(x, y)
        self.leaves(x, y)

class znappletree(tree):
    def leaves(self, x, y):
        self.leaf = c.create_oval(x-15, y, x+1, y+5, fill='#2f624e', outline='#2f624e')#2f624e
    def costumes(self, stagenum):
        pass
    
#seed calculations
print('seed: ' + str(seed))
while seed > 9999999:
    seed /= 10
    seed = int(seed)
    
while seed < 999999999999999:
    seed = ((seed*10) + seed%9)
    notifier += 1
    if notifier == 10:
        seed = (seed*10) + seed**2
        
while seed > 999999999999999:
    seed /= 10
    seed = int(seed)

seed = str(seed)
notifier = seed.find('0')
seed = seed.split('0')
seed = str(notifier).join(seed)
print('genoration code: ' + str(seed))
#???seed = int(seed)???

#play screen
c.create_rectangle(0, 0, 1000, 750, fill='#41da53', outline='#41da53')
###
c.create_line(0, 375, 1000, 375)
c.create_line(500, 0, 500, 750)
tree_list.append(tree())
tree_list[0].create(300, 300)
player = player()

tk.update()
###
#x's
freed = x()
freed.create()

dexter = x()
dexter.create()

#toolbar selection

while backdropnum [0] == 4:
    print('h')
        
    
    tk.update()
    tk.update_idletasks()
    
    time.sleep(0.025)

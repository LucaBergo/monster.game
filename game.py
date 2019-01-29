from random import randint
import os


class Entity:
	def __init__ (self,x,y,graphic):
		self.x=x
		self.y=y
		self.graphic=graphic


	def move (self,direction):
		if direction == "N":
			self.y -= 1
		elif direction == "S":
			self.y += 1
		elif direction == "E":
			self.x+=1
		elif direction == "W":
			self.x-=1


class Player(Entity):
	def __init__ (self,x,y, graphic,cur_hp, max_hp):
		Entity.__init__(self, x, y, graphic)
		self.cur_hp=cur_hp
		self.max_hp=max_hp



class Enemy(Entity):
	def __init__ (self, x ,y, graphic,damage):
		Entity.__init__(self, x ,y, graphic)
		self.damage=damage


	def attack(self, target):
		target.cur_hp-=self.damage



class Gold(Entity):
	def __init__ (self, x ,y, graphic):
		Entity. __init__ (self,x,y, graphic)


#class World:
#	def __init__(self, height , width):
#		self.height=height 
#		self.width=width
#
#
#
#	def campo(self):
#		#print("["+Entity.graphic+"]", end="")
#
#		print("["+p1.graphic+"]", end="")
#		print("["+m.graphic+"]", end="")
#		print("["+g.graphic+"]", end="")
#






p1 = Player (0,0,"P",100,100)
m = Enemy (randint(1,4), randint(1,4), "M", 40)
g = Gold (5, 5, "T")
#level1= World(6,6)


while True:
	os.system("cls")
	z=randint(1,4)
	print()
	print("              Developed by Luca Bergognoni       ")
	print()
	print()
	#level1.campo()
	
	command=input().lower()
	if command=="w":
		p1.move("N")
	elif command=="s":
		p1.move("S")
	elif command=="a":
		p1.move("W")
	elif command=="d":
		p1.move("E")
	elif command== "b":
		break

	if z==1:
		m.move("N")
	elif z==2:
		m.move("S")
	elif z==3:
		m.move("W")
	elif z==4:
		m.move("E")


	if p1.x==m.x:
		if p1.y==m.y:
			m.attack(p1)


	if p1.cur_hp<=0:
		print("GAME OVER")
		exit()


	if p1.x==g.x:
		if p1.y==g.y:
			print("YOU WON")
			exit()








		
	
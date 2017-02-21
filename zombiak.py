import json
import random
class Weapon:
	def __init__(self,name,damage,count,max_count):
		self.name = name
		self.damage = damage
		self.count = count
		self.max_count = max_count

class Character :
	def __init__(self,name,hp,damage):
		self.name = name
		self.hp = hp
		self.damage = damage
	
	def attack(self,victim):
		victim.hp -= self.damage
		print("{0.name} нанёс {1.name} {0.damage} урона".format(self,victim))

class Zombie(Character):
	pass

class Player(Character):

	def __init__(self,name,hp,damage,weapons):
		super().__init__(name,hp,damage)
		self.weapons = weapons
	
	def show_weapons(self):
		print("У вас имеются:")
		for num, weapons in enumerate(self.weapons):
			print("{0}.{1.name}, Урон:{1.damage}, Колличество:{1.count}".format(num, weapons))

	def choose_weapon(self):
		self.damage = 0
		while True:
			try:
				w= int(input("введите номер оружия: "))
				if w in range(len(self.weapons)):
					self.damage = self.weapons[w].damage
					self.weapons[w].count -= 1
					if self.weapons[w].count <= 0:
						self.weapons.pop(w)
					break
				print("Введите номер существующего оружия")
			except ValueError:
				print("Введите число")

class Game:
	def load_config(self):
		with open("config.json","rt",encoding="utf-8") as f:
			return f.read()

	def load_zombie(self):
		with open("zombie.json","rt",encoding="utf-8") as d:
			return d.read()

	def get_weapons(self, conf):
		weapons = json.loads(conf)["weapons"]
		print(weapons)
		return [Weapon(name,ch['damage'],0,ch['count'])
			for name, ch in weapons.items()]

	def give_weapon(self,player):
		if not random.randint(0,3):
			this_weapon = random.choice(self.weapons)
			this_weapon.count += this_weapon.max_count
			if this_weapon not in player.weapons:
				player.weapons.append(this_weapon)
			print(this_weapon.name,"получено")

	def start(self):
		conf = self.load_config()
		self.weapons = self.get_weapons(conf)
		weapon = Weapon("SUperPuper",5,555,555)
		player = Player("Кадырл",1000,100,[weapon])
		zombie = Zombie("Аркадий паравозов", 500, 50)
		count = 0
		while True:
			self.give_weapon(player)
			player.show_weapons()
			player.choose_weapon()
			player.attack(zombie)
			zombie.attack(player)
			input()
			if player.hp <= 0 :
				print("Ты умер !!! и получил {0} очков".format(count))
				break
			if zombie.hp <= 0 :
				zombie = Zombie("Аркадий паравозов", 500, 50)
				count += 1
				print("Ты убил зомби")

game = Game()
game.start()
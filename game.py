import cocos
from cocos.actions import *
import player

class bgLayer(cocos.layer.ColorLayer):
	def __init__(self):
		super(bgLayer, self).__init__(64,64,224,255)
		self.player = player
		label = cocos.text.Label('Dueling Simulator',
			font_name='Times New Roman',
			font_size=32,
			anchor_x='center', anchor_y='center')
		label.position = 800,850
		self.add(label)
		scale = ScaleBy(1.1, duration=2)
		label.do(Repeat(scale + Reverse(scale)))

class cardLayer(cocos.layer.Layer):
	def __init__(self, player):
		super(cardLayer, self).__init__()
		self.player = player
		self.displayHand()

	def displayHand(self):
		hand = self.player.hand
		for i in range(len(self.player.hand)):
			self.displayCard(hand[i], i)

	def displayCard(self, card, hand_slot):
		card_bg = cocos.sprite.Sprite("cards/cardtemp.png")
		card_bg.position = ((hand_slot * 210+300), 146)
		self.add(card_bg)
		name = self.createLabel(card.name)
		name.position = (card_bg.x-90, card_bg.y+126)
		attack = self.createLabel(card.attack)
		attack.position = (card_bg.x+32, card_bg.y-79)
		defense = self.createLabel(card.defense)
		defense.position = (card_bg.x+32, card_bg.y-99)
		self.add(name)
		self.add(attack)
		self.add(defense)

	def createLabel(self, info):
		label = cocos.text.Label(str(info),
			font_name='Times New Roman',
			font_size=12,
			color=(0,0,0,255),
			anchor_x='left', anchor_y='top')
		return label


cocos.director.director.init(1600, 900)
player1 = player.Player("Yugi", [1, 2, 3, 4])
player1.startGame()
bgLayer = bgLayer()
hello_layer = cardLayer(player1)

main = cocos.scene.Scene(bgLayer, hello_layer)

cocos.director.director.run(main)
import constants as C
import player, actions, field

## Here is hjow turns will be handled, not sure how to have it switch between players yet

class Turn():
	def __init__(self):
		self.actions = []

	def push(self, phase):
		self.actions.append(phase)

	def pop(self):
		self.actions.pop()

	def is_empty(self):
		return (self.actions == [])


'''
Each phase has a list of possible actions. The phase object will check the validity of any action passed to it by the game controller
'''
class Phase():
	def __init__(player):
		self.player = player
		self.actions = []

	def phase():
		pass

	def checkValidity(self, action):
		return action in self.actions # Hopefully this works

class DrawPhase(Phase):
	def phase(self, player):
		self.actions.append(actions.DrawCard(self.player))

class MainPhase(Phase):
	def summon(index):


class BattlePhase(Phase):
	pass

class GameController():
	def __init__(self, player1, player2):
		self.player1 = player.Player(player1, [])
		self.player2 = player.Player(player2, [])
		self.turn = Turn()
		self.phases = [1, 2, 3, 4]
		self.turnLog = []
		self.turnPlayer = player1


	def gameStart():
		player1.shuffleDeck()
		player1.drawCard(3)
		player2.shuffleDeck()
		player2.drawCard(3)

	def runTurn():


		
class MCTSNode(object):
	def __init__(self, game_state, parent=None, move=None):
		self.game_state = game_state
		self.parent = parent
		self.move = move
		self.win_counts = {
		Player.black: 0,
		Player.white: 0,
		}

class Power:

	def __init__(self, name=None, rule=None, colour=None):
		if not name or not rule or not colour:
			raise InvalidPowerArgs
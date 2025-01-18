class Attack:
	def __init__(self, damage, acc, use_text, target_type, debuff=None, debuff_stack_amount=0, sound='hit'):
		self.damage = damage
		self.acc = acc
		self.use_text = use_text
		self.target_type = target_type
		self.debuff = debuff
		self.debuff_stack_amount = debuff_stack_amount
		self.sound = sound

from modulos import *
class Validadores:
	def validateCod(self, text):
		if text == "": return True
		try:
			value = int(text)
		except ValueError:
			return False
		return 0 <= value <= 10000
	def validate60(self, text):
		return len(text) < 61
	def validate20(self, text):
		return len(text) < 21
	def validate100(self, text):
		return len(text) < 101
	def validate10(self, text):
		return len(text) < 11

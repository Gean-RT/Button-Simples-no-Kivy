from kivy.app import App
from kivy.uix.button import Button

class BSimples(App):
	def build(self):
		button = Button(text='Olá Mundo!')
		return button

BSimples().run()

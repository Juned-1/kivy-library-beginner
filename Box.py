from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
class BoxLayoutExample(BoxLayout):
    pass
class Box(App):
    def build(self):
        return BoxLayoutExample()
Box().run()
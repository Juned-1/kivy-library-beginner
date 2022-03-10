from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
class AnchorLayoutExample(AnchorLayout):
    pass
class Anchor(App):
    def build(self):
        return AnchorLayoutExample()
Anchor().run()
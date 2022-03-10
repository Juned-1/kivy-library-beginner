#It is stacking layout inside layout
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
class BoxLayoutExample(BoxLayout):
    pass
class EmbedLayout(App):
    def build(self):
        return BoxLayoutExample()
EmbedLayout().run()
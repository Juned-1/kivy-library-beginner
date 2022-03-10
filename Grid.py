from kivy.app import App
from kivy.uix.gridlayout import GridLayout
class GridLayoutExample(GridLayout):
    pass
class Grid(App):
    def build(self):
        return GridLayoutExample()
Grid().run()
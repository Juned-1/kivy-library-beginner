from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
class Demo(GridLayout):
    pass
class MyFirstApp(App):
    def build(self):
        return Demo()
MyFirstApp().run()
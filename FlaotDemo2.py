import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.config import Config
Config.set('graphics','resizable',True)
class FlaotDemo(FloatLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.btn1=Button(
            text="Button 1",
            size_hint=(0.2,0.1),
            pos=(100,100)
        )
        self.add_widget(self.btn1)
        self.btn2=Button(
            text="Button 2",
            size_hint=(0.2,0.1),
            pos=(100,200)
        )
        self.add_widget(self.btn2)
class DemoApp(App):
    def build(self):
        return FlaotDemo()
DemoApp().run()
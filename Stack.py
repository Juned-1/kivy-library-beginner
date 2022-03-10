from kivy.app import App
from kivy.uix.stacklayout import StackLayout
from kivy.uix.button import Button
from kivy.metrics import dp
class StackLayoutExample(StackLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        #self.orientation= "rl-bt"
        #self.padding=("20dp","20dp", "20dp", "20dp")
        #self.spacing=("20dp","20dp")
        for i in range(0,10):
            si=dp(100)+i*10 #si is local variable
            b=Button(
                text=str(i+1),
                #size_hint=(.2,.2)
                size_hint=(None,None),
                #size=(dp(100),dp(100))
                size=(si,si)
            )
            self.add_widget(b)
class Stack(App):
    def build(self):
        return StackLayoutExample()
Stack().run()
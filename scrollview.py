from kivy.app import App 
from kivy.uix.stacklayout import StackLayout
from kivy.uix.button import Button
from kivy.metrics import dp
class sc(StackLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        for i in range(401):
            b = Button(
                text = str(i+1),
                size_hint = (None,None)
            )
            self.add_widget(b)
class scrollview(App):
    def build(self):
        return sc()
scrollview().run()
from kivy.app import App
from kivy.uix.pagelayout import PageLayout
from kivy.uix.button import Button
class PageDemo(PageLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.btn1=Button(
            text="Button 1",
            size_hint=(0.5,0.5)
        )
        self.add_widget(self.btn1)
        self.btn2=Button(
            text="Button 2",
            size_hint=(0.5,0.5)
        )
        self.add_widget(self.btn2)
        self.btn3=Button(
            text="Button 3",
            size_hint=(0.5,0.5)
        )
        self.add_widget(self.btn3)
class DemoApp(App):
    def build(self):
        return PageDemo()
DemoApp().run()
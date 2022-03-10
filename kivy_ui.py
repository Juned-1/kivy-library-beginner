from kivy.app import App
from  kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.image import Image
class kivy_ui(GridLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.cols=1
        self.rows=4
        self.img=Image(
            source="/home/junaid/Downloads/pexels-pixabay-326055.jpg"
        )
        self.add_widget(self.img)
        self.lbl=Label(
            text="Enter your name"
        )
        self.add_widget(self.lbl)
        self.txt=TextInput(
            text="",font_size=40 #40 px font size
        )
        self.add_widget(self.txt)
        self.btn=Button(
            text="Submit"
        )
        self.add_widget(self.btn)
        self.pop=Popup(
            title="Pop-up Display",
            size=(400,400), #tuple contain value
            content=Label(
                text=""
            )
        )
        self.bind(on_click=self.call_back)
    def call_back(self,elem):
        self.pop.content.text=self.txt.text
        #copy text of Text widget to pop up content
        self.pop.open() #open method call Pop-Up
class DemoApp(App):
    def build(self):
        return kivy_ui()
DemoApp().run()
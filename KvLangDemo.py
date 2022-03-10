from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.widget import Widget
class Demo(Widget):
    name=ObjectProperty(None) #argument passing is none
    age=ObjectProperty(None)
    def onClick(self):
        print("My name is {} and I'm {} year old!".format(self.name.text,self.age.text))
        self.name.text="" #renitializing value
        self.age.text=""
class MyFirstApp(App):
    def build(self):
        return Demo()
MyFirstApp().run()
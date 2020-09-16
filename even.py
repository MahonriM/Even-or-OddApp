import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid,self).__init__(**kwargs)
        self.cols=1
        self.inside=GridLayout()
        self.inside.cols=2
        self.inside.add_widget(Label(text="Introduce a number"))
        self.num1=TextInput(multiline=False)
        self.inside.add_widget(self.num1)
        self.evod=(Label(text=""))
        self.inside.add_widget(self.evod)
        self.add_widget(self.inside)
        self.submit=Button(text="Even/Odd",font_size=20)
        self.submit.bind(on_press=self.func)
        self.add_widget(self.submit)
    def func(self,instance):
        num=int(self.num1.text)
        if num%2==0:
            self.evod.text=("Even")
        else:
            self.evod.text=("Odd")
class MyApp(App):
    def build(self):
        return MyGrid()
if __name__=="__main__":
    MyApp().run()
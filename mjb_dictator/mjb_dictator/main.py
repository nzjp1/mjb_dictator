import dictator as d
import pyautogui as pya

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.properties import NumericProperty, ReferenceListProperty
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout

#initialising the models&microphones
r = d.Recognizer()
m = d.Microphone()


class Container(Widget):
    #override __init__ to add buttons
    def __init__(self, **kwargs):
        super(Container, self).__init__(**kwargs)
        btn1 = Button(text='Hello World 1')
        btn1.bind(on_press=self.callback)
        self.add_widget(btn1)

    def callback(self, instance):
        print('The button %s state is <%s>' % (instance, instance.state))

class DictatorApp(App):
    def build(self):
        app = Container()
        return app


if __name__ == '__main__':
    DictatorApp().run()


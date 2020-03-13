from kivy.app import App
from kivy.base import runTouchApp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.metrics import dp
from kivy.lang.builder import Builder
from kivy.garden.navigationdrawer import NavigationDrawer

Builder.load_string('''
<NavigationDrawer>:
    size_hint: (1,1)
    side_panel_width: min(dp(250), 0.8*self.width)
''')


class ExampleApp(App):

    def build(self):

        navigationdrawer = NavigationDrawer()

        side_panel = BoxLayout(orientation='vertical')
        side_panel.add_widget(Label(text='Panel label'))
        side_panel.add_widget(Button(text='A button'))
        side_panel.add_widget(Button(text='Another button'))
        navigationdrawer.add_widget(side_panel)
        main_panel = BoxLayout(orientation='vertical')

        navigationdrawer.add_widget(main_panel)

        return navigationdrawer


ExampleApp().run()

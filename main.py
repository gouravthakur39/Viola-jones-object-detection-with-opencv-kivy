import os
from kivymd.app import MDApp
from kivymd.theming import ThemeManager
from kivy.uix.boxlayout import BoxLayout
from kivymd.toast.kivytoast.kivytoast import toast
from kivy.utils import get_hex_from_color

from kivymd.uix.dialog import  MDDialog
# NavigationDrawer
from kivy.properties import StringProperty

from kivymd.uix.list import OneLineAvatarListItem

class ContentNavigationDrawer(BoxLayout):
    pass

class NavigationItem(OneLineAvatarListItem):
    icon = StringProperty()

class RootWidget(BoxLayout):
    pass

class MainApp(MDApp):
    # __init__ is a special method in Python classes, it is the constructor method for a class.
    # The self is used to represent the instance of the class. With this keyword, you can 
    # access the attributes and methods of the class in python
    # *args(non keyboard argument) and *kwargs(keyboard argument) are special keyword which allows 
    # function to take variable length argument.
    def __init__(self, **kwargs):
        self.title = "Viola Jones object detection framework"
        self.theme_cls = ThemeManager()
        self.theme_cls.primary_palette = "Indigo"
        self.theme_cls.accent_palette = "Teal"
        self.theme_cls.theme_style="Light"

        # The super() function is used to give access to methods and properties of a parent or sibling class.
        super().__init__(**kwargs)
    
    
    def build(self):
        return RootWidget()
    
    def back_to_home_screen(self):
        self.root.ids.person_name.text = ""
        self.root.ids.person_id.text = ""
        self.root.ids.screen_manager.current = "HomeScreen"
    
    def show_ExitDialog(self):
        dialog = MDDialog(
            title="Viola Jones object detection framework", 
            text = "Are you [color=%s][b]sure[/b][/color] ?"
            % get_hex_from_color(self.theme_cls.primary_color), 
            size_hint=[.5, .5],
        events_callback=self.stopApp,
        text_button_ok="Exit",
        text_button_cancel="Cancel"
        )
        dialog.open()
    
    def stopApp(self, text_of_selection, popup_widget):
        
        if text_of_selection == "Exit":
            self.stop()
        else:
            pass
    
    def performDetection(self):
        # os. system() method execute the command (a string) in a subshell
        os.system("python faceRecognition.py")
    
    def captureTrainingImages(self, person_name, person_id, screen_manager):
        
        print(len(person_name), len(person_id))
        if len(person_name) > 0 and len(person_name) <= 23 and len(person_id) > 0 and len(person_id) <= 6:
            os.system("python captureTrainingImages.py {} {}".format(person_name, person_id))
            toast("Training Images Collected.")
            screen_manager.current = "HomeScreen"
        else:
            toast("Please Enter Correct Details.")

MainApp().run()

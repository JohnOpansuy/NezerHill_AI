#Підключення модулів.
from kivy.app import App
from kivy.core.window import Window
from kivy.graphics import Rectangle
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.animation import Animation
from kivy.utils import get_color_from_hex
from kivy.uix.popup import Popup
from kivy.uix.progressbar import ProgressBar
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.checkbox import CheckBox
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from colorama import Back, Fore
import os
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'

#Клас скрін1/головний екран.
class Scrin_1 (Screen):
#Деф конструктор викликається при створенні скрін1.
    def __init__ (self, **kwargs):
#Виклик батьківського класу скріін.
        super (Scrin_1, self).__init__ (**kwargs)
#Встановлюємо розмір вікна.
        Window.size = (1000, 575)
        Window.top = 100
        Window.left = 200
#Відкриття контекстного менеджера для відображення позаду зображення.
        #?with self.canvas.before:
#Створення прямокутника.
            #?self.bg = Rectangle (source = "OIG3.jpg", size = (1900, 1400), pos = self.pos)
#Створення направних ліній.
        widget_1 = BoxLayout (orientation = "vertical") #Створення віджету1.
        horithontal_1_2 = BoxLayout (orientation="horizontal", size_hint = (None, None), height = 88, pos_hint = {"center_x": 0.88, "center_y": 0}, padding = 4)
#\Створення кнопок.
        self.button_1 = Button (text = "Продовжити", size_hint = (0.4, 0), pos_hint = {"center_x": 0.5, "center_y": 0.2}, color = (0, 0, 0, 1), background_color = ("1B8191"), background_normal = "")
#-!        self.button_1.disabled = True #Блокування кнопки.
#Додавання до віджету ліній.
        widget_1.add_widget (horithontal_1_2)
#Додавання до селфу віджету.
        self.add_widget (widget_1)
    def go_to_scrinusers (self, instance):
#Встановлення анімації.
        self.manager.transition = SlideTransition (direction = "down")
#Вибір на який екран переходити.
        self.manager.current = ("Збережені користувачі")
#Деф відкриття спливаючого вікна.
    def show_popup (self, message):
#Створення направляючої лінії.
        # Створення направляючої лінії.
        popup_layout = BoxLayout(orientation='vertical', padding=10)
        # Створення лейблу.
        popup_label = Label(text=message)
        # Створення кнопки.
        close_button = Button(text="Закрити", size_hint=(1, 0.2))
        # Додавання до ліній інтерфейсу.
        popup_layout.add_widget(popup_label)
        popup_layout.add_widget(close_button)
        # Створення спливаючого вікна (popup).
        popup = Popup(title="Результат перевірки", content=popup_layout, size_hint=(0.8, 0.4))
        # Створення закриття кнопки.
        close_button.bind(on_press=popup.dismiss)
        # Запуск кнопки.
        popup.open()
#.

#.

#.

#.

#.

#.

#.

#.

#Клас Майап.
class MyApp (App):
#Деф конструктор Майап.
    def __init__ (self, **kwargs):
        super (MyApp, self).__init__ (**kwargs)
# Встановлюємо імя вікна.
        self.title = ("AI-Chat")
#Деф СкрінМенеджер.
    def build (self):
        scrinmanager = ScreenManager() #Створення скрінменеджера.
        scrinmanager.add_widget (Scrin_1 (name = "Екран1")) #Додавання до скрінменеджера вікна.
#Встановлення Scrin_1 як стартового екрану.
        scrinmanager.current = ("Екран1")
#Запуск екраногоменеджера.
        return scrinmanager
#Запуск програми.
if __name__ == "__main__":
    MyApp().run()

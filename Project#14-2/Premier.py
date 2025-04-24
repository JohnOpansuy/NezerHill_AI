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
from Information_test import text_vstyp, text_name_1, text_age, krok_1, krok_1_1, krok_2_1, krok_3_1, krok_3_2, krok_3_3
from Sums_test import sums_rufye, Stanserca
#\Створення лист_1/лист_2 для зберігання даних користувача та віджету/горизонтальної лінії для додавання скрінюзерс.
list_1 = dict()
widget_u = BoxLayout (orientation = "vertical")
horithontal_2_5_2 = BoxLayout (orientation = "horizontal")
ryadok_1 = TextInput (hint_text = "Введіть імя", size_hint = (1, 0.4), pos_hint = {"center_x": 0.5, "center_y": 0.2}, multiline = False, background_color = ("1E90A2"), foreground_color = (0, 0, 0, 1), hint_text_color = (0, 0, 0, 1))
ryadok_2 = TextInput (hint_text = "Введіть вік", size_hint = (1, 0.4), pos_hint = {"center_x": 0.5, "center_y": 0.2}, multiline = False, background_color = ("1E90A2"), foreground_color = (0, 0, 0, 1), hint_text_color = (0, 0, 0, 1))
#/.
#Клас скрін1/головний екран.
class Scrin_1 (Screen):
#Деф конструктор викликається при створенні скрін1.
    def __init__ (self, **kwargs):
#Виклик батьківського класу скріін.
        super (Scrin_1, self).__init__ (**kwargs)
#Встановлюємо розмір вікна.
        Window.size = (950, 700)
#Відкриття контекстного менеджера для відображення позаду зображення.
        with self.canvas.before:
#Створення прямокутника.
            self.bg = Rectangle (source = "OIG3.jpg", size = (1900, 1400), pos = self.pos)
#Створення направних ліній.
        widget_1 = BoxLayout (orientation = "vertical") #Створення віджету1.
        vertical_1m = BoxLayout (orientation = "vertical", padding = 4, spacing = 4)
        vertical_1_2m = BoxLayout (orientation = "vertical", padding = 40, spacing = 4)
        horizontal_1 = BoxLayout (orientation = "horizontal", padding = 100, spacing = 4)
        horizontal_1_1 = BoxLayout (orientation = "horizontal", padding = 100, spacing = 4)
        horithontal_1_2 = BoxLayout (orientation="horizontal", size_hint = (None, None), height = 88, pos_hint = {"center_x": 0.88, "center_y": 0}, padding = 4)
#\Створення кнопок.
        self.button_1 = Button (text = "Продовжити", size_hint = (0.4, 0), pos_hint = {"center_x": 0.5, "center_y": 0.2}, color = (0, 0, 0, 1), background_color = ("1B8191"), background_normal = "")
#-!        self.button_1.disabled = True #Блокування кнопки.
#Присвоєння нажаття кнопки до екрану2.
        self.button_1.bind (on_press = self.go_to_scrin2) 
        self.button_2 = Button (text = "Користувачі", size_hint = (None, None), size = (250, 75), color = (0, 0, 0, 1), background_color = ("1B8191"), background_normal = "")
        self.button_2.bind (on_press = self.go_to_scrinusers)
#Створення текстінпутів.
#Створення курсора на першому рядку.
        ryadok_1.focus = True
        ryadok_1.bind (text = self.on_text_change_1) #Обробник змін тексту
        ryadok_2.bind (text = self.on_text_change_1)
#/Додавання до ліній інтерфейсу.
        horithontal_1_2.add_widget (self.button_2)
        vertical_1m.add_widget (text_vstyp)
        horizontal_1.add_widget (text_name_1)
        horizontal_1.add_widget (ryadok_1)
        horizontal_1_1.add_widget (text_age)
        horizontal_1_1.add_widget (ryadok_2)
        vertical_1_2m.add_widget (self.button_1)
#Додавання до віджету ліній.
        widget_1.add_widget (horithontal_1_2)
        widget_1.add_widget (vertical_1m)
        widget_1.add_widget (horizontal_1)
        widget_1.add_widget (horizontal_1_1)
        widget_1.add_widget (vertical_1_2m)
#Додавання до селфу віджету.
        self.add_widget (widget_1)
#Деф перевірка заповнення рядків.
    def on_text_change_1 (self, instance, value):
        input_text_1 = ryadok_1.text
        input_text_2 = ryadok_2.text
        
        if input_text_1 and input_text_2:  # Якщо обидва текстові поля не порожні
            self.button_1.disabled = False  # Розблокування кнопки
        else:
            self.button_1.disabled = True  # Блокування кнопки
    def go_to_scrinusers (self, instance):
#Встановлення анімації.
        self.manager.transition = SlideTransition (direction = "down")
#Вибір на який екран переходити.
        self.manager.current = ("Збережені користувачі")
#Деф переходу до скрін2.
    def go_to_scrin2 (self, instance):
        input_text_1 = ryadok_1.text
        input_text_2 = ryadok_2.text
        if input_text_1.isalpha() and input_text_2.isdigit():
            self.manager.transition = SlideTransition(direction="left")
            self.manager.current = "Введеня другого етапу"
            global ryadok_1_text_1
            global ryadok_2_text_1
            global ryadok_1_btn
            ryadok_1_text_1 = ryadok_1.text  # Отримуєм текст з рядка1.
            ryadok_1_btn = self.button_1
            ryadok_2_text_1 = ryadok_2.text  # Отримуєм текст з рядка2.
        else:
            self.show_popup("Введіть букви в перше поле та цифри в друге поле")
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
#Клас скрін2 введення даних1.
class Scrin_2 (Screen):
#Деф конструктор.
    def __init__ (self, **kwargs):
        super (Scrin_2, self).__init__ (**kwargs)
#Встановлюємо розмір вікна.
        Window.size = (950, 700)
#Відкриття контекстного менеджера для відображення позаду зображення.
        with self.canvas.before:
#Створення прямокутника.
            self.bg = Rectangle (source = "OIG3.jpg", size = (1900, 1400), pos = self.pos)
#Створення направних ліній.
        widget_2 = BoxLayout (orientation = "vertical")
        vertical_2_1m = BoxLayout (orientation = "horizontal", padding = 4, spacing = 4)
        vertical_2_2m = BoxLayout (orientation = "horizontal", padding = 4, spacing = 4)
        horithontal_2_1 = BoxLayout (orientation = "horizontal", padding = 4 ,  spacing = 4 ) 
        horithontal_2_2 =  BoxLayout (orientation = "horizontal", size_hint = (1, None), height = 50)
        horithontal_2_3 = BoxLayout (orientation = "horizontal", padding = 200, spacing = 4)
        horithontal_2_4 = BoxLayout (orientation = "horizontal", padding = 4, spacing = 4)
#Створення текста таймера1.
        self.krok_2_1 = Label (text = "15", font_size = "20sp", color = ("00FFFF"))
        self.timer_label_1 = Label (text = f"Залишилось часу: {self.krok_2_1.text} секунд.", font_size = "20sp", color = ("00FFFF"))
#Створення кнопок/текстінпутів.
        self.button_2_1 = Button (text = "Продовжити", size_hint = (0.4, 0), color = (0, 0, 0, 1), background_color = ("1B8191"), background_normal = "")
        self.button_2_1.bind (on_press = self.go_to_scrin3)
#-!        self.button_2_1.disabled = True
        self.button_2_2 = Button (text = "<-", size_hint = (None, None), size = (100, 50), color = (0, 0, 0, 1), background_color = ("1B8191"), background_normal = "")
        self.button_2_2.bind (on_release = self.go_to_scrin1_1)
        self.button_2_3 = Button (text = "Почати", size_hint = (0.4, 0), color = (0, 0, 0, 1), background_color = ("00FFFF"))
        self.button_2_3.bind (on_release = self.start_progress_1)
        self.ryadok_3 = TextInput (hint_text = "Введіть перший результат", size_hint = (1, 0.2), pos_hint = {"center_x": 0.2, "center_y": 0.5}, multiline = False, background_color = ("1E90A2"), foreground_color = (0, 0, 0, 1), hint_text_color = (0, 0, 0, 1))
        self.ryadok_3.bind (text = self.on_text_change_2)
#-!        self.ryadok_3.disabled = True
#Створення глобального рядка.
        global ryadok_3_ryadok
        ryadok_3_ryadok = self.ryadok_3
#Створення прогресбар.
        self.progresbar_1 = ProgressBar (max = 15, height = 50)
#Додавання до ліній інтерфейсу.
        horithontal_2_2.add_widget (self.button_2_2)
        vertical_2_1m.add_widget (krok_1)
        vertical_2_2m.add_widget (krok_1_1)
        vertical_2_2m.add_widget (self.ryadok_3)
        horithontal_2_4.add_widget (self.timer_label_1)
        horithontal_2_3.add_widget (self.progresbar_1)
        horithontal_2_1.add_widget (self.button_2_3)
        horithontal_2_1.add_widget (self.button_2_1)
#Додавання до віджету ліній.
        widget_2.add_widget (horithontal_2_2)
        widget_2.add_widget (vertical_2_1m)
        widget_2.add_widget (vertical_2_2m)
        widget_2.add_widget (horithontal_2_4)
        widget_2.add_widget (horithontal_2_3)
        widget_2.add_widget (horithontal_2_1)
#Додавання до селфу віджету.
        self.add_widget (widget_2)
#Деф перевірка заповнення рядків.
    def on_text_change_2 (self, instance, value):
        if self.ryadok_3.text: #Якщо обидва текстові поля не порожні
            self.button_2_1.disabled = False #Розблокування кнопки
        else:
            self.button_2_1.disabled = True #Блокування кнопки#Деф переходу до скрінюзерс.
#Деф старту прогресбара1.
    def start_progress_1 (self, instance):
        self.button_2_3.disabled = True
        if self.button_2_1.disabled != True:
            self.button_2_1.disabled = True
            self.ryadok_3.text = ""
            self.ryadok_3.disabled = True
        else:
            None
#Становлення текст мітки таймера на 15.
        self.krok_2_1.text = ("15")
#Створення залишку часу.
        self.time_left_1 = 15
#Створення значення прогрес бару.
        self.progresbar_1.value = 0
#Запуск апдейтпрогрес кожну секунду/оновлювлення прогресбар та таймер.
        Clock.schedule_interval (self.update_progress_1, 1)
#Деф оновлення з часом прогрес бару.
    def update_progress_1 (self, dt):
#Іф перевірки чи прогресбар не більший 15.
        if self.progresbar_1.value < 15:
#Збільшуєм прогресбар.
            self.progresbar_1.value += 1
#Зменшуєм час.
            self.time_left_1 -= 1
#Оновлюємо текст.
            self.krok_2_1.text = str (self.time_left_1)
            self.timer_label_1.text = f"Залишилось часу: {self.time_left_1} секунд."
        else:
#Зупинка апдейтпрогрес.
            self.ryadok_3.focus = True
            self.ryadok_3.disabled = False
            self.button_2_3.disabled = False
            Clock.unschedule (self.update_progress_1)
#-?            self.button_3_1.disabled = False
            self.reset_screen_1()
#Деф оновлення таймеру.
    def reset_screen_1 (self):
        self.progresbar_1.value = 0
        self.time_left_1 = 15
        self.krok_2_1.text = "15"
        self.timer_label_1.text = f"Залишилось часу: {self.time_left_1} Секунд."
#Деф переходу до скрін3.
    def go_to_scrin3(self, instance):
        global ryadok_3_text_1
        global ryadok_3_text_2
        ryadok_3_text_1 = self.ryadok_3.text
        ryadok_3_text_2 = self.ryadok_3
        
        if ryadok_3_text_2.text.isdigit():  # Перевірка, чи введено букви
                self.button_2_1.disabled = False  # Розблокування кнопки
                self.manager.transition = SlideTransition(direction="left")
                self.manager.current = "Введеня третього етапу"
        else:
                self.button_2_1.disabled = True  # Блокування кнопки
                self.show_popup ("Введіть цифри в поле")
#Деф переходу до скрін1.
    def go_to_scrin1_1 (self, instance):
        self.manager.transition = SlideTransition (direction = "right")
        self.manager.current = ("Введеня першого етапу")
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
#Клас скрін3.
class Scrin_3 (Screen):
#Деф конструктор.
    def __init__ (self, **kwargs):
        super (Scrin_3, self).__init__ (**kwargs)
#Встановлюємо розмір вікна.
        Window.size = (950, 700)
#Відкриття контекстного менеджера для відображення позаду зображення.
        with self.canvas.before:
#Створення прямокутника.
            self.bg = Rectangle (source = "OIG3.jpg", size = (1900, 1400), pos = self.pos)
#Створення направних ліній.
        widget_3 = BoxLayout (orientation = "vertical")
        vertical_3m = BoxLayout (orientation = "vertical", padding = 4, spacing = 4)
        horithontal_3_1 = BoxLayout (orientation = "horizontal", padding = 200, spacing = 4)
        horithontal_3_2 = BoxLayout (orientation = "horizontal", padding = 20, spacing = 8)
        horithontal_3_3 = BoxLayout (orientation = "horizontal", spacing = 0)
        horithontal_3_4 =  BoxLayout (orientation = "horizontal", size_hint = (1, None), height = 50)
        horithontal_3_5 =  BoxLayout (orientation = "horizontal", size_hint = (1, None), height = 50)
#Створення тексту таймера2.
        self.krok_2_2 = Label (text = "45", font_size = "20sp", color = ("00FFFF"))
        self.timer_label_2 = Label (text = f"Залишилось часу: {self.krok_2_2.text} Секунд.", font_size = "20sp", color = ("00FFFF"))
#Створення кнопок.
        self.button_3_1 = Button (text = "Продовжити", size_hint = (0.4, 0), color = (0, 0, 0, 1), background_color = ("1B8191"), background_normal = "")
#-!        self.button_3_1.disabled = True
        self.button_3_1.bind (on_press = self.go_to_scrin4)
        self.button_3_2 = Button (text = "Почати", size_hint = (0.4, 0), color = (0, 0, 0, 1), background_color = ("00FFFF"))
        self.button_3_2.bind (on_release = self.start_progress_2)
        self.button_3_3 = Button (text = "<-", size_hint = (None, None), size = (100, 50), color = (0, 0, 0, 1), background_color = ("1B8191"), background_normal = "")
        self.button_3_3.bind (on_press = self.go_to_scrin2)
        self.button_3_4 = Button (text = "|||", size_hint = (None, None), size = (100, 50), color = ("1B8191"), background_color = ("1B8191"))
#Створення анімації.
        self.animation_1 = Animation (x = 1745, duration = 4) + Animation (x = 0, duration = 4)
        self.animation_1.repeat = True
#Створення глобальної кнопки продовжити.
        global button_3_1_2
        button_3_1_2 = self.button_3_1
#Створення прогресбару/рядка загрузеи.
        self.progresbar_2 = ProgressBar (max = 45, height = 50) #Встановлення максимального значення 45с-100%.
#Додавання до ліній інтерфейсу.
        horithontal_3_4.add_widget (self.button_3_3)
        horithontal_3_5.add_widget (self.button_3_4)
        vertical_3m.add_widget (krok_2_1)
        horithontal_3_3.add_widget (self.timer_label_2)
        horithontal_3_1.add_widget (self.progresbar_2)
        horithontal_3_2.add_widget (self.button_3_2)
        horithontal_3_2.add_widget (self.button_3_1)
#Додавання до віджету ліній.
        widget_3.add_widget (horithontal_3_4)
        widget_3.add_widget (horithontal_3_5)
        widget_3.add_widget (vertical_3m)
        widget_3.add_widget (horithontal_3_3)
        widget_3.add_widget (horithontal_3_1)
        widget_3.add_widget (horithontal_3_2)
#Додавання до селфу віджету.
        self.add_widget (widget_3)
#Деф старту прогресбара2.
    def start_progress_2(self, instance):
        self.button_3_2.disabled = True
        if self.button_3_1.disabled != True:
            self.button_3_1.disabled = True
        else:
            None
#Запуск анімації при натисканні кнопки.
        self.animation_1.start (self.button_3_4)
#Зміна кольору та тексту кнопки під час анімації
        self.change_button_properties()
#Становлення текст мітки таймера на 45.
        self.krok_2_2.text = "45"
#Створення залишку часу.
        self.time_left_2 = 45
#Створення значення прогрес бару.
        self.progresbar_2.value = 0
#Запуск апдейтпрогрес кожну секунду/оновлювлення прогресбар та таймер.
        Clock.schedule_interval (self.update_progress_2, 1)
#Деф оновлення з часом прогресбару.
    def update_progress_2 (self, dt):
#Іф перевірки чи прогресбар не більший 45.
        if self.progresbar_2.value < 45:
#Збільшуєм прогресбар.
            self.progresbar_2.value += 1
#Зменшуєм час.
            self.time_left_2 -= 1
#Оновлюємо текст.
            self.krok_2_2.text = str (self.time_left_2)
            self.timer_label_2.text = f"Залишилось часу: {self.time_left_2} Секунд."
        else:
#Зупинка апдейтпрогрес.
            self.animation_1.stop (self.button_3_4)
            self.button_3_1.disabled = False
            self.button_3_2.disabled = False
            self.krok_2_2.text = "45"
            Clock.unschedule (self.update_progress_2)
            self.reset_screen_2 ()
#Деф оновлення таймеру.
    def reset_screen_2 (self):
        self.progresbar_2.value = 0
        self.time_left_2 = 45
        self.krok_2_2.text = "45"
        self.timer_label_2.text = f"Залишилось часу: {self.time_left_2} Секунд."
#Повернення кнопки на початкову позицію та зміна тексту
        self.button_3_4.pos = (0, self.button_3_4.pos[1])
        self.button_3_4.text = "Закінчено"
        self.button_3_4.background_color = get_color_from_hex (("1B8191"))  #Початковий колір кнопки.
        Clock.schedule_once (self.reset_button_text, 4)
#Деф повернення початкового тексту.
    def reset_button_text (self, dt):
        self.button_3_4.size = (100, 50)
        self.button_3_4.text = "|||"
#Деф зміни кольору/тексту.
    def change_button_properties (self):
#Зміна кольору та тексту кнопки під час анімації.
        final_color = "4CAAB9" #Новий колір.
        texts = ["Присідайте"] #Новий текст.
        sizes = [(175, 50)]  #Новий розмір кнопки.
#Фор обовлення кольору/тексту/розміру.
        Clock.schedule_once(lambda dt: self.update_button_properties(final_color, texts[0], sizes[0]), 0)
#Деф оновлення анімації для кнопки.
    def update_button_properties (self, color, text, size):
        self.button_3_4.background_color = get_color_from_hex(color)
        self.button_3_4.text = text
        self.button_3_4.size = size
#Деф переходу до скрін2.
    def go_to_scrin2 (self, instance):
        self.manager.transition = SlideTransition (direction = "right")
        self.manager.current = ("Введеня другого етапу")
#Деф переходу до скрін1.
    def go_to_scrin4 (self, instance):
        self.manager.transition = SlideTransition (direction = "left")
        self.manager.current = ("Введеня четвертого етапу")
#Клас скрін4/введення данних2.
class Scrin_4 (Screen):
#Деф конструктор.
    def __init__ (self, **kwargs):
        super (Scrin_4, self).__init__ (**kwargs)
#Встановлюємо розмір вікна
        Window.size = (950, 700)
#Відкриття контекстного менеджера для відображення позаду зображення.
        with self.canvas.before:
#Створення прямокутника.
            self.bg = Rectangle (source = "OIG3.jpg", size = (1900, 1400), pos = self.pos)
#Створення направних ліній.
        widget_4 = BoxLayout (orientation = "vertical")
        vertical_4m = BoxLayout (orientation = "vertical", padding = 4, spacing = 4)
        vertical_1_4m = BoxLayout (orientation = "horizontal", padding = 100, spacing = 4)
        vertical_2_4m = BoxLayout (orientation = "horizontal", padding = 100, spacing = 4)
        vertical_3_4m = BoxLayout (orientation = "vertical", padding = 40, spacing = 4)
        horithontal_4_5 =  BoxLayout (orientation = "horizontal", size_hint = (1, None), height = 50)
#Створення кнопок/текстінпутів.
        self.button_4_1 = Button (text = "Завершити", size_hint = (0.4, 0), pos_hint = {"center_x": 0.5, "center_y": 0.5}, color = (0, 0, 0, 1), background_color = ("1B8191"), background_normal = "")
        self.button_4_1.disabled = True
        self.button_4_1.bind (on_press = self.go_to_scrin5)
        self.button_4_2 = Button (text = "<-", size_hint = (None, None), size = (100, 50), color = (0, 0, 0, 1), background_color = ("1B8191"), background_normal = "")
        self.button_4_2.bind (on_press = self.go_to_scrin3)
        self.ryadok_4_1 = TextInput (hint_text = "P.S.Серце лише важить приблизно 310 грам", size_hint = (1, 0.4), pos_hint = {"center_x": 0.5, "center_y": 0.5}, background_color = ("1E90A2"), foreground_color = (0, 0, 0, 1), hint_text_color = (0, 0, 0, 1))
        self.ryadok_4_1.bind (text = self.on_text_change_3)
        self.ryadok_4_2 = TextInput (hint_text = "P.S.Серце прокачує 20000 галонів крові на 60000 миль", size_hint = (1, 0.4), pos_hint = {"center_x": 0.5, "center_y": 0.5}, background_color = ("1E90A2"), foreground_color = (0, 0, 0, 1), hint_text_color = (0, 0, 0, 1))
        self.ryadok_4_2.bind (text = self.on_text_change_3)
#Додавання до ліній інтерфейсу.
        horithontal_4_5.add_widget (self.button_4_2)
        vertical_4m.add_widget (krok_3_1)
        vertical_1_4m.add_widget (krok_3_2)
        vertical_1_4m.add_widget (self.ryadok_4_1)
        vertical_2_4m.add_widget (krok_3_3)
        vertical_2_4m.add_widget (self.ryadok_4_2)
        vertical_3_4m.add_widget (self.button_4_1)
#Додавання до віджету ліній.
        widget_4.add_widget (horithontal_4_5)
        widget_4.add_widget (vertical_4m)
        widget_4.add_widget (vertical_1_4m)
        widget_4.add_widget (vertical_2_4m)
        widget_4.add_widget (vertical_3_4m)
#Додавання до селфу віджету.
        self.add_widget (widget_4)
#Перевірка заповнених рядків.
    def on_text_change_3 (self, instance, value):
        if self.ryadok_4_1.text and self.ryadok_4_2.text:
            self.button_4_1.disabled = False
        else:
            self.button_4_1.disabled = True
#Деф переходу до скрін5.
    def go_to_scrin5(self, instance):
        global ryadok_4_1_text_1
        global ryadok_4_2_text_1
        global ryadok_4_1_text_2
        global ryadok_4_2_text_2
        ryadok_4_1_text_1 = self.ryadok_4_1.text
        ryadok_4_2_text_1 = self.ryadok_4_2.text
        ryadok_4_1_text_2 = self.ryadok_4_1
        ryadok_4_2_text_2 = self.ryadok_4_2
        
        if ryadok_4_1_text_2.text.isdigit() and ryadok_4_2_text_2.text.isdigit():  # Перевірка, чи введено цифри
            self.button_4_1.disabled = False  # Розблокування кнопки
            self.manager.transition = SlideTransition(direction="left")
            self.manager.current = "Виведення даних етапів"
        else:
            self.button_4_1.disabled = True  # Блокування кнопки
            self.show_popup("Введіть цифри в поле")
            return  # Додано return, щоб зупинити виконання функції, якщо умова не виконана
#Деф переходу до скрін3.
    def go_to_scrin3 (self, instance):
        self.manager.transition = SlideTransition (direction = "right")
        self.manager.current = ("Введеня третього етапу")
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
#Клас скрін5/виведення результату.
class Scrin_5 (Screen):
#Деф конструктор.
    def __init__ (self, **kwargs):
        super (Scrin_5, self).__init__ (**kwargs)
#Встановлюємо розмір вікна.
        Window.size = (950, 700)
#Відкриття контекстного менеджера для відображення позаду зображення.
        with self.canvas.before:
#Створення прямокутника.
            self.bg = Rectangle (source = "OIG3.jpg", size = (1900, 1400), pos = self.pos)
#Створення направних ліній.
        widget_5 = BoxLayout (orientation = "vertical")
        vertical_5_1 = BoxLayout (orientation = "vertical", padding = 4, spacing = 4)
        vertical_5_2 = BoxLayout (orientation = "vertical", size_hint = (1, None), height = 50)
        vertical_5_3 = BoxLayout (orientation = "vertical", size_hint = (1, 1), height = 50)
        vertical_5_4 = BoxLayout (orientation = "vertical", size_hint = (None, 1), height = 50)
        horithontal_5_1 = BoxLayout (orientation = "horizontal", size_hint = (1, None), height = 50)
        horithontal_5_2 = BoxLayout (orientation = "horizontal", padding = 20, spacing = 8)
#Створення тексту індексаРуфє.
        global index_rufye
        index_rufye = Label (text = "", font_size = "20sp", color = ("1E90A2"))
#Створення кнопок.
        self.button_5_1 = Button (text = "<-", size_hint = (None, None), size = (100, 50), color = (0, 0, 0, 1), background_color = ("1B8191"), background_normal = "")
        self.button_5_1.bind (on_press = self.go_to_scrin4)
        self.button_5_2 = Button (text = "Показати результат", size_hint = (0.2, 0), color = (0, 0, 0, 1), background_color = ("1B8191"), background_normal = "")
        self.button_5_2.bind (on_release = self.show_result)
        self.button_5_3 = Button (text = "Додати", size_hint = (0.2, 0), color = (0, 0, 0, 1), background_color = ("1B8191"), background_normal = "")
        self.button_5_3.bind (on_press = self.add_user_1)
        self.button_5_4 = Button (text = "Очистити", size_hint = (None, None), size = (250, 50), color = (0, 0, 0, 1), background_color = ("1B8191"), background_normal = "")
        self.button_5_4.bind (on_press = self.clear_wedenya_2)
        self.button_5_4.disabled = True
        self.button_5_5 = Button (text = "->", size_hint = (None, None), size = (100, 50), color = (0, 0, 0, 1), background_color = ("1B8191"), background_normal = "")
        self.button_5_5.bind (on_press = self.go_to_scrin1_3)
#Створення глобальної кнопки додати.
        global button_5_3_2
        global button_5_3_3
        button_5_3_2 = self.button_5_3
        button_5_3_3 = self.button_5_4
#Додавання до ліній інтерфейсу.
        vertical_5_2.add_widget (self.button_5_1)
        vertical_5_3.add_widget (self.button_5_4)
        vertical_5_4.add_widget (self.button_5_5)
        horithontal_5_1.add_widget (vertical_5_2)
        horithontal_5_1.add_widget (vertical_5_3)
        horithontal_5_1.add_widget (vertical_5_4)
        vertical_5_1.add_widget (index_rufye)
        horithontal_5_2.add_widget (self.button_5_2)
        horithontal_5_2.add_widget (self.button_5_3)
#Додавання до віджету ліній.
        widget_5.add_widget (horithontal_5_1)
        widget_5.add_widget (vertical_5_1)
        widget_5.add_widget (horithontal_5_2)
#Додавання до селфу віджету.
        self.add_widget (widget_5)
#Деф передачі данних до самсРуфє (Самс).
    def show_result (self, instance):
        self.button_5_2.disabled = True
        self.button_5_4.disabled = False
#Передача результатів до Деф в самсРуфє.
        index_rufye.text = sums_rufye (ryadok_1_text_1, ryadok_2_text_1, ryadok_3_text_1, ryadok_4_1_text_1, ryadok_4_2_text_1)
#Деф очишення всіх рядків.
    def clear_wedenya_2 (self, instance):
#-!        self.button_5_4.disabled = True
#-!        button_3_1_2.disabled = True
#-!        ryadok_3_ryadok.disabled = True
#-!        ryadok_1_btn.disabled = False
        ryadok_1.text = ""
        ryadok_2.text = ""
        ryadok_3_text_2.text = ""
        ryadok_4_1_text_2.text = ""
        ryadok_4_2_text_2.text = ""
        Stanserca.clear()
#Деф переходу до скрін1.
    def go_to_scrin1_3 (self, instance):
        self.manager.transition = SlideTransition (direction = "left")
        self.manager.current = ("Введеня першого етапу")
        self.button_5_4.disabled = False
        button_5_3_2.disabled = False
        self.button_5_2.disabled = False
#Деф переходу до скрін4.
    def go_to_scrin4 (self, instance):
        self.manager.transition = SlideTransition (direction = "right")
        self.manager.current = ("Введеня четвертого етапу")
#Деф додавання користувачів1.
    def add_user_1 (self, instance):
        self.button_5_3.disabled = True
#/Обробка вийнятків при завантажені даних до файлу.
        try:
            user_name = ryadok_1.text  #Створення імені.
            user_age = ryadok_2.text  #Створення віку.
            stanserca = f". Ваш результат - {Stanserca [0]} Ваш вік - "
            list_1 [user_name] = [stanserca, user_age]
            ryadok_1.text = ""
            ryadok_2.text = ""
            print (Fore.CYAN)
            print ("Saved: {0}".format (list_1))
            print (Fore.WHITE)
        except Exception as e:
            print (Fore.LIGHTRED_EX)
            print ("Error1: {0}".format (e))
            print (Fore.WHITE)
            return
        try:
            with open ("users.txt", "a") as fyle_1:
                fyle_1.write (f"{user_name}: {stanserca}, {user_age}\n")
                print (Fore.CYAN)
                print ("Data saved to file: {0}: {1}, {2}".format (user_name, stanserca, user_age))
                print (Fore.WHITE)
        except Exception as e:
            print (Fore.LIGHTRED_EX)
            print ("Error2: {0}".format (e))
            print (Fore.WHITE)
        try:
            self.manager.get_screen ("Збережені користувачі").add_user_2 (user_name, stanserca, user_age)
        except Exception as e:
            print (Fore.LIGHTRED_EX)
            print ("Error3: {0}".format (e))
            print (Fore.WHITE)
#Клас скрінюзерс.
class Scrin_users (Screen):
#Деф конструктор.
    def __init__ (self, **kwargs):
        super (Scrin_users, self).__init__ (**kwargs)
#Встановлюємо розмір вікна.
        Window.size = (950, 700)
#Відкриття контекстного менеджера для відображення позаду зображення.
        with self.canvas.before:
#Створення прямокутника.
            self.bg = Rectangle (source = "OIG3.jpg", size = (1900, 1400), pos = self.pos)
#Створення направних ліній.
        self.horithontal_2_5_1 = BoxLayout (orientation = "horizontal", size_hint = (1, None), height = 55, spacing = 1580)
        self.horithontal_2_5_2 = BoxLayout (orientation = "horizontal", spacing = 4, size_hint_y = 10)
        self.vertical_2_5_1 = BoxLayout (orientation = "vertical", spacing = 4, size_hint_y = 10)
#Створення кнопок.
        self.button_2_5_1 = Button (text = "<-", size_hint = (None, None), size = (100, 50), color = (0, 0, 0, 1), background_color = ("1B8191"), background_normal = "")
        self.button_2_5_1.bind (on_press = self.go_to_scrin1_2)
        self.button_2_5_2 = Button (text = "Видалити", size_hint = (None, None), size = (200, 50), color = (0, 0, 0, 1), background_color = ("1B8191"), background_normal = "")
        self.button_2_5_2.bind (on_press = self.remove_checkbox)
        self.button_2_5_3 = Button (text ="Інформація", size_hint = (None, None), size = (200, 50), color = (0, 0, 0, 1), background_color = ("1B8191"), background_normal = "")
#Додавання до ліній інтерфейсу.
        self.horithontal_2_5_1.add_widget (self.button_2_5_1)
        self.horithontal_2_5_1.add_widget (self.button_2_5_2)
        self.horithontal_2_5_2.bind (minimum_height = self.horithontal_2_5_2.setter ("height"))
#Додавання до віджету ліній.
        widget_u.add_widget (self.horithontal_2_5_1)
        widget_u.add_widget (self.vertical_2_5_1)
#Додавання до селфу віджету.
        self.add_widget (widget_u)
#Виклик методу для зчитування даних з файлу.
        self.load_users_from_file()
#Деф переходу до скрін1.
    def go_to_scrin1_2 (self, instance):
        self.manager.transition = SlideTransition (direction = "up")
        self.manager.current = "Введеня першого етапу"
#Деф додавання данних користувача до скрінюзерс.
    def add_user_2 (self, user_name, stanserca, user_age ):
#Створення тексту юзера.
        self.label_user = Label (text = f"{user_name} {stanserca} {user_age}", color = (0.12, 0.56, 0.64, 1))
#Створення кнопкичекер.
        self.button_insert = CheckBox (group = "options")
        self.button_insert.bind (on_press = lambda x: self.insert_user (user_name, stanserca, user_age))
#Створення напрямних ліній для нового користувача.
        horithontal_2_5_3 = BoxLayout (orientation = "horizontal", spacing = 4)
#Додавання до ліній інтерфейсу.
        horithontal_2_5_3.add_widget (self.button_insert)
        horithontal_2_5_3.add_widget (self.label_user)
        self.vertical_2_5_1.add_widget (horithontal_2_5_3)
#Створення данних для видалення.
        self.checkbox_to_remove = self.button_insert
        self.label_to_remove = self.label_user
        self.user_name_to_remove = user_name
#Деф вставлення даних в рядки.
    def insert_user (self, user_name, stanserca, user_age):
        print (Fore.CYAN)
        print ("User {0} {1} {2}".format (user_name, stanserca, user_age))
        print (Fore.WHITE)
        ryadok_1.text = user_name
        ryadok_2.text = user_age
#Деф завантаження даних з файлу.
    def load_users_from_file (self):
        try:
#Відкриття файлу юзерс.
            with open ("users.txt", "r") as fyle_1:
#Фор кожного рядка.
                for line in fyle_1:
#Обробка кожного рядка від пробілів.
                    user_data = line.strip().split (": ")
#Іф чи розділення дало дві частини.
                    if len (user_data) == 2:
#Розділення на імя та вік/стансерця.
                        user_name = user_data [0]
                        user_info = user_data [1].split (", ")
#Іф чи розділення дало дві частини (вік та результат).
                        if len (user_info) == 2:
#Завантаження віку/результату.
                            stanserca = user_info [0]
                            user_age = user_info [1]
#Завантаження користувача до інтерфейсу.
                            self.add_user_2 (user_name, stanserca, user_age)
        except Exception as e:
            print (Fore.CYAN)
            print ("Error loading users from file: {0}".format (e))
            print (Fore.LIGHTRED_EX)
#Деф видалення даних.
    def remove_checkbox(self, instance):
#Видалення CheckBox та Label з макету
        parent_layout = self.checkbox_to_remove.parent
        self.vertical_2_5_1.remove_widget(parent_layout)
#Видалення данних з рядків.
        ryadok_1.text = ""
        ryadok_2.text = ""
#Видалення даних з файлу.
        self.remove_data_from_file(self.user_name_to_remove)
#Деф видалення данних з файлу.
    def remove_data_from_file(self, user_name_to_remove, filename="users.txt"):
        try:
#Читання всіх даних з файлу.
            with open(filename, "r") as file:
                lines = file.readlines()
#Видалення рядків, які містять значення user_name_to_remove.
                with open(filename, "w") as file:
#Фор кожного рядка.
                    for line in lines:
                        if user_name_to_remove not in line:
                            file.write(line)
                print (Fore.CYAN)
                print(f"Data with value '{0}' has been removed from {1}.".format (user_name_to_remove, filename))
                print (Fore.WHITE)
        except Exception as e:
            print (Fore.LIGHTRED_EX)
            print (f"Error: {0}".format (e))
            print (Fore.WHITE)
class MyApp (App):
#Деф конструктор Майап.
    def __init__ (self, **kwargs):
        super (MyApp, self).__init__ (**kwargs)
# Встановлюємо імя вікна.
        self.title = ("Your Health")
#Деф СкрінМенеджер.
    def build (self):
        scrinmanager = ScreenManager() #Створення скрінменеджера.
        scrinmanager.add_widget (Scrin_1 (name = "Введеня першого етапу")) #Додавання до скрінменеджера вікна.
        scrinmanager.add_widget (Scrin_2 (name = "Введеня другого етапу"))
        scrinmanager.add_widget (Scrin_3 (name = "Введеня третього етапу"))
        scrinmanager.add_widget (Scrin_4 (name = "Введеня четвертого етапу"))
        scrinmanager.add_widget (Scrin_5 (name = "Виведення даних етапів"))
        scrinmanager.add_widget (Scrin_users (name = "Збережені користувачі"))
#Встановлення Scrin_1 як стартового екрану.
        scrinmanager.current = ("Введеня першого етапу")
#Запуск екраногоменеджера.
        return scrinmanager
#Запуск програми.
if __name__ == "__main__":
    MyApp().run()
#.

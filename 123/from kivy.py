from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.clock import *
from kivy.properties import BooleanProperty

txt_instruction = """
Ця програма дозволить вам за допомогою тесту Руф'є\n
провести первинну діагностику вашого здоров'я.\n
Проба Руф'є являє собою навантажувальний комплекс, призначений\n
для оцінки працездатності серця при фізичному навантаженні.\n
У випробуваного визначають частоту пульсу за 15 секунд.\n
Потім протягом 45 секунд випробуваний виконує 30 присідань.\n
Після закінчення навантаження пульс підраховується знову: число\n
пульсацій за перші 15 секунд, 30 секунд відпочинку, число\n
пульсацій за останні 15 секунд.\n"""

txt_test1 = """ Заміряйте пульс за 15 секунд.\n
Результат запишіть у відповідне поле. """

txt_test2 = """ Виконайте 30 присідань за 45 секунд.\n
Натисніть кнопку "Почати", щоб запустити лічильник присідань.\n
Робіть присідання зі швидкістю лічильника. """

txt_test3 = """ Протягом хвилини заміряйте пульс двічі:\n
за перші 15 секунд хвилини, потім за останні 15 секунд.\n
Результати запишіть у відповідні поля. """

txt_sits = "Виконайте 30 присідань за 45 секунд."

age = 0
name = ""

class Seconds(Label):
    done = BooleanProperty(False)

    def __init__(self, total, **kwargs):
        self.done = False
        self.current = 0
        self.total = total
        my_text = "Прошло секунд: " + str(self.current)
        super().__init__(text="Прошло секунд: " + str(self.current))

    def start(self):
        Clock.schedule_interval(self.change, 1)

    def change(self, dt):
        self.current += 1
        self.text = "Прошло секунд: " + str(self.current)
        if self.current >= self.total:
            self.done = True
            return False

    def restart(self, total, **kwargs):
        self.done = False
        self.total = total
        self.current = 0
        self.text = "Прошло секунд: " + str(self.current)
        self.start()

class First(Screen):
    def __init__(self, name):
        super().__init__(name=name)
        label = Label(text=txt_instruction)
        lbl_name = Label(text="Введіть ім'я")
        lbl_age = Label(text='Введіть вік')
        self.in_name = TextInput(text="ім'я")
        self.in_age = TextInput(text='0')
        self.btn = Button(text='Далі')
        self.btn.on_press = self.next
        h1 = BoxLayout()
        h2 = BoxLayout()
        v_line = BoxLayout(orientation='vertical')
        h1.add_widget(lbl_name)
        h1.add_widget(self.in_name)
        h2.add_widget(lbl_age)
        h2.add_widget(self.in_age)
        v_line.add_widget(label)
        v_line.add_widget(h1)
        v_line.add_widget(h2)
        v_line.add_widget(self.btn)
        self.add_widget(v_line)

    def next(self):
        global name, age
        name = self.in_name.text
        age = int(self.in_age.text)
        self.manager.current = "second"

class Second(Screen):
    def __init__(self, name):
        super().__init__(name=name)
        label = Label(text=txt_test1)
        lbl_p1 = Label(text='Результат')
        self.in_p1 = TextInput(text = "0")
        self.btn = Button(text='Далі')
        self.btn.on_press = self.next
        h1 = BoxLayout()
        v_line = BoxLayout(orientation='vertical')
        h1.add_widget(lbl_p1)
        h1.add_widget(self.in_p1)
        v_line.add_widget(label)
        v_line.add_widget(h1)
        v_line.add_widget(self.btn)
        self.add_widget(v_line)

    def next(self):
        self.manager.current = "third"

class Third(Screen):
    def __init__(self, name):
        super().__init__(name=name)
        label = Label(text=txt_test2)
        self.btn = Button(text='')
        self.btn.on_press = self.next
        v_line = BoxLayout(orientation='vertical')
        v_line.add_widget(label)
        v_line.add_widget(self.btn)
        self.add_widget(v_line)

    def next(self):
        self.manager.current = "fourth"

class Fourth(Screen):
    def __init__(self, name):
        super().__init__(name=name)
        label = Label(text=txt_test3)
        lbl_p2 = Label(text='')
        lbl_p3 = Label(text='')
        self.in_p2 = TextInput(text='0')
        self.in_p3 = TextInput(text='0')
        self.btn = Button(text='')
        self.btn.on_press = self.next
        h1 = BoxLayout()
        h2 = BoxLayout()
        v_line = BoxLayout(orientation='vertical')
        h1.add_widget(lbl_p2)
        h1.add_widget(self.in_p2)
        h2.add_widget(lbl_p3)
        h2.add_widget(self.in_p3)
        v_line.add_widget(label)
        v_line.add_widget(h1)
        v_line.add_widget(h2)
        v_line.add_widget(self.btn)
        self.add_widget(v_line)

    def next(self):
        self.manager.current = "fifth"

class Fifth(Screen):
    def __init__(self, name):
        super().__init__(name=name)
        label = Label()
        v_line = BoxLayout(orientation='vertical')
        v_line.add_widget(label)
        self.add_widget(v_line)


class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(First(name='first'))
        sm.add_widget(Second(name='second'))
        sm.add_widget(Third(name='third'))
        sm.add_widget(Fourth(name='fourth'))
        sm.add_widget(Fifth(name='fifth'))
        return sm

app = MyApp()
app.run()
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button


class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)

        self.label = Label(text="سلام 👋 خوش اومدی!", font_size=32)

        btn = Button(text="کلیک کن", font_size=28)
        btn.bind(on_press=self.clicked)

        layout.add_widget(self.label)
        layout.add_widget(btn)

        return layout

    def clicked(self, instance):
        self.label.text = "🔥 دکمه زده شد!"


if __name__ == "__main__":
    MyApp().run()

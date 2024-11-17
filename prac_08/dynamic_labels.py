from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelsApp(App):
    def build(self):
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        names = ['Alice', 'Bob', 'Charlie', 'David', 'Eve']

        # Access the BoxLayout in the kv file by its id
        main_layout = self.root.ids.main

        # Loop through the list of names and create a Label for each
        for name in names:
            temp_label = Label(text=name, font_size=32, color=(1, 1, 0, 1))

            main_layout.add_widget(temp_label)

        return self.root


DynamicLabelsApp().run()

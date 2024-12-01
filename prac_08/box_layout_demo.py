from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    def build(self):
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')  # Load the .kv file
        return self.root

    def handle_greet(self):
        # Get the text from the TextInput and greet the user
        user_name = self.root.ids.input_name.text
        if user_name.strip():  # Only greet if there's a name entered
            self.root.ids.output_label.text = f"Hello {user_name}"
        else:
            self.root.ids.output_label.text = "Hello, stranger!"

    def handle_clear(self):
        # Clear the TextInput and reset the Label
        self.root.ids.input_name.text = ''
        self.root.ids.output_label.text = 'Enter your name'


if __name__ == '__main__':
    BoxLayoutDemo().run()

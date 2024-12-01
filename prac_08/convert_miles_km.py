"""
CP1404 Week 11 Workshop - GUI program to convert miles to kilometres
Zhang Hanzhi
12/11/2024
"""

from kivy.app import App
from kivy.lang import Builder

# Constant for conversion factor from miles to kilometers
MILES_TO_KM = 1.60934


class MilesConverterApp(App):
    """ Kivy App for converting miles to kilometers """

    def build(self):
        """ Build the Kivy app from the kv file """
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')  # Load kv file
        return self.root

    def handle_calculate(self):
        """ Handle calculation of miles to km """
        value = self.get_validated_miles()  # Get validated miles input
        result = value * MILES_TO_KM  # Calculate kilometers
        self.root.ids.output_label.text = str(result)  # Update the label with result

    def handle_increment(self, change):
        """
        Handle up/down button press, update the miles value in the input field and recalculate
        :param change: the amount to change (1 for up, -1 for down)
        """
        value = self.get_validated_miles() + change  # Increment or decrement the miles value
        self.root.ids.input_miles.text = str(value)  # Update the input field
        # self.handle_calculate()  # Recalculate the km value

    def get_validated_miles(self):
        """
        Get and validate the input miles value
        :return: float value of miles if valid, otherwise return 0
        """
        try:
            value = float(self.root.ids.input_miles.text)  # Convert input text to float
            return value
        except ValueError:
            return 0  # If the input is invalid, return 0


# Run the app
MilesConverterApp().run()

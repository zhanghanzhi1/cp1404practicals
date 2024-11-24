from taxi import Taxi


class SilverServiceTaxi(Taxi):
    """A premium taxi service that charges an extra flagfall fee."""
    flagfall = 4.50  # class variable for the fixed charge on each fare

    def __init__(self, name, fuel, fanciness):
        """Initialize a SilverServiceTaxi instance, adjust price per km by fanciness."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km = Taxi.price_per_km * fanciness  # Scale the base price per km by fanciness

    def get_fare(self):
        """Calculate the total fare including the flagfall."""
        return round(super().get_fare() + self.flagfall, 2)

    def __str__(self):
        """Return a string representation including the flagfall."""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"

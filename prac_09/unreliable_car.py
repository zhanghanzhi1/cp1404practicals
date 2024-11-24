import random
from prac_09.car import Car


class UnreliableCar(Car):
    """A Car that might not always drive when asked due to reliability issues."""

    def __init__(self, name, fuel, reliability):
        """Initialise an UnreliableCar instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.reliability = reliability  # reliability is a float between 0 and 100

    def drive(self, distance):
        """Attempt to drive the car a given distance based on its reliability."""
        if random.random() * 100 < self.reliability:
            # If the random number is less than reliability, the car drives
            distance_driven = super().drive(distance)
        else:
            # Otherwise, the car does not drive
            distance_driven = 0
        return distance_driven

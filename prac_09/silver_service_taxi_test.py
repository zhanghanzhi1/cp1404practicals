from silver_service_taxi import SilverServiceTaxi

# Create a SilverServiceTaxi with a high level of fanciness
luxury_taxi = SilverServiceTaxi("Hummer", 200, 4)

# Test-driving the taxi
luxury_taxi.drive(18)  # Drive 18 km

# Print details and fare
print(luxury_taxi)
print("Total fare for 18 km:", luxury_taxi.get_fare())

# Use assert to verify correctness of fare calculation
assert luxury_taxi.get_fare() == 93.06, "The fare calculation is incorrect."

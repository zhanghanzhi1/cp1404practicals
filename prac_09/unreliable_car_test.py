from unreliable_car import UnreliableCar

# Create an unreliable car with moderate reliability
test_car = UnreliableCar("Sketchy", 100, 50)  # 50% reliability

# Attempt to drive it 10 times, up to 20 km each time
for i in range(10):
    distance_to_drive = 20
    driven = test_car.drive(distance_to_drive)
    print(f"Attempt {i+1}: Tried to drive {distance_to_drive}km, drove {driven}km")

print(test_car)

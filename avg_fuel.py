n = int(input("Enter number of trips: "))

distance_travelled = 0
fuel_consumed = 0
trip = 0

for trip in range (1,n):
    distance=float(input("Enter the distance travelled: "))
    fuel=float(input("Enter the fuel consumed: "))
    trip+=1
    distance_travelled+=distance
    fuel_consumed+=fuel
avg_fuel_used=distance_travelled/fuel_consumed
print(avg_fuel_used)
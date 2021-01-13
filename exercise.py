print("learning Python3 the hard way")
print("hens", 10-5*4)
print("more complex", 10%1/10*5-6+4)
print("5 is > 4", 5 > 4)
print("3 is < 2", 3 < 2)


cars = 10
space_in_a_car = 4.0
cars_not_driven = 8
passengers = 12
cars_empty = cars_not_driven
cars_driven = cars - cars_not_driven
car_capacity = cars_driven * space_in_a_car
average_passenger_per_car = passengers / cars_driven
print(car_capacity, "car_capacity")
print(average_passenger_per_car, "average_passenger_per_car")

print(f" {cars_driven} cars has {passengers} passengers, with an average of {round(average_passenger_per_car)} in each car")


man = "patriarchy{}"
woman = "feminism is the new order"

print(man.format(woman))

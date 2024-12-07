import utilities
import random

list_of_numbers = [random.randint(1, 25) for _ in range(15)]

print(utilities.find_max(list_of_numbers))
print(utilities.calculate_average(list_of_numbers))

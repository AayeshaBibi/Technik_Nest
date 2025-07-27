from my_package.utils import greet, square

print("Tasks - Libraries and pip - Task 2:")
print("--- Using Custom Package ---")

message = greet("Alice")
print(message)

num_to_square = 7
squared_value = square(num_to_square)
print(f"The square of {num_to_square} is: {squared_value}\n")
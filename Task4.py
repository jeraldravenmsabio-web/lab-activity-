print("Task 4: The Movie Ticket Price Decider")

age = int(input("Age: "))
is_student = input("Is student? (True/False): ") == "True"
price = 12
if age <= 12:
    price -= 3
elif age >= 65:
    price -= 4
elif is_student:
    price -= 2
print(f"Your ticket price is ${price}")

print()

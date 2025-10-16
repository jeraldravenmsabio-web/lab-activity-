print("Task 2: The Order of Operations Challenge \n")

pred1 = int(input("Predict the result of: 5 + 3 * 2 ** 2 = "))
pred2 = int(input("Predict the result of: (5 + 3) * 2 ** 2 = "))
pred3 = int(input("Predict the result of: 10 % 3 + 5 * 2 = "))
print()

result1 = 5 + 3 * 2 ** 2
result2 = (5 + 3) * 2 ** 2
result3 = 10 % 3 + 5 * 2

print("Your answer for #1:", pred1, " | Correct answer:", result1)
print("Your answer for #2:", pred2, " | Correct answer:", result2)
print("Your answer for #3:", pred3, " | Correct answer:", result3)
print()

score = 0
if pred1 == result1:
    score += 1
if pred2 == result2:
    score += 1 
if pred3 == result3:
    score += 1

if score == 3:
	print("you got it perfect")
else:
	print("You got", score, "out of 3 correct.")
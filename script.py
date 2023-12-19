import time

# Create lists for last semester gradebook, subjects, and grades
last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]
subjects = ["physics", "calculus", "poetry", "history"]
grades = [98, 97, 85, 88]

# Create 2D gradebook lists combining subjects and grades
gradebook = [
  ["physics", 98], 
  ["calculus", 97], 
  ["poetry", 85], 
  ["history", 88]
]

# Display Gradebook
print("Your current gradebook: ")
print(gradebook)
print(" ")
time.sleep(1)

# Grade for computer science class just came in with a score of 100. Add new entry to gradebook.
print("Updating gradebook with Computer Science score (100)...")
gradebook.append(["computer science", 100])
time.sleep(1)

# Grade for visual arts just came in with a score of 93. Add new entry to gradebook.
print("Updating gradebook with Visual Arts score (93)...")
gradebook.append(["visual arts", 93])
time.sleep(1)

# Display updated Gradebook
print("Your current gradebook: ")
print(gradebook)
print(" ")
time.sleep(1)

# There was a grading mistake for the visual arts class. An extra 5 points was awarded; update visual arts class.
print("Updating gradebook grading mistake for Visual Arts class. Adding +5 points to score...")
gradebook[-1][-1] += 5
time.sleep(1)

# Display updated Gradebook
print("Your current gradebook: ")
print(gradebook)
print(" ")
time.sleep(1)

# The poetry class has switched from numerical grades to Pass/Fail option. Remove numerical grade.
print("Poetry class is switching from numerical grades to Pass/Fail.")
print("Removing numerical grade from gradebook.")
gradebook[2].remove(85)
time.sleep(1)

# Display updated Gradebook
print("Your current gradebook: ")
print(gradebook)
print(" ")
time.sleep(1)

# Update poetry class with a Pass value.
print("Adding 'Pass' grade for Poetry class.")
gradebook[2].append("Pass")
time.sleep(1)

# Display updated Gradebook
print("Your current gradebook: ")
print(gradebook)
print(" ")
time.sleep(1)

# Create a full_gradebook that combines the last_semester_gradebook and gradebook lists.
print("Creating Full Gradebook combining Last Semester and current Gradebook...")
full_gradebook = last_semester_gradebook + gradebook
time.sleep(1)

# Display Full Gradebook
print("Your Full Gradebook: ")
print(full_gradebook)
print(" ")

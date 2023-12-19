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
print(gradebook)
print(" ")

# Grade for computer science class just came in with a score of 100. Add new entry to gradebook.
gradebook.append(["computer science", 100])

# Grade for visual arts just came in with a score of 93. Add new entry to gradebook.
gradebook.append(["visual arts", 93])

# Display updated Gradebook
print(gradebook)
print(" ")

# There was a grading mistake for the visual arts class. An extra 5 points was awarded; update visual arts class.
gradebook[-1][-1] += 5 

# Display updated Gradebook
print(gradebook)
print(" ")

# The poetry class has switched from numerical grades to Pass/Fail option. Remove numerical grade.
gradebook[2].remove(85)

# Display updated Gradebook
print(gradebook)
print(" ")

# Update poetry class with a Pass value.
gradebook[2].append("Pass")

# Display updated Gradebook
print(gradebook)
print(" ")

# Create a full_gradebook that combines the last_semester_gradebook and gradebook lists.
full_gradebook = last_semester_gradebook + gradebook

# Display Full Gradebook
print(full_gradebook)
print(" ")

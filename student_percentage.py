# Calculate total and percentage of a student

name = input("Enter student name: ")

m1 = float(input("Enter marks for Subject 1: "))
m2 = float(input("Enter marks for Subject 2: "))
m3 = float(input("Enter marks for Subject 3: "))
m4 = float(input("Enter marks for Subject 4: "))
m5 = float(input("Enter marks for Subject 5: "))

total = m1 + m2 + m3 + m4 + m5
percentage = total / 5

print("\nStudent Name:", name)
print("Total Marks:", total)
print("Percentage:", percentage, "%")

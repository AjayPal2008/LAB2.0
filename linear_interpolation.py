# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Micah Kadiri
#               Benjamin Hatch
#               Ajay Palanisamy
#               Hudson Dobbs
# Section:      508
# Assignment:   Lab Topic 2 (Team: Part 1)
# Date:         31 August 2026

initial_distance = 2030 
initial_time = 10
final_distance = 23030
final_time = 55
slope = (final_distance - initial_distance) / (final_time - initial_time)
y_intercept = initial_distance - slope * initial_time
time = 25 #float(input("Enter a time in minutes to calculate the distance traveled: "))
print("The distance traveled is", (slope * time + y_intercept)%42376.6, "kms")# for part one put in 25 mins as Input remove input function.

#Part 1 
i_d = 2030 #kilometres
i_t = 10
f_d = 23030 #kilometres
f_t = 55
distance = float(input("Input a number between 10 and 55 -"))
x_2 = 466.6676*distance - 2636.67
print("For t=" ,distance, "minutes, the position p =" ,x_2, "kilometres")

# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:                    Micah Kadiri
#                           Benjamin Hatch
#                           Ajay Palanisamy
#                           Hudson Dobbs
# Section:            508
# Assignment:    Lab Topic 2 (Team: Part 1)
# Date:                4 september 2026


initial_distance = 2030 
initial_time = 10
final_distance = 23030
final_time = 55
slope = (final_distance - initial_distance) / (final_time - initial_time)#calculates the slope of the line
y_intercept = initial_distance - slope * initial_time



print("Part 1:\nFor t = 25 minutes, the position p =", (slope * 25 + y_intercept), "kilometers")
print("Part 2:\nFor t = 300 minutes, the position p =", (slope * 300 + y_intercept)%42380.19, "kilometers")

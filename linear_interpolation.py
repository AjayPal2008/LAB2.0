initial_distance = 2030 
initial_time = 10
final_distance = 23030
final_time = 55
slope = (final_distance - initial_distance) / (final_time - initial_time)
y_intercept = initial_distance - slope * initial_time
time = 25 #float(input("Enter a time in minutes to calculate the distance traveled: "))
print("The distance traveled is", (slope * time + y_intercept)%42376.6, "kms")# for part one put in 25 mins as Input remove input function.


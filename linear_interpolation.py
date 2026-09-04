initial_distance = 2030 
initial_time = 10
final_distance = 23030
final_time = 55
slope = (final_distance - initial_distance) / (final_time - initial_time)
y_intercept = initial_distance - slope * initial_time
time = float(input("Enter a time in minutes to calculate the distance traveled: "))
print("The distance traveled is", (slope * time + y_intercept)%42376.6, "kms")


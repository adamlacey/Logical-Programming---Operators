# Seperate the data into the 3 categories of triathlon: swim, cycle, run

swimming_time = int(input("How long in minutes did it take you to complete the swimming section of the triathlon?: "))

cycle_time = int(input("How long in minutes did it take you to complete the cycling section of the triathlon?: "))

running_time = int(input("How long in minutes did it take you to complete the running section of the triathlon?: "))

# Add all 3 variables together to get total finishing time

total_time = int(swimming_time) + int(cycle_time) + int(running_time)

# Total finishing time

print(f"Your total time for completing the triathlon is: {sum} minutes")

if total_time >= 0 and total_time <= 100:           # 'greater than or equal to 0 and less than or equal to 100'
    print("Congratulations, you're within the qualifying time! Your award is Provincial Colours!")
elif total_time >= 101 and total_time <= 105:       # 'greater than or equal to 101 and less than or equal to 105'
    print("Congratulations, you're 5 minutes within the qualifying time! Your award is Provincial Half Colours!")
elif total_time >= 106 and total_time <= 110:       # 'greater than or equal to 106 and less than or equal to 110'
    print("Congratulations, you're 10 minutes within the qualifying time! Your award is Provincial Scroll!")
elif total_time >= 111:                             # 'greater than or equal to 111'
    print("Congratulations on completing, but unfortunately you are over the qualifying time and do not recieve a prize.")
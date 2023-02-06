import random
#Part A
weeks = 16
classes = 5
tuition = 6000
cost_per_week = ((tuition/classes)/weeks)
print("Cost per week:", cost_per_week)
classes_per_week = 5
cost_per_class = cost_per_week/classes_per_week
print("Cost per class:", cost_per_class)

print(weeks, type(weeks))
print(classes, type(classes))
print(tuition, type(tuition))
print(cost_per_week, type(cost_per_week))
print(classes_per_week, type(classes_per_week))
print(cost_per_class, type(cost_per_class))

#Part B
BasketballPlayers = ["Lebron", "Jordan", "Kareem", "Wilt", "Magic"]
print("The greatest basketball player is:", random.choice(BasketballPlayers))
print(10*5)
print(10**2)
print(15 / 10) #Standard division, always results in a float
print(15 // 10) #Always results in an integer, floor operator
print(-15 // 10)
print(15 % 10)
print(10 % 15)
print(10 % 10)
print(0 % 10)
print(10/15)
# Last one is wrong because 10/15 is 6.667 or 6 repeating but computer cuts it off

##Variables
var1_data = 6
print(var1_data + 6)

print(type(var1_data))

var1_data = "7"
print(type(var1_data))

#Container Types
# -data that only holds other data

#list
mylist = [1,"2",3,4.0,[5,6,7,8,9,10]]

print(mylist[0]) #0 indexed
print(mylist[2])
print(mylist[-1])

mycolors = [
    "red",
    "green",
    "blue"
]

print(mycolors, len(mycolors))

mycolors[1] = "purple"
print(mycolors)

mycolors.append("yellow")
print(mycolors)

del mycolors[3]
print(mycolors)
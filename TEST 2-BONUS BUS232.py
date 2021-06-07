import sys
import math

# Creating a text file to write.
f = open("shares.txt", "w")
    
# This var is to hold the total number of shares.
total = 0

# This list is to hold the stakeholders' shares.
shares = []

# In order to not get a undefined variable error,
# I predefine share as 1.
share = 1

# In this while loop, we'll take the stakeholders'
# number of shares; store them inside an array;
# and calculate the total number of shares.
while(True):
    share = int(input("Please enter the number of shares: "))
    if share == 0:
        break
    toWrite = "Please enter the number of shares: " + str(share)  + "\n"
    f.write(toWrite)
    shares.append(share)
    total = total + share

print("Thank you, there's a total of", total, "shares represented here.")
toWrite = "Thank you, there's a total of " + str(total) + " shares represented here.\n"
f.write(toWrite)

# Find the number of shares to take the majority.
sharesNeeded = math.floor(total / 2) + 1
print("Shares needed for the majority vote is", sharesNeeded, ".")
toWrite = "Shares needed for the majority vote is " + str(sharesNeeded) + ".\n"
f.write(toWrite)

# Sort the shares list.
shares = sorted(shares)[::-1]

# This var is the summation of the shares needed
# for the majority.
sum = 0
# This var will represent the index of the list "shares",
# and also the number of top stakeholders needed to take 
# the majority.
index = 0
# We'll add the shares to the var "sum",
# till their summation is not smaller than 
# "sharesNeeded". 
while(sum < sharesNeeded):
    sum = sum + shares[index]
    index += 1

print("You need the support of top", index, "shareholders for this number of votes.")
toWrite = "You need the support of top " + str(index) + " shareholders for this number of votes." + "\n"
f.write(toWrite)

# Close the txt file.
f.close()
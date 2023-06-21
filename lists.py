# python lists are a way to store collections of items 
# they are are ordered,changeable and allow duplicates
# lists are are created using square brackets[] and commas to seperate items 
#                                0       1        2        3      4
#                                -5      -4       -3       -2     -1
nimi_top_five_sports = ["Basketball","football","swimming","tennis","fencing"]

last = nimi_top_five_sports[-1]
print (last)
# to select a range of values is called slicing
#           [start  :  stop]
top_three = nimi_top_five_sports[0 : 3]
print (top_three)
# using slicing to skip
#[start  :  stop: step/skip]
even_only = nimi_top_five_sports[0:: 2]
print ("even only", even_only )

# reverse a list
reversed = nimi_top_five_sports[::-1]
print ("reversed", reversed)

# adding elements
nimi_top_five_sports.append("swimming")
print("after using append", nimi_top_five_sports)

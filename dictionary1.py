students = {
    "Nimi":"10 years old",
    "Elizabeth":"12 years old",
    "Sammy":"13 years old"
}
(names) = (students.keys)
(ages) = (students.values)

print (names)
print (ages) 
key = "Nimi"

if key in students:
    print ("the key", key,"exists in your dictionary")
else:
    print ("the key", key," does not exists in your dictionary")
    
del students["Sammy"]
print (students)

my_list = []
    
    
    









vegtables = {
    "carrot" :"an orange crunchy vegtable",
    "broccli":"a green vegetable that has an odd taste",
    "cucumber":"a green juicy vegetable"
}
friuts = {
    "kiwi" :"a soft furry brown fruit ",
    "pear":"a green crunchy fruit",
    "watermelon":"a big red juicy fruit"
}

vegtables.update(friuts)

print (vegtables)




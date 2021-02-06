#Yeşim Ece Ersoy Day2Homework


#Question1
mylist = ["Y", 1200, "E", 151, "E", 568]

#(first 3 elements)
list1 = mylist [:3]
#(last 3 elements)
list2 = mylist [3:]

# print list (s)
print ("list : ",mylist)
print ("newlist ",list2+list1)


#Question2
x = int(input("Enter an integer: "))
number=0
while -1<number <= x<10:
   if(number % 2 == 0):
       print(("{0}".format(number)))
   number = number + 1


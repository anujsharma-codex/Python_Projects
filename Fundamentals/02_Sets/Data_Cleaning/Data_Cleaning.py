# ANSWER 

list_a = ["a@gmail.com", "b@gmail.com", "c@gmail.com"]
list_b = ["b@gmail.com", "c@gmail.com", "d@gmail.com"]

#1
set1=set(list_a)
set2=set(list_b)
print("unique elements of first list: ",set1)
print("unique elements of second list: ",set2)

#2
sa=set(list_a)
sb=set(list_b)
s=set1.intersection(set2)
print("emails in both sets: ",s)

#3
unique_a=set1.difference(set2)
unique_b=set2.difference(set1)
print("elements only in first: ",unique_a)
print("elements only in second",unique_b)

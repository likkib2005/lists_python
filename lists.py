numbers=[12,34,56,78-10,-56]
print(numbers)
print(len(numbers))
mixed_list=[1,"likitha",True,10.9]
print(mixed_list)
print(mixed_list[1])
print(mixed_list[4])
list=[10,0,-1,7,8,10,-67]
print(list)
print(len(list))
print(list[1:3])
print(list[1:])
print(list[0:5:2])
print(list[0::3])
list_1=[12,45,67,43,345,54]
list_1.sort()
print(list_1)
list_1.reverse()
print(list_1)
print(min(list_1))
print(max(list_1))
count_of_12=list_1.count(12)
print(f"count of 12:{count_of_12}")  
#append at the end of list we can add
list_1.append(14)
print(list_1) 
#at specific position
list_1.insert(2,76)
print(list_1)
list_1 = [1, 2, 2, 3, 3, 3]
count_of_2=list_1.count(2)
count_of_3 = list_1.count(3)
print(f"Count of 3: {count_of_3}")
print(f"count of 2:{count_of_2}")
print(list_1)
#one or more data
list_1.extend([45,67,65,43,23,21])
print(list_1)
#change elements
list_1[0]=34
print(list_1)
#remove elements
num=[78,65,43,23,23]
num.remove(43)
print(num)
num.pop()
print(num)
num.pop(1)
print(num)
num=[34,56,43,34,24]
num.clear()
   
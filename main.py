# import random
# def sort(algo):
#   for i in range(0, len(algo)-1):
#     for j in range(len(algo)-1):
#       if(algo[j]>algo[j+1]):
#         temp = algo[j]
#         algo[j] = algo[j+1]
#         algo[j+1] = temp
#   return algo

# print(sort([5,3,8,6,7,0,0]))
# def selection_sort(list1):
#   for i in range(len(list1)):
#     min = i
#     for j in range(i+1, len(list1)):
#       if list1[min] >list1[j]:
#         min = j
#       temp = list1[i]
#       list1[i] = list1[min]
#       list1[min] = temp
#   return list1 

# print(selection_sort([4,6,2,6]))
def search(list1, num):
  for i in range(len(list1)):
    if list1[i] == num:
      return i
  return -1

numbers = [1,2,3,4]
num = int(input("number "))
result = search(numbers,num)
if result == -1:
  print("not in this list")
else:
  print("found the number,", result)
print('start')
# list=[1,2,3,4,'a','b']

list1 = ['physics', 'Biology', 'chemistry', 'maths']
print(list1.reverse())

# for element in list:
#   print(element)

# def create_list(n):
#   x_list=[]
#   for i in range(1,n+1):
#     x_list.append(i)
#   return x_list

# print(create_list(100))


def create_even_list(n):
  x_list=[]
  for i in range(1,n+1):
    if i%2==0:
      x_list.append(i)
  return x_list

def sum_of_list(array):
  sum=0
  for element in array:
    sum+=element
  return sum

def multiply_of_list(array):
  result=1
  for element in array:
    result=result*element
  return result

  

array_1 = create_even_list(100)
print(array_1)
print(array_1.reverse())
print(sum_of_list(array_1))
print(multiply_of_list(array_1))












# for i in range(len(list)):
#   if (i+1)%3==0:
#     print(list[i])
# list[0]=list[len(list)-1]
# print(list)
# print(list2)
# new_list= list2+ list
# print(new_list)

# print(list3)

print('end')




# Bubble sort 
ls = [5,1,3,4,2,0,9,6,8,7]
print(ls)
print(" -- Start -- ")

# for i in range(len(ls)-1):
#   for j in range(len(ls)-i-1):
#     if ls[i]>ls[i+j+1]:
#       ls[i],ls[i+j+1]= ls[i+j+1],ls[i]



for i in range(len(ls)-1):
  for j in range(len(ls)-i-1):
    print('step ' + str(i) + '.' + str(j) + ' check elem ' + str(i) + ' and ' + str(j+i+1))
    if ls[i] > ls[j+i+1]:
       ls[i],ls[j+i+1]=ls[j+i+1],ls[i]
       print('swap ' + str(ls[i]) + ' and ' + str(ls[j+i+1]))
       print(ls)
print(" -- Result -- ")
print(ls)

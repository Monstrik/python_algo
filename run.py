# Bubble sort 
ls = [5,1,3,4,2,0,9,6,8,7]
print(ls)
for i in range(len(ls)-1):
  for j in range(len(ls)-i-1):
    if ls[i]>ls[i+j+1]:
      ls[i],ls[i+j+1]= ls[i+j+1],ls[i]
print(ls)
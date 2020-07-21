# Bubble sort 
ls = [64, 25, 12, 22, 11, 90, 5, 1, 3, 4, 2, 0, 9, 6, 8, 7]
print(ls)
print(" -- Start -- ")

for i in range(len(ls)-1):
  for j in range(len(ls)-i-1):
    if ls[i]>ls[i+j+1]:
      ls[i],ls[i+j+1]= ls[i+j+1],ls[i]


# for i in range(len(ls)-1):
#   for j in range(len(ls)-i-1):
#     print('step ' + str(i) + '.' + str(j) + ' check elem ' + str(i) + ' and ' + str(j+i+1))
#     if ls[i] > ls[j+i+1]:
#        ls[i],ls[j+i+1]=ls[j+i+1],ls[i]
#        print('swap ' + str(ls[i]) + ' and ' + str(ls[j+i+1]))
#        print(ls)
# print(" -- Result -- ")
# print(ls)



def bubbleSort(arr):
    n = len(arr)
    # Traverse through all array elements
    for i in range(n - 1):
        # range(n) also work but outer loop will repeat one time more than needed.
        # Last i elements are already in place
        for j in range(0, n - i - 1):

            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# bubbleSort(ls)
print("Sorted array is:")
print(ls)

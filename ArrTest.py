import array

arr=array.array('i',[1,2,3,])
z=len(arr)
x=arr.index(3)
print("Newly created array is :",end=" ")
for i in range(0,3):
    print(arr[i],end=",")
print(z,x)
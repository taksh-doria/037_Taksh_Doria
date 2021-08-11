
import nupmy as np

array1=np.empty(2,3)
array2=np.empty(3,2)


for i in range(0,2):
    list=[]
    for j in range(0,3):
        list.append(random())
    np.append(array1,list,axis=i)


for i in range(0,3):
    list=[]
    for j in range(0,2):
        list.append(random())
    np.append(array2,list,axis=i)

multiply=np.matmul(array1,array2)


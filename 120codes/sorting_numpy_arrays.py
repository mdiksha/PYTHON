#Sorting using the inbuilt sort function

import numpy as np
a = np.array([34, 5, 89, 23, 76])
print("Sorting using the inbuilt sort function = ",np.sort(a))

#Sorting without using the inbuilt sort function

def sorting(x):
    for i in range(len(x)):
        swap = i + np.argmin(x[i:])
        (x[i], x[swap]) = (x[swap], x[i])
    return x
print("Sorting without using the inbuilt sort function = ",sorting(a))

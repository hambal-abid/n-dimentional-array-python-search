import numpy as np

def print_array(L, c = []):

    i = 0
    c.append(i)
    while i < len(L):
        c[len(c)-1] = i

        if type(L[i]) == np.ndarray or type(L[i]) == list:
            print_array(L[i],c)
        else:
            if len(c) > 1:
                print(str(tuple(c))+' = '+str(L[i]))
            else:
                print(str(tuple(c)).rstrip(',)') + ')' + ' = '+str(L[i]))
        i += 1
    c.pop()

# a = [1,2,3]
# a = np.array([[1,2,3],[4,5,6]])
# a = np.array([[[1,2,3],[4, 5, 6 ]],[[7,8,9],[10,11,12]]])
# a = [[2,3,[47,56,67]],[4,5,6,7,[3333,[200,[66]]]]]
print_array(a)
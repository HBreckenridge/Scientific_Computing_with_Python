#expected
alist = ['blue', 'blue', 'blue', 'test', 'yellow', 'yellow']
#drawn
blist = ['blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'green', 'green', 'green', 'red', 'test', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow']
#a = ['blue', 'blue', 'blue', 'test', 'yellow', 'yellow']
#b = ['blue', 'green', 'green', 'yellow', 'red', 'test']




def does_A_contain_B(A, B): #remember now A is the larger list
    b_size = len(B)
    for a_index in range(0, len(A)):
        if A[a_index : a_index+b_size]==B:
            return Trueall(True if a.count(item) <= b.count(item) else False for item in a)
    else:
        return False
#sccess = set(b).issubset(a)
if len(alist)> len(blist):
    a = alist
    b = alist
else:
    b = alist
    a = blist

success2= all(True if b.count(item) <= a.count(item) else False for item in b)


#success = (does_A_contain_B(big, small))
#print(success)
print(success2)


 
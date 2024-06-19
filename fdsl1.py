'''
In second year computer engineering class, group A student’s play cricket, group B students play
badminton and group C students play football. Write a Python program using functions to compute
following: -
a. List of students who play both cricket and badminton
b. List of students who play either cricket or badminton but not both
c. Number of students who play neither cricket nor badminton
d. Number of students who play cricket and football but not badminton.
(Note- While realizing the group, duplicate entries should be avoided, Do not use SET built-in functions)

'''

def intersection(l1,l2):
    res=[]
    for i in l1:
        if i in l2:
            res.append(i)
    return res

def union(l1,l2):
    res=l2.copy()
    for i in l1:
        if i not in l2:
            res.append(i)
    return res
    
    
def diff(l1,l2):
    res=[]
    for i in l1:
        if i not in l2: 
            res.append(i)
    return res
            
    

#main

print("\n")

A=['Aarya','Rishi','Om','Siddhi'] #cricket
B=['Samika','Rishi','Misbah'] #badminton
C=['Atharva','Samika','Aarya','Om','Rishi'] #football

print("List of students who play cricket:",A)
print("List of students who play badminton:",B)
print("List of students who play football:",C)

print("\n")

i=intersection(A,B)
print("1.List of students who play both cricket and badminton:",i,"\n")

j=diff(union(A,B),intersection(A,B))
print("2.List of students who play either cricket or badminton but not both:",j,"\n")

k=diff(C,union(A,B))
print("List of students who play neither cricket nor badminton:",k)
print("3.Number of students who play neither cricket nor badminton=",len(k),"\n")

l=diff(intersection(A,C),B)
print("List of students who play cricket and football but not badminton:",l)
print("4.Number of students who play cricket and football but not badminton=",len(l),"\n")


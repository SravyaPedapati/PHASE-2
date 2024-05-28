def ENQ(Q,ele):
    Q.append(ele)
    print(ele,"is added to Q")
def DEQ(Q):
    if len(Q)==0:
        print("Q is empty")
        return
    print(Q[0],"is deleted")
    Q.pop(0)
Q=[]
n=list(map(int,input().split()))
for ele in n:
    ENQ(Q,ele)
print(ENQ)
for ele in n:
    DEQ(Q)
    print(DEQ)
DEQ(Q)

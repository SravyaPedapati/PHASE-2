#program-8#stack implementation
'''def push(stack,ele):
    stack.append(ele)
    print(ele,"is added to the the stack")
def pop(stack):
    if len(stack)==0:
        print("stack is empty")
        return
    print(stack[-1],"is deleted from the stack")
    stack.pop()
nums = list(map(int, input().split()))
#print(nums)
stack = []
for ele in nums:
    push(stack, ele)
print(stack)
for ele in nums:
    pop(stack)
    print(stack)
pop(stack)'''
#program-9#example of stack
def isbalanced(word):
    stack=[]
    for ele in word:
        if ele=='(':
            stack.append(ele)
        else:
            if len(stack)==0:
                return False
            else:
                stack.pop()
    if len(stack)==0:
        return True
    else:
        return False
word=input()
print(isbalanced(word))


        

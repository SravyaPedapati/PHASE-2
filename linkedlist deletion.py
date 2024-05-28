#program-5

'''class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None
def printLinkedList(head):
    currentNode = head 
    while currentNode != None:
        print(currentNode.data, end = " --> ")
        currentNode = currentNode.next
    print()
def insertAtTail(head, ele):
    temp = Node(ele)
    if head == None:
        return temp
 
    tail = head 
    while tail.next != None:
        tail = tail.next 
    tail.next = temp 
    return head
def insertAtSpecificPosition(head, position, ele):
    if position == 0:
        return insertAtHead(head, ele)
 
    temp = Node(ele)
    index = 0 
    currentNode = head 
 
    while index != position - 1:
        currentNode = currentNode.next 
        index += 1 
 
    nextNode = currentNode.next 
    temp.next = nextNode 
    currentNode.next = temp 
    return head
nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
head = None 
for ele in nums:
    head = insertAtTail(head, ele)
print("Final linked list is:")
printLinkedList(head)
 
head =insertAtSpecificPosition(head, 3, 101)
printLinkedList(head)'''

#program-6
'''class Node:
    def __init__(self,data):
        self.data=data
        self. next=None
def printlinkedlist(head):
    currentnode=head
    while currentnode!=None:
        print(currentnode.data,end= "-->")
        currentnode=currentnode.next
    print()
def insertAtTail(head, ele):
    temp = Node(ele)
    if head == None:
        return temp
 
    tail = head 
    while tail.next != None:
        tail = tail.next 
    tail.next = temp 
    return head 
def deleteattail(head):
    if head==None or head.next==None:
        return None
    previous=None
    currentnode=head
    while currentnode.next!=None:
        previous=currentnode.next
        currentnode=currentnode.next
    previous.next=None
    return head
nums=[10,20,30,40]
head=None
for ele in nums:
    head=insertAtTail(head,ele)
    printlinkedlist(head)
print("final")
printlinkedlist(head)   
deleteattail(head)'''
#program-7
'''class Node:
    def __init__(self,data):
        self.data=data
        self. next=None
def printlinkedlist(head):
    currentnode=head
    while currentnode!=None:
        print(currentnode.data,end= "-->")
        currentnode=currentnode.next
    print()
def insertAtTail(head, ele):
    temp = Node(ele)
    if head == None:
        return temp
 
    tail = head 
    while tail.next != None:
        tail = tail.next 
    tail.next = temp 
    return head
def delatspec(head,position):
    index=0
    currentnode=head
    while index!=position-1:
        index+=1
        current=current.next

    nodeToBeDel=current.next
    nextnode=nodeToBeDel.next
    nodeToBeDel=None
    currentNode.next=None
    currentNode.next=nextNode
nums=[10,20,30,40]
head=None
for ele in nums:
    head=insertAtTail(head,ele)
    printlinkedlist(head)
print("final")
printlinkedlist(head)   
delatspec(head,position) '''   

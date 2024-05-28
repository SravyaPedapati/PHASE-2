#program-2
##class student:
##    def __init__(self,name,rollno,maths,physics,chemistry,java,python):
##        self.name=name
##        self.rollno=rollno
##        self.maths=maths
##        self.physics=physics
##        self.chemistry=chemistry
##        self.java=java
##        self.python=python
##
##    def printalldetails(self):
##        print(self.name)
##        print(self.rollno)
##        print(self.maths)
##        print(self.physics)
##        print(self.chemistry)
##        print(self.java)
##        print(self.python)
##
##obj=student("geeth",12,56,46,87,89,67)
##obj.printalldetails()
##obj2=student("sidharth",13,56,76,45,89,75)
##obj2.printalldetails()



#program-3(linked list)
##class node:
##    def __init__(self,data):
##        self.data=data
##        self. next= None
##obj1=node(71)
##obj2=node(72)
##obj3=node(73)
##obj4=node(74)
##obj5=node(75)
##obj6=node(76)
##obj7=node(77)
##obj8=node(78)
##obj9=node(79)
##obj10=node(80)
##
##obj1. next=obj2
##obj2. next=obj3
##obj3. next=obj4
##obj4. next=obj5
##obj5. next=obj6
##obj6. next=obj7
##obj7. next=obj8
##obj8. next=obj9
##obj9. next=obj10
##
##currentdata=obj1
##while currentdata!= None:
##    print(currentdata.data,end="-->")
##    currentdata=currentdata.next

#program-4

##class Node:
##    def __init__(self, data):
##        self.data = data 
##        self.next = None 
## 
##def printLinkedList(head):
##    currentNode = head 
##    while currentNode != None:
##        print(currentNode.data, end = " --> ")
##        currentNode = currentNode.next
##    print()
## 
##def insertAtTail(head, ele):
##    temp = Node(ele)
##    if head == None:
##        return temp
## 
##    tail = head 
##    while tail.next != None:
##        tail = tail.next 
##    tail.next = temp 
##    return head
## 
## 
##nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
##head = None 
##for ele in nums:
##    head = insertAtTail(head, ele)
##    printLinkedList(head)
##print("Final linked list is:")
##printLinkedList(head)

#program-5

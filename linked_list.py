# class Node:
#     def __init__(self,val):
#         self.val=val
#         self.next=None
# class Linked_list:
#     def __init__(self):
#             self.head=None

#     def append(self,val):
#         new_node=Node(val)

#         if self.head is None:
#             self.head=new_node
#         else:
#             curr=self.head

#             while curr.next is not None:
#                 curr=curr.next
#             curr.next=new_node

#     def display(self):
#         curr=self.head
#         while curr is not None:
#             print(curr.val,end="-->")
#             curr=curr.next
#         print("None")
# ll=Linked_list()

# x=int(input("enter the nodes"))
# for i in range(x):
#     val=int(input("enter the number"))
#     ll.append(val)

# ll.display()




class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def append(self,val):
        new_node=Node(val)
        if self.head is  None:
            self.head=new_node
        else:
            curr=self.head
            while curr.next is not None:
                curr=curr.next
            curr.next=new_node
    def delete(self,val):
        temp=self.head
        if temp.next is not None:
            if temp.val==val:
                self.head=temp.next
        else:
            found=False
            prev_node=None
            while temp is not None:
                if temp.val==val:
                    found=True
                    break
                prev_node=temp
                temp=temp.next
                if found:
                    prev_node.next=temp.next
                    return

    def insertion(self,val,post):
        new_node=Node(val)
        if post==0:
            new_node.next=self.head
            self.head=new_node
            return
        curr=self.head
           
        count=0
        while curr is not None and count<post:
            prev_node=curr
            curr=curr.next
            count+=1
        
        if curr is None and count < post:
            print("Position out of range")
            return

        new_node.next = curr
        prev_node.next = new_node

    def travrsal(self):
        curr=self.head
        while curr is not None:
            print(curr.val,end="--->>")
            curr=curr.next
        print("None")
ll=LinkedList()
x=int(input("enter the Node"))
for i in range(x):
    val=int(input("enter the number "))
    ll.append(val)
val=int(input("enter the value to insert "))
post=int(input("enter the post "))
ll.insertion(val,post)
ll.travrsal()
val = int(input("Enter the value to delete: "))

ll.delete(val)

print("After deletion:")
ll.travrsal()
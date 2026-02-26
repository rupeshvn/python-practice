"""
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single 
digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 
itself.

Example 

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807

"""



class Solution:
    def addTwoNumbers(self, l1, l2):
        class Node:
            def __init__(self,val):
                self.val = val
                self.next = None

        def convert_to_ll(list_val):
            base = Node(list_val[0])
            current = base
            for i in list_val[1:]:
                current.next = Node(i)
                current = current.next
            return base

        numberl1 = ""
        numberl2 = ""
        while l1:
            numberl1=numberl1+str(l1.val)
            l1=l1.next
        while l2:
            numberl2 = numberl2+str(l2.val)
            l2=l2.next

        print(numberl1)
        print(numberl2)

        actual_number = str(int(numberl1[::-1])+int(numberl2[::-1]))
        actual_number=actual_number[::-1]
        actual_list=[int(i) for i in actual_number]
        print(actual_list)
        
        return convert_to_ll(actual_list)


class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

def create_linked_list(val_list):
    base = Node(val_list[0])
    current = base
    for i in val_list[1:]:
        current.next = Node(i)
        current = current.next
    return base


sample_list1 = [2,4,3]
sample_list2 = [5,6,4]
list_l1 = create_linked_list(sample_list1)
list_l2 = create_linked_list(sample_list2)

new_obj = Solution()
final_val = new_obj.addTwoNumbers(list_l1,list_l2)
print(final_val.val)


        


        
    



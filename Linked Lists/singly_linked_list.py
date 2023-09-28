"""
Singly linked lists
It's a linear data structure which consists of nodes. These nodes contain values and a pointer which points to the next node with a value. 
The pointers go in one direction. 
"""

class Node:
    def __init__(self, val):
        self.value = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    #Add a new node into the list
    def insert(self, new_node):
        #2 possibilities, 
        # when there already is a list to which the node is added
        # and when a node is added to an empty list
        if self.head:
            temp = self.head
            while (temp.next):
                temp = temp.next
            temp.next = new_node
        else:
            self.head = new_node

    #Display the linked list
    def display(self):
        temp = self.head
        while (temp):
            print(temp.value, end=" -> ")
            temp = temp.next
        print()

    #Search an element in a linked list
    def search(self, val):
        temp = self.head

        while temp:
            if (temp.value == val):
                print('The value is in the linked list')
                return
            temp = temp.next
        print("The value does not exist in the list")

    #Finding the length of a linked list
    def get_length(self):
        count = 0
        if not self.head:
            return count
        
        temp = self.head
        while temp:
            count += 1 
            temp = temp.next
        return count
    
    #Reversing a list 
    def reverse(self):
        temp = self.head
        temp2 = None
        while temp:
            next = temp.next
            temp.next = temp2
            temp2 = temp
            temp = next
        self.head = temp2

    #Deleting a value in a linked list
    def deletion(self, val):
        temp = self.head
        if (temp.value == val):
            self.head = self.head.next
            return 
        while temp:
            if temp.next.value == val:
                temp.next = temp.next.next
                return
            temp = temp.next
        print("The value is not in the list")

    #Deleting a node given the position
    def delete_pos(self, val):
        temp = self.head
        if not temp:
            print("List is empty")
            return
        if (val >= self.get_length()):
            print('List not long enough')
            return
        if val == 0:
            self.head = self.head.next
        count = 1
        while temp:
            if count == val:
                temp.next = temp.next.next
                return
            temp = temp.next
            count += 1

    #Delete the entire linked list
    def clean_slate(self):
        if self.head == None:
            print("List is empty")
            return
        self.head = None

###################################################################################################################
###################################################################################################################
    #Easy problems

    #Comparing 2 linked lists and checking if they are equal
    def compare(self, linked_list_2):
        #If the 2 lists don't have equal length, they are automatically unequal
        if (self.get_length() != linked_list_2.get_length()):
            print('The lists are not equal')
            return
        temp1 = self.head
        temp2 = linked_list_2.head
        while temp1:
            #While looping through the lists, if any pair of values are unequal, the lists are unequal
            if temp1.value != temp2.value:
                print("The lists are not equal")
                return
            temp1 = temp1.next
            temp2 = temp2.next
        #If the enitre loop runs without breaking, the lists are equal
        print("The lists are equal")
    
    #Find the middle node in the list
    def middle(self):
        #Checking what will be the middle value
        mid = self.get_length()//2
        temp = self.head
        c = 0
        while temp:
            #Run the loop until we get to the middle value
            temp = temp.next
            c += 1
            if c == mid:
                print("Middle value: ", temp.value)
                return
    
    #Get nth node in list
    def get_n_node(self, n):
        temp = self.head
        len = 0
        while temp:
            len += 1
            temp = temp.next
        temp = self.head
        co=0
        while temp:
            #While traversing, once we reach the target node, we display the value there
            if (co == n):
                print("The value on node no {} is {}".format(n, temp.value))
                return
            #Otherwise, it keeps moving forward
            else:
                co += 1
                temp = temp.next 
        #If we're unable to find the position, that means the list is not big enough
        print("The input position is greater than the list length")
        return
        
    #Get Nth node from end of list
    def get_n_from_last(self, n):
        temp = self.head
        len = 0
        while temp:
            len += 1
            temp = temp.next
        #If the given value is not within the list
        if (len < n):
            print("The list in not big enough")
            return
        temp = self.head
        #Run the list to get to the right position
        for i in range(0, len-n):
            temp = temp.next
        print("The value on position {} from last is {}".format(n, temp.value))

    #Shift the last node to the first
    def shift_from_last(self):
        if self.head == None:
            print("List is empty")
            return
        temp = self.head
        if self.head.next == None:
            print("The list only has 1 node")
            return
        last_node = None
        #Run the loop to get to the last node, after which the last node is picked and put at the head 
        while temp and temp.next:
            if temp.next.next == None:
                last_node = temp.next
                temp.next = None
            else:
                temp=temp.next
        last_node.next = self.head
        self.head = last_node

    #Shift the middle node to the head
    def shift_from_mid(self):
        len = self.get_length()
        if len < 3:
            print('List not big enough')
            return
        mid = len // 2
        c = 0
        mid_node = None
        temp = self.head
        while temp:
            #Run the loop until we get to the middle value
            temp = temp.next
            c += 1
            #Once we get to the node just before the middle node, we take out
            # the middle node and connect the nodes adjacent to the middle node 
            if c == mid-1:
                mid_node = temp.next
                temp.next = temp.next.next
                break
        #The middle node is taken and put to the head, and itself as head
        mid_node.next = self.head
        self.head = mid_node
        return
    
    #Delete the alternate nodes
    def del_alternate(self):
        temp = self.head
        if not temp:
            print("There's no list")
            return
        while temp and temp.next:
            #While we loop through the list, the next of each node is shifted to the next, next node
            # thereby skipping the alternate nodes
            temp.next = temp.next.next
            temp = temp.next

    #Add 1 to the linked list
    def add_1(self):
        #Reverse the list, so that the addition process can be done easily
        self.reverse()
        temp = self.head
        carry = 1
        while temp:
            #Each term in the list is added to carry
            temp.value += carry
            if temp.value >= 10:
            #If the number becomes 10 or more(unlikely), 1 is carried over to the next number and the current
            # val becomes single digit
                temp.value = temp.value%10
                carry = 1
            else:
            #Otherwise there's no carry over
                carry = 0
            temp = temp.next
        #Binging the list back to original list
        self.reverse()

    #Add 2 numbers which are linked lists, make sure the sum is also a linked list 
    def add_2_numbers(self, ll_2):
        num1, num2 = 0, 0
        temp1, temp2 = self.head, ll_2.head
        while temp1:
        #Using the loop to run through the list, and making a number out of it
            num1 += temp1.value
            if temp1.next:
                num1 *= 10
            temp1 = temp1.next
        while temp2:
        #Using the loop to run through the list, and making a number out of it
            num2 += temp2.value
            if temp2.next:
                num2 *= 10
            temp2 = temp2.next
        s = num1 + num2
        list_s = LinkedList()
        #Making a new list, which will contain the numbers in the sum
        while s:
            r = s%10
            s = s//10
            list_s.insert(Node(r))
        list_s.reverse()
        return list_s

    #Subtract 2 numbers which are linked lists, make sure the final result is a linked list
    def subtract_2_numbers(self, ll_2):
        num1, num2 = 0, 0
        temp1, temp2 = self.head, ll_2.head
        while temp1:
        #Using the loop to run through the list, and making a number out of it
            num1 += temp1.value
            if temp1.next:
                num1 *= 10
            temp1 = temp1.next
        while temp2:
        #Using the loop to run through the list, and making a number out of it
            num2 += temp2.value
            if temp2.next:
                num2 *= 10
            temp2 = temp2.next
        s = 0
        #Making sure the smaller number is subtracted from the larger number
        if (num1>num2):
            s = num1 - num2
        else:
            s = num2 - num1
        list_s = LinkedList()
        while s:
        #Making a new list, which will contain the numbers in the result
            r = s%10
            s = s//10
            list_s.insert(Node(r))
        list_s.reverse()
        return list_s
    
    #Find the sum of the last n nodes in the list
    def sum_last_n(self, n):
        temp = self.head
        len_list = self.get_length()
        #Get to the nth node from the end
        for _ in range(len_list-n):
            temp = temp.next
        sum = 0
        #Add up the remaining nodes
        while temp:
            sum += temp.value
            temp = temp.next
        return sum
    
    #Swap pairs of nodes in a list
    def swap_pairs(self):
        temp = self.head
        while temp:
            if temp.next == None:
                break
            else:
                temp.value, temp.next.value = temp.next.value, temp.value
                temp = temp.next.next

    #Delete every kth node in the list
    def delete_k(self, k):
        temp = self.head
        if k == 1:
            self.head = None
            return
        c = 1
        while temp:
            if c+1 == k:
                c = 1
                if temp.next != None:
                    temp.next = temp.next.next
            else:
                c += 1
            temp = temp.next 

###################################################################################################################
###################################################################################################################
    #Medium problems        
    
    #Check if the list is palindrome 
    def is_palindrome(self):
        if not self.head or not self.head.next:
            print("Is palindrome")
            return
        temp = self.head
        r = []
        while temp:
            r.append(temp.value)
            temp = temp.next
        if (r == r[::-1]):
            print("The list is a palindrome")
            return
        else:
            print("The list is NOT a palindrome")
            return
    
    #Remove the duplicates in a list(Any type of list: sorted or unsorted)
    def remove_duplicates(self):
        #Node current will point to head  
        temp = self.head;  
        index = None;  
        t = None;   
        if(self.head == None):
            print("The list is empty")  
            return;  
        else:  
            while(temp != None):  
                #Node t will point to previous node to index.  
                t = temp;  
                #Index will point to node next to temp 
                index = temp.next;  
                  
                while(index != None):  
                    #If current node's data is equal to index node's data  
                    if(temp.value == index.value):  
                        #Here, index node is pointing to the node which is duplicate of temp node  
                        #Skips the duplicate node by pointing to next node
                        t.next = index.next;  
                    else:  
                        #t will point to previous node of index.  
                        t = index;  
                    index = index.next;  
                temp = temp.next;  

    # #Remove ALL duplicate nodes in the list
    # def remove_all_duplicates(self):
    #     cur = self.head
    #     h = prev = Node(None)
    #     h.next = cur
    #     while cur and cur.next:
    #         if cur.value == cur.next.value:
    #             while (cur and cur.next and cur.value == cur.next.value):
    #                 cur = cur.next
    #             cur = cur.next
    #             prev.next = cur
    #         else:
    #             prev = prev.next
    #             cur = cur.next

    # Swapping nodes(NOT VALUES WITHIN) in a list
    def swap_nodes(self, x, y):
        #If the values are the same
        if x == y:
            print("No point in swapping/ nodes are the same")
            return
        #If the list is empty
        if not self.head:
            print("List is empty")
            return
        prev_x = None
        cur_x = self.head
        #Setting 2 variables to catch the x node and the node before it
        while cur_x != None and cur_x.value != x:
            prev_x = cur_x
            cur_x = cur_x.next
        
        prev_y = None
        cur_y = self.head
        #Setting 2 more variables to catch the y node and the node before it
        while cur_y != None and cur_y.value != y:
            prev_y = cur_y
            cur_y = cur_y.next
        
        #If either or both nodes don't exist
        if not cur_x or not cur_y:
            print("One or both of the nodes are not present in the list")
            return
        if prev_x != None:
        #If x node is not the head node
            prev_x.next = cur_y
        else:
        #If x node is the head node
            self.head = cur_y

        if prev_y != None:
            #If y node is not the head node
            prev_y.next = cur_x
        else:
            #If y node is the head node
            self.head = cur_x

        #Implement the switch
        temp = cur_x.next
        cur_x.next = cur_y.next
        cur_y.next = temp 

    #Segregate odd and even numbers in the list
    def segregate_odd_even(self):
        temp = self.head

        odd, oddTail = None, None
        even, evenTail = None, None

        while temp:
            if temp.value % 2 == 0:
            #If the node is even valued
                if even is None:
                    even = evenTail = temp
                else:
                    evenTail.next = temp
                    evenTail = temp
            else:
            #If the node is odd valued
                if odd is None:
                #If the odd list is not created, it will be now
                    odd = oddTail = temp
                else:
                #If the even list is not created, it will be now
                    oddTail.next = temp
                    oddTail = temp
            temp = temp.next
        if even:
        #If even list was created, it's head is set as the real head, 
        # and it's tail connected to the next of the odd
            self.head = even
            evenTail.next = odd
        else:
        #If there is no even list, the odd list becomes the real list
            head = odd
        if oddTail:
        #If the oddTail has some set value, set the next to none
            oddTail.next = None

    #Alternate odd even nodes in the list
    def alternate_odd_even(self):
        temp = self.head
        odd, even = [], []
        i = 1
        while temp:
            #Adding the nodes in the lists
            if (temp.value%2!=0 and i%2==0):
                odd.append(temp)
            elif (temp.value%2==0 and i%2!=0):
                even.append(temp)
            temp = temp.next
            i += 1
        while (len(odd)!=0 and len(even)!=0):
            #Switching the odd even values
            odd[-1].value, even[-1].value = even[-1].value, odd[-1].value
            odd.pop()
            even.pop()

###################################################################################################################
###################################################################################################################
    #Hard problems    

    #Reverse a linked list in a set  
    # eg, 1->2->3->4->5  k=3
    # 3->2->1->4->5 
    # def reverse_set(self, k):
    #     temp = self.head
    #     if not temp:
    #         print("Empty list")
    #         return
    #     current = self.head
    #     next, prev = None, None
    #     count = 0
    #     while (current is not None and count < k):
    #         next = current.next
    #         current.next = prev
    #         prev = current
    #         current = next
    #         count+=1
    #     if next is not None:
    #         self.head.next = self.reverse_set(next, k)
        

            
        





        

            



if __name__=="__main__":
    new_list = LinkedList()
    new_list.insert(Node(2))
    new_list.insert(Node(1))
    new_list.insert(Node(4))
    new_list.insert(Node(3))
    new_list.insert(Node(5))
    new_list.insert(Node(6))
    
    new_list.display()
    #new_list.search(3)
    #new_list.search(0)
    #print("The length of the list is: ", new_list.get_length())
    #new_list.reverse()
    #new_list.deletion(6)
    # new_list.delete_pos(5)
    #new_list.middle()
    #new_list.get_n_node(0)
    #new_list.get_n_from_last(4)
    #new_list.shift_from_last()
    #new_list.shift_from_mid()
    #new_list.del_alternate()
    #new_list.add_1()
    #sum = new_list.sum_last_n(1)
    #print(sum)
    #new_list.swap_pairs()
    #new_list.delete_k(4)
    #new_list.remove_duplicates()
    #new_list.is_palindrome()
    #new_list.remove_all_duplicates()
    #new_list.swap_nodes(1, 4)
    #new_list.segregate_odd_even()
    new_list.alternate_odd_even()
    new_list.display()



    # new_list_2 = LinkedList()
    # new_list_2.insert(Node(1))
    # new_list_2.insert(Node(2))
    # new_list_2.insert(Node(3))
    # new_list_2.insert(Node(4))
    # new_list_2.insert(Node(6))
    # new_list_2.insert(Node(6))
    # new_list.compare(new_list_2)

    # l_list_1 = LinkedList()
    # l_list_2 = LinkedList()
    # l_list_2.insert(Node(1))
    # l_list_2.insert(Node(2))
    # l_list_2.insert(Node(3))

    # l_list_1.insert(Node(1))
    # l_list_1.insert(Node(9))
    # l_list_1.insert(Node(6))
    # l_list_1.insert(Node(0))
    # l_list_1.insert(Node(2))


    # l_list_1.display()
    # l_list_2.display()
    # #sum_list = l_list_1.add_2_numbers(l_list_2)
    # #sum_list.display()
    # res_list = l_list_1.subtract_2_numbers(l_list_2)
    # res_list.display()




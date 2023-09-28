"""
Doubly Linked List
A linear data structure similar to singly linked lists. In single linked lists, there a pointer going in one direction, 
but in double linked lists, each node has 2 pointers, one pointing to the next node and another to the previous node
"""

class Node:
    def __init__(self, value):
        #Initializing the node. Here a node will have the current node value, the previous node and the next node.
        self.prev = None
        self.data = value
        self.next = None

class LinkedList:
    def __init__(self):
        #Initializing the list which will have a start and end
        self.start = None
        self.end = None

    def insert(self, new_node):
        #Adding a new node into the list. 
        #2 possible cases, if there is a list and if there isn't
        if self.start is None:
            #If there's no list, the new node will be both start and end
            #The prev of the head and the end of the tail will be none 
            self.start = self.end = new_node
            self.start.prev = None
            self.end.next = None
        else:
            #If there already is a list, the node will be added at 
            # the end of the list, ie after the tail
            #The tail next will be the new node, the prev of the 
            # new node will be the tail, and the new tail will be the newly added node
            self.end.next = new_node
            new_node.prev = self.end
            self.end = new_node
            self.end.next = None

    def display(self):
        #Displays the node
        temp = self.start
        while temp!=None:
            print(temp.data, end=" <=> ")
            temp = temp.next
        print()

    def display_reverse(self):
        #Displays the node in reverse
        temp = self.end
        while (temp != None):
            print(temp.data, end=" <=> ")
            temp = temp.prev
        print()

    def delete_node(self, node):
        check = False
        #Checks if the node is at the start of the list
        if self.start.data == node:
            self.start = self.start.next
            self.start.prev = None
            check = True
        #Checks if the node is at the end of the list
        elif self.end.data == node:
            self.end = self.end.prev
            self.end.next = None
            check = True
        #In case the node is somewhere in the list
        else: 
            temp = self.start
            while (temp):
                if (temp.data == node):
                    check = True
                    #Once the node is found, 
                    # it's previous node's next pointer will be shifted to the one after that, 
                    # and the next node's previous will be shifted to the previous on
                    temp.prev.next = temp.next
                    temp.next.prev = temp.prev
                    check = True
                temp = temp.next
        #The the node does not exist in the list
        if check == False:
            print("Given value does not exist in the node")

###################################################################################################################
###################################################################################################################
    #Easy problems

    def list_length(self):
        #Find the length of the list
        temp = self.start
        count = 0
        #Each time the list is traversed, the length increases by 1
        while temp:
            count += 1
            temp = temp.next
        return count
    
    def max_val(self):
        #Find the larget value available in the list
        temp = self.start
        high_val = self.start.data
        while temp:
            if (temp.data > high_val):
                high_val = temp.data
            temp = temp.next
        return high_val 
    
    def find_sum_pair(self, val):
        #For a given sorted list with DISTINCT elements, check if it contains pairs of numbers whose sum equals to the given value
        temp_first = self.start
        temp_second = self.end
        found = False
        sets = []
        len = self.list_length()
        #While the first and second values don't cross each other, the loop keeps running
        while (temp_first != temp_second and temp_second.prev != temp_first):
            if (temp_first.data + temp_second.data == val):
                #If a pair is found, the set is added to the list, and both the pointers are moved
                sets.append([temp_first.data, temp_second.data])
                found = True
                temp_first = temp_first.next
                temp_second = temp_second.prev
            else:
                #If the pair does not equal the sum, one of the pointers are 
                # moved until either the result is obtained or the loop condition stays valid
                if ((temp_first + temp_second) < val):
                    temp_first = temp_first.next
                else:
                    temp_second = temp_second.prev
        if found:
            print("The pairs whose sum is the given value is: ", sets)
        else:
            print("There are no pairs in the list whose sum is the given value")

    def is_palindrome(self):
        #Check if the given list/string is a palindrome
        temp_first = self.start
        temp_second = self.end
        br = False
        #Run the loop 
        while (temp_first.next != None):
            if (temp_first.data == temp_second.data):
            #If the 2 nodes on opposite ends are equal, then we move forward and check
                temp_second = temp_second.prev
                temp_first = temp_first.next
            else:
            #Even if there is 1 case of characters not being equal, the list is not a palindrome
                br = True
                break
        if not br:
            print("The linked list is a palindrome")
        else:
            print("It's not a palindrome")
    
    def sorted_insert(self, new_val):
        #Inserting a value in a sorted list (increasing)
        new_val = Node(new_val)
        temp_first = self.start
        temp_second = self.end
        while temp_first:
            #If we find place of insertion
            if (temp_first.data <= new_val.data and temp_first.next.data >= new_val.data):
                #The new node's next will be the prev node's original next
                # and the new node's prev will be the  prev node
                new_val.next, new_val.prev = temp_first.next, temp_first.next.prev
                #The prev node's next will be the new node and the 
                # next node's prev will be the new node
                #Since the new node is AREADY ADDED in the prev line, here we refer to the 
                # original next and next of next node
                temp_first.next, temp_first.next.next.prev = new_val, new_val
                break
            temp_first = temp_first.next

    def rotate_list(self, n):
        #Rotate the given list n times
        #If the list is 1 <=> 2 <=> 3 <=> 4 <=> 5 and n=3,
        # the resultant list should be 4 <=> 5 <=> 1 <=> 2 <=> 3
        temp_first = self.start
        temp_second = self.end
        if (n == 0):
            return 
        #Original list's start and end are connected to make a loop
        self.start.prev = self.end
        self.end.next = self.start
        while n != 0:
            #Getting to the point where the rotation will occur
            temp_first = temp_first.next
            n -= 1
        #Establishing the new start and end of the list
        self.start, self.end = temp_first, temp_first.prev
        #Breaking the loop so that the list does not become a circular list
        temp_first.prev.next, temp_first.prev = None, None

###################################################################################################################
###################################################################################################################
    #Medium problems

    # def insertion_sort(self):
    #     sorted = None
    #     current = self.start
    #     while (current != None):
    #         next = current.next

    #         current.prev = current.next = None

    #         sorted = self.sort_insert(sorted, current)
    #         current = next
    #     self.start = sorted
    #     return self.start
    
    # def sort_insert(self, ref, node):
    #     current = None

    #     if ref == None:
    #         ref = node
    #     elif (ref.data >= node.data):
    #         node.next = ref
    #         node.next.prev = node
    #         ref = node
    #     else:
    #         temp = node
    #         while (temp.next != None and temp.next.data < node.data):
    #             temp = temp.next
    #         node.next = current.next

    #         if (temp.next != None):
    #             node.next.prev = node
            
    #         temp.next = node
    #         node.prev = temp
    #         return ref

    def remove_duplicates(self):
        #For a given sorted double linked list, remove all the duplicate values and create a unique value linked list
        if self.start == None:
            return None
        
        temp = self.start
        #next = None
        while (temp.next != None):
            if (temp.data == temp.next.data):
                temp_2 = temp.next
                #If the next value is the same as prev value, loop is set to run until we get the next unique value, after which we 
                # set the new link, thereby removing all the duplicates in the middle
                while (temp_2.data == temp.data):
                    temp_2 = temp_2.next
                temp.next = temp_2
                temp_2.prev = temp 
            else:
                temp = temp.next

    def triplets_sum(self, val):
        #For a give sorted linked list with unique node values, find out the number of triplets whose sum equals to the 
        # given value.
        res = []
        #Establishing temp start and end variables
        temp_start, temp_end = self.start, self.end
        #Setting a loop while setting the temp start 
        while temp_start.next.next != None:
            #Creating a target sum for the remaining pair(By substracting the start variable)
            cur_sum = val - temp_start.data
            #Setting a third variable
            temp_mid = temp_start.next
            #Setting another loop to set different values to find the other 2 variables
            while temp_mid and temp_end and temp_mid != temp_end:
                pair_sum = temp_mid.data + temp_end.data
                if pair_sum == cur_sum:
                    #If the pair of numbers are equal to the 'target sum', the triplet set are added to the results
                    res.append([temp_start.data, temp_mid.data, temp_end.data])
                    temp_mid = temp_mid.next
                elif pair_sum > cur_sum:
                    #If the sum of pair is greater than the 'target value', the end variable is reduced by shifting to the previous node
                    temp_end = temp_end.prev
                else:
                    #If sum of pair is less than target sum, middle value is increased by setting it to next node
                    temp_mid = temp_mid.next
            #Process is repeated with the new start variable
            temp_start = temp_start.next
        return res
    
    """
    def biotonic_sort(self):
        #A biotonic list (First increasing order, then decreasing) is to be sorted completely in increasing order
        temp_start_1, temp_end_1 = self.start, None
        temp_start_2, temp_end_2 = None, self.end
        temp = self.start
        if (not temp):
                print('List is empty')
        while (temp):
            if (temp.next.data < temp.data):
                temp_end_1, temp_end_1.next = temp, None
                temp_start_2, temp_start_2.prev = temp.next, None
            temp = temp.next
        #temp, star, en = self.start, self.start, self.start
        temp_1, temp_2 = temp_start_1, temp_start_2
        while (temp_2):
            if (temp_1.data < temp_2.data):
    """

    def del_occurance(self, val):
        temp = self.start
        while (temp):

            if (temp.data == val):
                if (temp.prev == None):
                    #Checking if the node is starting node
                    self.start = self.start.next
                    self.start.prev = None
                elif (temp.next == None):
                    #Checking if the node is ending node
                    self.end = self.end.prev
                    self.end.next = None
                    temp = self.end
                else:
                    #Checking node between start and end
                    temp.prev.next = temp.next
                    temp.next.prev = temp.prev
            temp = temp.next
            

###################################################################################################################
###################################################################################################################

            
        






if __name__=="__main__":
    linked_list = LinkedList()
    linked_list.insert(Node(4))
    linked_list.insert(Node(4))
    linked_list.insert(Node(4))

    linked_list.insert(Node(1))
    linked_list.insert(Node(2))
    linked_list.insert(Node(4))
    linked_list.insert(Node(5))
    linked_list.insert(Node(6))
    linked_list.insert(Node(4))
    linked_list.insert(Node(4))
    linked_list.insert(Node(4))
    linked_list.insert(Node(8))
    linked_list.insert(Node(4))
    linked_list.insert(Node(4))
    linked_list.insert(Node(4))

    linked_list.insert(Node(9))
    linked_list.insert(Node(4))
    linked_list.insert(Node(4))

    #linked_list.insert(Node(7))
    #linked_list.insert(Node(7))
    #linked_list.insert(Node(9))
    #linked_list.delete_node(3)
    linked_list.display()
    linked_list.del_occurance(4)
    #linked_list.display_reverse()
    ##linked_list.sorted_insert(6)
    #linked_list.rotate_list(3)
    #linked_list.display_reverse() 
    #linked_list.remove_duplicates()
    linked_list.display()  
    #print("The length of the list is: ", linked_list.list_length())
    #print("The maximum value in the list is: ", linked_list.max_val())
    #print("The set of triplets are: ", linked_list.triplets_sum(15))
    #linked_list.find_sum_pair(7)

    # linked_list = LinkedList()
    # linked_list.insert(Node('l'))
    # linked_list.insert(Node('e'))
    # linked_list.insert(Node('v'))
    # #linked_list.insert(Node(10))
    # linked_list.insert(Node('e'))
    # linked_list.insert(Node('l'))
    # linked_list.is_palindrome()
            
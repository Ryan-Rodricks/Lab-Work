"""
-------------------------
# Student Name: Ryan Rodricks
# Student ID: 190499940
# Student email: rodr9940@mylaurier.ca
#-------------------------
"""

from copy import deepcopy

class Stack:
    """
    -------------------------------------------------------
    Implementation of Stack ADT (Array-based Implementation)
    Top of Stack is the last element in the Python list
    -------------------------------------------------------
    """
    def __init__(self,size):
        """
        -------------------------------------------------------
        Description:
            Initializes a Stack Object
            Initializes items to an empty list
        Use: stack = Stack()
        -------------------------------------------------------
        Parameters:
            None
        Returns:
            A Stack object (Stack)            
        -------------------------------------------------------
        """
        self.items = []
        self.size = size
    
    def peek(self):
        """
        -------------------------------------------------------
        Description:
            Returns a copy of top of stack
            if Stack is empty prints error msg and returns None
        Use: item = stack.peek()
        -------------------------------------------------------
        Parameters:
            None
        Returns:
            An item from top of stack (?)            
        -------------------------------------------------------
        """
        result = None
        if self.is_empty():
            print('Error(Stack.peek):Invalid peek operation. Stack is empty')
        else:
            result = deepcopy(self.items[0])
        return result
    
    def push(self,item):
        """
        -------------------------------------------------------
        Description:
            Adds an item to the stack
        Use: stack.push(item)
        -------------------------------------------------------
        Parameters:
            item - An item to be added to the stack (?)
        Returns:
            None           
        -------------------------------------------------------
        """
        if self.is_full():
            print("Error(Stack.push):Invalid push operation. Stack is full")
        else:
            return self.items.insert(0,item)
        
    
    def pop(self):
        """
        -------------------------------------------------------
        Description:
            Removes the top item of the stack
            if Stack is empty prints error msg and returns None
        Use: item = stack.pop()
        -------------------------------------------------------
        Parameters:
            None
        Returns:
            item - An item from top of stack (?)            
        -------------------------------------------------------
        """
        if self.is_empty():
            print('Error(Stack.pop):Invalid pop operation. Stack is empty')
            return None
        return self.items.pop(0)
    
    def is_empty(self):
        """
        -------------------------------------------------------
        Description:
            checks if stack is empty
        Use: result = stack.is_empty()
        -------------------------------------------------------
        Parameters:
            None
        Returns:
            True if stack is empty, False otherwise
        -------------------------------------------------------
        """
        return len(self.items)== 0
    
    def is_full(self):
        return len(self.items)==int(self.size)+1
    
        
def print_stack(stack):
    """
    -------------------------------------------------------
    Description:
        Utility function for testing purposes only
        Prints contents of stack
        First line is: size = stack_size
        Next lines contain stack items, each in separate line
        Top of stack is printed first
    Use: print_stack(stack)
    -------------------------------------------------------
    Parameters:
        stack - a stack object to be printed (Stack)
    Returns:
        None
    -------------------------------------------------------
    """
    size_stack = stack.size
    temp = []
    print("size = {}".format(size_stack))
    if stack.is_empty():
        print("[]")
        
        
    while not stack.is_empty():
        temp.append(stack.pop())
        
    for i in temp:
        stack.push(i)
        print(i) 
def list_to_stack(list1):
    """
    -------------------------------------------------------
    Description:
        Convert a list to a stack
        First item in list will be the bottom of stack
        Last item in list will be the top of the stack
    Use: stack = list_to_stack(list1)
    -------------------------------------------------------
    Parameters:
        list1 - a list to be copied into a new stack (list)
    Returns:
        stack - a newly created stack objects with items from list (Stack)
    -------------------------------------------------------
    """
    s = Stack(len(list1))
    for x in list1:
        s.push(x)
    return(s)

def students_to_stack(filename, size):
    """
    -------------------------------------------------------
    Description:
        Reads the contents of a file into a stack
        The file stores student information, each in separate line
            sid:last,first
        The stack is initialized with the given size
        The function does not perform file reading if stack is full 
    Use: stack = students_to_stack(filename,size)
    -------------------------------------------------------
    Parameters:
        filename - name of input file (str)
        size - Maximum stack size (int)
    Returns:
        stack - a stack containing student objects (Stack)
    -------------------------------------------------------
    """
    stack = Stack(size)
    file = open(filename,"r")
    in_file = file.readlines()
    for line in in_file:
        stack.push(line.rstrip("\n"))
    return stack
    

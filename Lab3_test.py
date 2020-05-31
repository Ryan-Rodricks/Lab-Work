#------------------------------
# CP264 Winter 2020
# Week 3 - Lab3
# Stacks - Array Based
# Testing File
#------------------------------
from Lab3 import Stack,print_stack,students_to_stack, list_to_stack

def test_stack():
    print('{}'.format('-'*20))
    print('Testing Stack class:\n')
    
    print('Creating a new stack:')
    s = Stack(3)
    print(type(s))
    print('Printing Contents of Stack: ')
    for item in s.items:
        print(item)
    print('Is empty? = {}'.format(s.is_empty()))
    print('Is full? = {}'.format(s.is_full()))
    print('Peek: ')
    item = s.peek()
    print('item = {}'.format(item))
    print('Pop: ')
    item = s.pop()
    print('item = {}'.format(item))
    print()
    
    print('Push integer 5 and print stack:')
    s.push(5)
    for item in s.items:
        print(item)
    print('Is empty? = {}'.format(s.is_empty()))
    print('Is full? = {}'.format(s.is_full()))
    print('Peek: ')
    item = s.peek()
    print('item = {}'.format(item))
    print()
    
    print('Push integer 10 then 15 and print stack:')
    s.push(10)
    s.push(15)
    for item in s.items:
        print(item)
    print('Is empty? = {}'.format(s.is_empty()))
    print('Is full? = {}'.format(s.is_full()))
    print('Peek: ')
    item = s.peek()
    print('item = {}'.format(item))
    print()
    print('Push integer 20 and print contents of stack:')
    s.push(20)
    for item in s.items:
        print(item)
    print('Pop, print item and then print stack: ')
    item = s.pop()
    print('item = {}'.format(item))
    for item in s.items:
        print(item)
    print()
    
    print('End of stack class testing')
    print('{}\n'.format('-'*20))
    return

def test_print():
    print('{}'.format('-'*20))
    print('Testing print_stack:\n')
    
    print('Printing an empty stack of size 5: ')
    stack = Stack(5)
    print_stack(stack)
    print()
    
    print('filling stack with 1 to 5, then print:')
    for i in range(1,6):
        stack.push(i)
    print_stack(stack)
    print()
    
    
    print('End of print_stack testing')
    print('{}\n'.format('-'*20))
    return

def test_list_to_stack():
    print('{}'.format('-'*20))
    print('Testing list_to_stack:\n')
    
    print('Converting [] to a stack')
    stack1 = list_to_stack([])
    print_stack(stack1)
    print()
    
    print('Converting [10,20,30] to a stack')
    stack2 = list_to_stack([10,20,30])
    print_stack(stack2)
    print()
    
    list3 = [[1,2,3],[4,5,6],[7,8,9]]
    print('Converting {} to a stack: '.format(list3))
    stack3 = list_to_stack(list3)
    #list3[0][0] = 100
    print_stack(stack3)
    print()
    
    print('End of list_to_stack testing')
    print('{}\n'.format('-'*20))
    return

def test_students_to_stack():
    print('{}'.format('-'*20))
    print('Testing test_count:\n')
    
    filename1 = 'students1.txt'
    print('Reading {} int a stack of size 12 '.format(filename1))
    stack = students_to_stack(filename1,12)
    print_stack(stack)
    print()
    
    filename2 = 'students2.txt'
    print('Reading {} int a stack of size 12 '.format(filename2))
    stack = students_to_stack(filename2,12)
    print_stack(stack)
    print()
    
    filename3 = 'students3.txt'
    in_file = open(filename3,'w')
    in_file.close()
    print('Reading {} int a stack of size 12 '.format(filename3))
    stack = students_to_stack(filename3,12)
    print_stack(stack)
    print()
    
    print('End of students_to_stack testing')
    print('{}\n'.format('-'*20))
    return

#test_stack()
#test_print()
#test_list_to_stack()
#test_students_to_stack()
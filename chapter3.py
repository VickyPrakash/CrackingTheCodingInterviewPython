# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 19:13:34 2019

@author: vicky
"""

class Stack:
    def __init__(self):
        self.items = [];
        self.minimum = 100000000000;
        
    def isEmpty(self):
        return self.items == [];
    
    def push(self, item):
        if (self.minimum > item):
            self.minimum = item;
        
        self.items.append(item);
    
    def pop(self):
        return self.items.pop();
    
    def peek(self):
        return self.items[len(self.items) - 1];
    
    def size(self):
        return len(self.items);
    
    def minStack(self):
        return self.minimum;

class SetOfStacks:
    def __init__(self):
        self.StackPile = [];
        
    
    def isEmpty(self):
        return self.StackPile == [];
    
    def push(self, item):
        lastStack = self.getLastStack();
        if(self.isEmpty()):
            newStack = Stack();
            newStack.push(item);
            self.StackPile.append(newStack);
        elif(len(lastStack.items) == 5):
            newStack = Stack();
            newStack.push(item);
            self.StackPile.append(newStack);
        else:
            lastStack.push(item);
    
    def pop(self):
        if (self.isEmpty()):
            print("The Stack is empty!");
            return;
        
        lastStack = self.getLastStack();
        if (len(lastStack.items) == 1):
            popVal = lastStack.pop();
            self.StackPile.pop();
            return popVal;
        else:
            return lastStack.pop();
    
    def popAT(self, index):
        popStack = self.StackPile[index-1];
        if(popStack.isEmpty()):
            print("The Stack at index value ", index, " is already empty.");
            return;
        elif (len(popStack.items) == 1):
            popVal = popStack.pop();
            for i in range(len(self.StackPile) - index-1):
                #temp = StackPile[index + 1 + i];
                self.StackPile[index - 1 + i] = self.StackPile[index + i];
            self.StackPile.pop();
            return popVal;
        else:
            return popStack.pop();
                
    def getLastStack(self):
        size = len(self.StackPile);
        if(self.isEmpty()):
            print("Empty Stack Pile");
            return;
        else:
            #print(size);
            return self.StackPile[size - 1];
        
class Stacks2Queue:
    def __init__(self):
        self.items = [];
    
    def isEmpty(self):
        return self.items == [];
    
    def push(self, item):
        newStack = Stack();
        while (self.isEmpty() == False):
            #print("First push");
            newStack.push(self.items.pop());
        
        newStack.push(item);
        while(newStack.isEmpty() == False):
            self.items.append(newStack.pop());
    
    def pop(self):
        return self.items.pop();
    
    def peek(self):
        return self.items[0];
        

def sortStack(stack1):
    stack2 = Stack();
    while(stack1.isEmpty() == False):
        if(stack2.isEmpty() == True):
            stack2.push(stack1.pop());
        else:
            temp = stack1.pop();
            #print(temp);
            while(stack2.isEmpty() == False):
                if(stack2.peek() < temp):
                    stack1.push(stack2.pop());
                else:
                    break;
            
            stack2.push(temp);
            #print(stack2.peek());
    
    return stack2;


class Queue:
    def __init__(self):
        self.items = [];
    
    def isEmpty(self):
        return self.items == [];
    
    def enqueue(self, item):
        return self.items.insert(0,item);
    
    def dequeue(self):
        return self.items.pop();
    
    def size(self):
        return len(self.items);
    
    def peek(self):
        return self.items[len(self.items)-1];

def dequeueAny(queue1):
    return queue1.dequeue();

def dequeueCat(queue1):
    tempQueue = Queue();
    tempVal = 0;
    flag =0;
    while(queue1.isEmpty() == False):
        if(queue1.peek().find("cat") == 0 and flag == 0):
            tempVal = queue1.dequeue();
            print("Temp Val: ", tempVal);
            flag = 1;
        else:
            tempQueue.enqueue(queue1.dequeue());
    
    while (tempQueue.isEmpty() == False):
        queue1.enqueue(tempQueue.dequeue());
    
    return tempVal;
    
def dequeueDog(queue1):
    tempQueue = Queue();
    tempVal = 0;
    flag =0;
    while(queue1.isEmpty() == False):
        if(queue1.peek().find("dog") == 0 and flag == 0):
            tempVal = queue1.dequeue();
            flag = 1;
        else:
            tempQueue.enqueue(queue1.dequeue());
    
    while (tempQueue.isEmpty() == False):
        queue1.enqueue(tempQueue.dequeue());
    
    return tempVal;           
#############Question 2
myStack = Stack();

print(myStack.isEmpty());
myStack.push(4);
myStack.push(91);
myStack.push(7.8);
print("My Stack:");
for i in range(len(myStack.items)):
    print(myStack.items[i]);
print(myStack.peek());
print("The Stack Pop Effect: ", myStack.pop());
print(myStack.size());
print("Stack Minimum: ", myStack.minStack());
myQueue = Queue();
myQueue.isEmpty();
myQueue.enqueue(6);
myQueue.enqueue('Animal Farm');
print("My Queue:");
for i in range(len(myQueue.items)):
    print(myQueue.items[i]);

myQueue.dequeue();

print(myQueue.size());
##############Question 3
platePile = SetOfStacks();
print("Is the plate pile empty? ", platePile.isEmpty());
platePile.push(11);
platePile.push(12);
platePile.push(13);
platePile.push(14);
platePile.push(15);
platePile.push(21);
platePile.push(22);
platePile.push(23);
platePile.push(24);
platePile.push(25);
platePile.push(31);
platePile.push(32);
platePile.push(33);
platePile.push(34);
platePile.push(35);
platePile.push(41);
platePile.push(42);
platePile.push(43);
platePile.push(44);
platePile.push(45);
platePile.push(51);
platePile.push(52);
platePile.push(53);
platePile.push(54);
platePile.push(55);
platePile.push(61);
platePile.push(62);
platePile.push(63);
platePile.push(64);
platePile.push(65);
platePile.push(71);
platePile.push(72);
platePile.push(73);

print(platePile.pop());
print(platePile.pop());
print(platePile.popAT(4));

print(platePile.popAT(4));
print(platePile.popAT(4));
print(platePile.popAT(4));
print(platePile.popAT(4));
print(platePile.popAT(4));
############Question 4
stackQueue = Stacks2Queue();
stackQueue.push(1);
stackQueue.push(2);
stackQueue.push(3);
stackQueue.push(4);
stackQueue.push(5);
stackQueue.push(6);
stackQueue.push(7);
print(stackQueue.pop());
print(stackQueue.peek());
#print(len(stackQueue.items));
for i in range(len(stackQueue.items)):
    print(stackQueue.items[i]);

###################Question 5
stack3 = Stack();
stack3.push(1);
stack3.push(8);
stack3.push(3);
stack3.push(11);
stack3.push(17);
print("hi");
stacksorted = sortStack(stack3);
for i in range(len(stacksorted.items)):
    print(stacksorted.items[i]);

#print(stacksorted.pop());
    
###########Question 6
queue6 = Queue();

queue6.enqueue("cat76");
queue6.enqueue("dog43");
queue6.enqueue("dog20");
queue6.enqueue("cat87");
queue6.enqueue("cat98");

queue6.enqueue("cat56");
queue6.enqueue("dog09");
print("Queue peek: ", queue6.peek());
print("dog dequeue: ", dequeueDog(queue6));
for i in range(len(queue6.items)):
    print(queue6.items[i]);
print("any dequeue: ", dequeueAny(queue6));
print("cat dequeue: ", dequeueCat(queue6));

print("Queue6");
for i in range(len(queue6.items)):
    print(queue6.items[i]);
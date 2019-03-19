# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 09:19:38 2019

@author: vicky
"""

class digits:
    def __init__(self, dataval = None):
        self.dataval = dataval;
        self.nextval = None;

class SLinkedList:
    def __init__(self):
        self.headval = None;
    
    def listprint(self):
        printval = self.headval;
        while printval is not None:
            print(printval.dataval);
            printval = printval.nextval;
    
    
    def InsertAtBeginning(self, newdata):
        NewNode = digits(newdata);
        NewNode.nextval = self.headval;
        self.headval = NewNode;
    
    def InsertAtEnd(self, newdata):
        NewNode = digits(newdata);
        if self.headval is None:
            self.headval = NewNode;
            return;
        
        nextNode = self.headval;
        while nextNode.nextval is not None:
            nextNode = nextNode.nextval;
        
        nextNode.nextval = NewNode;
    
    def InsertInBetween(self, middle_node, newdata):
        if middle_node is None:
            print("Middle Node doesn't exist.");
            return;
        
        NewNode = digits(newdata);
        NewNode.nextval = middle_node.nextval;
        middle_node.nextval = NewNode;
        
    def RemoveNode(self, data):
        HeadVal = self.headval;
        
        if HeadVal is None:
            print("List is empty.");
            return;
        
        if(HeadVal.dataval == data):
            self.headval = HeadVal.nextval;
            HeadVal = None;
            return;
        
        while HeadVal.nextval is not None:
            nextNode = HeadVal.nextval;
            if(nextNode.dataval == data):
                HeadVal.nextval = nextNode.nextval;
                nextNode.nextval = None;
                return;
            HeadVal = HeadVal.nextval;
    
    def RemoveDups(self):
        Headval = self.headval;
        #print(Headval.dataval);
        while Headval.nextval is not None:
            #print("In first while");
            head2 = Headval.nextval;
            #print(head2.dataval);
            prev = head2;
            while head2.nextval is not None:
                #print(Headval.dataval);
                #print("In second while");
                if (head2.dataval == Headval.dataval):
                    #print("Entering if");
                    prev.nextval = head2.nextval;
                    head2 = prev.nextval;
                    
                else:
                    #print("Else");
                    prev = head2;
                    head2 = head2.nextval;
            
            Headval = Headval.nextval;
            #print(Headval)
            #print("reached this point");
        return;
            
        
        
list1 = SLinkedList();
list1.headval = digits("Mon");
e2 = digits("Tue");
e3 = digits("Wed");
list1.headval.nextval = e2;
e2.nextval = e3;

#list1.listprint();

list2 = SLinkedList();
list2.headval = digits(19);
d2 = digits(12);
d3 = digits(113);
d4 = digits(9);
d5 = digits(2);
list2.InsertAtEnd(12);
list2.InsertAtBeginning(113);
list2.InsertInBetween(list2.headval, 9);
list2.InsertAtEnd(2);
list2.InsertAtEnd(113);
list2.InsertAtEnd(9);
list2.InsertAtEnd(9);
list2.InsertAtEnd(12);
list2.InsertAtEnd(19);
list2.InsertAtEnd(12);
list2.listprint();
list2.RemoveDups();
print("No Dups");
list2.listprint();
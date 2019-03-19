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
    
def mergesortlist(unsortedlist):
    head = unsortedlist.headval;
    if head is None:
        print("List is empty");
        return;
    elif head.nextval is None:
        return unsortedlist;
    else:
        middle = getMiddle(unsortedlist);
        nextmiddle = middle.nextval;
        middle.nextval = None;
        
        left = mergesortlist(head);
        right = mergesortlist(nextmiddle);
        
        sortedlist = mergelist(left, right);
        return sortedlist;
    
def mergelist(list1, list2):
    if list1 is None:
        return list2;
    if list2 is None:
        return list1;
    if(list1.dataval < list2.dataval):
        temp = list1;
        temp.nextval = mergelist(list1.nextval, list2);
    else:
        temp = list2;
        temp.nextval = mergelist(list1, list2.nextval);
    
    return temp;
    
def getMiddle(list1):
    if list1 is None:
        print("List is empty");
        return;
    elif list1.headval.nextval is None:
        return list1;
    else:
        fastlink = list1.headval
        slowlink = list1.headval;
        while fastlink.nextval is not None:
            fastlink = fastlink.nextval
            if fastlink.nextval is not None:
                slowlink = slowlink.nextval;
                fastlink = fastlink.nextval;
        
        return slowlink;
           
                

        
        
        
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

list3 = mergesortlist(list2);
list3.listprint();
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 19:41:02 2019

@author: vicky
"""

def BucketSort(array1):
    size = len(array1);
    temp = 0;
    for i in range (size):
        if(temp< array1[i]):
            temp = array1[i];
    
    array2 = [];
    for i in range(temp + 1):
        array2.append(0);
    
    for i in range(size):
        temp = array1[i];
        array2[temp] += 1;
    
    array1 = [];
    
    for i in range(len(array2)):
        while(array2[i] != 0):
            array1.append(i);
            array2[i] -= 1;
            
    
    return array1;

def BubbleSort(array1):
    for i in range(len(array1)):
        for j in range(len(array1) - i-1):
            if(array1[j] > array1[j+1]):
                temp = array1[j];
                array1[j] = array1[j+1];
                array1[j+1] = temp;
        
    return array1;

def SelectionSort(array1):
    mintemp = 0;
    minVal = 0;
    for i in range(len(array1)-1):
        minVal = array1[i];
        for j in range(len(array1) - i-1):
            if(minVal > array1[j+i+1]):
                mintemp = j+i+1;
        temp = array1[i];
        array1[i] = array1[mintemp];
        array1[mintemp] = temp;
    return array1;


array1 = [];
array1.append(18);
array1.append(3);
array1.append(11);
array1.append(90);
array1.append(5);
array1.append(3);
array1.append(11);
print("Unsorted Array");
print(array1);
array2 = BucketSort(array1);
print("Bucket Sort");
print(array2);
print("Bubble Sort");
array3 = BubbleSort(array1);
print(array3);
array4 = SelectionSort(array1);
print("Selection Sort");
print(array4);
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 05:19:09 2019

@author: vicky
"""

def uniquestring(str):
    n = len(str);
    switch  = False;
    for i in range(n):
        for j in range(n-i-1):
            if (str[i] == str[i+j+1]):
                switch = True;
                return switch;
    
    return switch;


def mergesort(arraytosort):
    n = len(arraytosort);
    
    arrayleft = arraytosort[:(n//2)];
    arrayright = arraytosort[(n//2):];
    if n > 1:
        mergesort(arrayleft);
        mergesort(arrayright);
    
    i=j=k=0;
    while (i<len(arrayleft) and j<len(arrayright)):
        if(arrayleft[i] < arrayright[j]):
            arraytosort[k] = arrayleft[i];
            i += 1;
        else:
            arraytosort[k] = arrayright[j];
            j +=1;
        
        k += 1;
    
    while(i< len(arrayleft)):
        arraytosort[k] = arrayleft[i];
        i +=1;
        k +=1;
    
    while(j< len(arrayright)):
        arraytosort[k] = arrayright[j];
        j += 1;
        k += 1;
    
    return arraytosort;


def ispermutation(word1, word2):
    sorted1 = ''.join(sorted(word1));
    sorted2 = ''.join(sorted(word2));
    if(sorted1 == sorted2):
        print(word1+" is a permutation of "+word2);
    else:
        print(word1+" is not a permutation of "+word2);
    
    return;

def URLify(string):
    stringModified = [];
    for i in range(len(string)):
        if(string[i] == " "):
            stringModified.append("%20");
        else:
            stringModified.append(string[i]);
    
    switch = True;      
    while(switch):
        if(stringModified[len(stringModified) - 1] == "%20"):
            del stringModified[-1];
            
        else:
            switch = False;
    
    newString = ''.join(stringModified);
    return newString;


def PalindromePermutation(string):
    sortedString = sorted(string);
    #print(''.join(sortedString));
    index = 0;
    i = 0;
    switch = True;
    while(True):
        if(sortedString[0] == " "):
            del sortedString[0];
        else:
            break;
    
    
    #print(''.join(sortedString));
    while(i < (len(sortedString) - 1) and switch):
        if(sortedString[i] == sortedString[i+1]):
            i += 2;
        else:
            index += 1;
            i += 1;
        if(index > 1):
            switch = False;
    
    return switch;

def OneAway(word1, word2):
    index = 0;
    a = len(word1);
    b = len(word2);
    if(a==b):
        for i in range(a):
            if(word1[i] != word2[i]):
                index += 1;
                if(index > 1):
                    return False;
        
        return True;
    elif(a == (b-1)):
        i= j = 0;
        while(i< (b-1)):
            if(word1[j] != word2[i]):
                if(word1[j] != word2[i+1]):
                    return False;                
                i +=1;
                index += 1;
                if (index > 1):
                    return False;
            
            i += 1;
            j += 1;
        return True;
    elif((a - 1) == b):
        i= j = 0;
        while(i< (a-1)):
            if(word1[i] != word2[j]):
                if(word1[i+1] != word2[j]):
                    return False;
                i +=1;
                index += 1;
                if (index > 1):
                    return False;
            
            i += 1;
            j += 1;
        return True;
    else:
        return False;

def StringCompression(string):
    n = len(string);
    i =0;
    stringCom = [];
    while(i < n):
        char = string[i];
        temp = 0;
        while(i < n and string[i] == char):
            temp +=1;
            i += 1;
        stringCom.append(char+str(temp));
        temp = 0;
    
    if(len(stringCom) == n):
        return string;
    else:
        return ''.join(stringCom);

def RotateMatrix(matrix):
    a = len(matrix);
    for i in range(a):
        for j in range(i):
            print(matrix[i][j]);
            temp = matrix[i][j];
            matrix[i][j] = matrix[j][i];
            matrix[j][i] = temp;
            print(matrix[i][j]);
    
    return matrix;

def zeroMatrix(matrix):
    a = len(matrix);
    b = len(matrix[0]);
    index = [];
    for i in range(a):
        for j in range(b):
            if(matrix[i][j] == 0):
                index.append([i, j]);
        
    print(index);
    for i in range(len(index)):
        temprow = index[i][0];
        tempcolumn = index[i][1];
        for k in range(b):
            matrix[temprow][k] = 0;
        for k in range(a):
            matrix[k][tempcolumn] = 0;
    print("break");    
    return matrix;


def stringRotation(string1, string2):
    a = len(string1);
    b = len(string2);
    if (a == b):
        for i in range(a):
            string1 = string1[a-1]+string1[:(a-1)];
            print(string1);
            if(string1 == string2):
                return True;
    else:
        return False;
    return False;


print(stringRotation("waterloo", "aterloow"))

mat = [[1, 2, 0, 4], [5, 6, 7, 8], [9, 0, 11, 12], [13, 14, 15, 16]];
print(zeroMatrix(mat));

print(StringCompression("mississippi"));

print(OneAway("place", "plda"));
        
    
        
if(PalindromePermutation("taco  cat")):
    print("True");
else:
    print("False");


print(URLify("This is my name.   "));




ispermutation("apple", "leopa");

array = [43, 65, 12, 9, 54, 11, 9, 2, 3];
print(mergesort(array));    


print(uniquestring("abcd"));
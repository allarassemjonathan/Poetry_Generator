from collections import defaultdict
import random
import numpy as np

def dicoGen():
    f = open(r'C:\Users\ALLARASSEMJJ20\Achilles\poem.txt', encoding = 'utf-8')
    text = f.read()
    forb = '''±¬¤¸£×¥¿*¶¼¦¹¯§¾´ª½¢¡®…³=²º¨0123456789!→°‘()[]{};:'“”"«»\,+<>/?@#$%^&*_~©'''
    for l in text:
        if l in forb:
            text = text.replace(l, ' ')

    arr = text.split()
    arr.reverse()
    p = '.-!?'
    for i in range(len(arr)-1):
        if arr[i][len(arr[i])-1] in p and len(arr[i])-1>0:
            arr.insert(i+1, arr[i][len(arr[i])-1])
            arr[i] = arr[i][0:len(arr[i])-1]
            
    dico = defaultdict(list)
    for a,b in zip(arr[0:-1],arr[1:]):
        dico[a].append(b)
    return dico

def tokenize():
    f = open(r'C:\Users\ALLARASSEMJJ20\Achilles\poem.txt', encoding = 'utf-8')
    text = f.read()
    arr = text.split()
    arr.reverse()
    p = ',.!;'
    c = 0
    var = len(arr)
    while(True):
        for i in range(len(arr)):
            if arr[i][len(arr[i])-1] in p and len(arr[i])-1>0:
                arr.insert(i+1, arr[i][len(arr[i])-1])
                arr[i] = arr[i][0:len(arr[i])-1]
                c = c + 1
        if(var >= len(arr)-1):
            break
        var = var + c
    return arr

def matrix(arr):
    i = 0
    j = 0
    M = [[0]*len(arr) for _ in range(len(arr))]
    for l in arr:
        for k in arr[1:]:
            if (l,k) in zip(arr,arr[1:]):
                M[i][j]+=1
            if j < len(arr)-1:
                j+=1
        if i < len(arr)-1:
            i+=1
    return M

def rhymes(arr):
    p = ',.!;'
    array = []
    #print(arr)
    #print(len(arr))
    for i in range(len(arr) - 1):
        if arr[i+1] in p:
            array.append(arr[i])
            #print(arr[i])
    return array

def normalization(state):
    for i in range(len(state)):
        state[i] = state[i]/sum(state)
    return state

def next_State(initial_State, matrix):
    state = initial_State
    state = np.matmul(matrix, state)
    state = normalization(state)
    return state

def proba_to_words(state):
    sum = 0
    index = 0
    p = np.random.rand()
    for i in range(len(state)):
        sum = sum + state[i]
        if p > 1 - sum:
            index = i
            break
    return tokenize()[index]

ini =[1/15*1 for _ in range(15)]
sentence = ''
for i in range(10):
    sentence = sentence + ' ' + proba_to_words(next_State(ini,matrix(tokenize())))
print(sentence)

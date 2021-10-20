from collections import defaultdict
import random

def markov_chain_first_order():
    f = open(r'C:\Users\ALLARASSEMJJ20\Achilles\Holmes.txt', encoding = 'utf-8')
    text = f.read()
    forb = '''±¬¤¸£×¥¿*¶¼¦¹¯§¾´ª½¢¡®…³=²º¨0123456789!→°‘()[]{};:'“”"«»\,+<>/?@#$%^&*_~©'''
    for l in text:
        if l in forb:
            text = text.replace(l, ' ')
            
    arr = text.split()
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
    print('tokenizing...')
    f = open(r'C:\Users\ALLARASSEMJJ20\Achilles\poem.txt', encoding = 'utf-8')
    text = f.read()
    arr = text.split()
    p = ':,.!;“”'
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

def tokenize_inverse():
    print('tokenizing...')
    f = open(r'C:\Users\ALLARASSEMJJ20\Achilles\Shakespear.txt', encoding = 'utf-8')
    text = f.read()
    arr = text.split()
    arr = arr[::-1]
    p = ':,.!;“”'
    c = 0
    var = len(arr)
    while(True):
        for i in range(len(arr)):
            if arr[i][len(arr[i])-1] in p and len(arr[i])-1>0:
                arr.insert(i-1, arr[i][len(arr[i])-1])
                arr[i] = arr[i][0:len(arr[i])-1]
                c = c + 1
        if(var >= len(arr)-1):
            break
        var = var + c
    return arr

def clean_text():
    f = open(r'C:\Users\ALLARASSEMJJ20\Achilles\poem.txt', encoding = 'utf-8')
    text = f.read()
    forb = '''±¬¤¸£×¥¿*¶¼¦¹¯§¾´ª½¢¡®…³=²º¨0123456789!→°‘()[]{};:'“”"«»\,+<>/?@#$%^&*_~©'''
    for l in text:
        if l in forb:
            text = text.replace(l, ' ')   
    arr = text.split()
    print(arr)
    p = '.-!?'
    for i in range(len(arr)-1):
        if arr[i][len(arr[i])-1] in p and len(arr[i])-1>0:
            arr.insert(i+1, arr[i][len(arr[i])-1])
            arr[i] = arr[i][0:len(arr[i])-1]
    return arr
        
def markov_chain_second_order(arr):
    dico = defaultdict(list)
    for a,b,c in zip(arr[0:-1],arr[1:], arr[2:]):
        tu = (a,b)
        dico[tu].append(c)
    return dico

def markov_chain_second_order(arr):
    arr = reversed(arr)
    dico = defaultdict(list)
    for a,b,c in zip(arr[0:-1],arr[1:], arr[2:]):
        tu = (a,b)
        dico[tu].append(c)
    return dico
    
def markov_chain_third_order(arr):
    dico = defaultdict(list)
    for a,b,c,d in zip(arr[0:-1],arr[1:], arr[2:], arr[3:]):
        tu = (a,b,c)
        dico[tu].append(d)
    return dico

def textGenerator_third_order (third_order, array):
    r = random.randint(0, len(array) -1)
    while array[r] != array[r].capitalize():
        r = random.randint(0, len(array) -1)
    key = (array[r], array[r+1], array[r+2])
    text = key[0] + ' ' + key[1] + ' ' + key[2]
    next_state = ''
    while next_state != '.':
        index = random.randint(0, len(third_order[key]) - 1)
        next_state = str(third_order[key][index])
        if next_state == '.':
            text = text + next_state
        else:
            text = text + ' ' + next_state
        key = (key[1], key[2], next_state)
    return text
        

def rhymes(arr, isInversed):
    p = ':,.!;'
    array = []
    for i in range(len(arr) - 1):
        if arr[i+1] in p:
            array.append(arr[i])
    print(array)
    return array

def textGenerator_second_order(second_order, array):
    r = random.randint(0, len(array) -1)
    key = (array[r], array[r+1])
    text = key[0] + ' ' + key[1]
    for i in range(150):
        index = random.randint(0, len(second_order[key]) - 1)
        next_state = str(second_order[key][index])
        text = text + ' ' + next_state
        key = (key[1], next_state)
    return text

def textGenerator_first_order(first_order, array):
    r = random.randint(0, len(array) - 1)
    key = array[r]
    text = key + ' '
    for i in range(150):
        index = random.randint(0, len(first_order[key]) - 1)
        next_state = str(first_order[key][index])
        text = text + ' ' + next_state
        key = next_state
    return text

def poetry_Generator(rhymes):
    r = random.randint(0, len(rhymes) - 1)
    first_key = rhymes[r]
    
    if r%2 == 0 and r !=0:
        second_key = rhymes[r+1]
    else:
        second_key = rhymes[r-1]
    rhymes.remove(first_key)
    rhymes.remove(second_key)
    
    print(first_key + ' ' + second_key)
        
    
def textGenerator_first_order():
    s = ''
    array = []
    dic = markov_chain_first_order()
    arr = list(dic.keys())
    start = []
    
    for e in arr:
        if e == e.capitalize():
            start.append(e)
    word = ''
    while word != '.':
        if len(array) == 0:
                word = random.choice(start)
                s += word + ' '
                array.append(word)
        else:
                word = random.choice(dic[array[len(array)-1]])
                s += word + ' '
                array.append(word)
    return s
print(textGenerator_third_order(markov_chain_third_order(clean_text()), clean_text()))
#print(textGenerator_second_order(markov_chain_second_order(clean_text()), clean_text()))
#print(poetry_Generator(rhymes(tokenize(False))))
#print(tokenize_inverse())


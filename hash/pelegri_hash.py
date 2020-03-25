#!/usr/bin/env python
# coding: utf-8

# # TP Julien Pelegri hash

# ## Link of my github to acces code source : 
# 
# Click on the link below and then go into the 'hash' folder :
# 
# https://github.com/glaiveVII/bigdata
# 
# How to compile it : 
# - use google colloab to compile the Jupiter Notebook 
# - or on your localhost with anaconda 
# - compile the pelegri_hash.py and see, it works for my compile

# ## Some Hash test

# In[98]:


# hash for integer unchanged
print('Hash for 181 is:', hash(181))

# hash for decimal
print('Hash for 181.23 is:',hash(181.23))

# hash for string
print('Hash for Python is:', hash('Python'))


# ## Read the file first 

# ### I have create a smaller .txt file with only a to go faster when testing since the file is long

# In[123]:


import hashlib

inputFile = input("Enter the name of the file:")

f=open(inputFile, "r")


# In[124]:


print(f)


# ## Now read the file line per line :

# In[125]:


words =[] #Liste pour stocker les différentes lignes
# Use str.rstrip() to remove a trailing newline 
for line in f:
    words.append(line.rstrip("\n"))
print(words)


# In[126]:


print(type(words[3]))


# ## Now going through words array and hash it 

# In[127]:


import hashlib

print(hashlib.algorithms_available)


# ### Basic python hash : use the hash function

# In[128]:


hashed = []
for i in words:
    hashed.append(hash(i))
    
print(hashed)


# ### Basic counting collision, just to have an idea

# In[129]:


counter = 0
for i in hashed:
    counter +=  hashed.count(i)
    
# since all elements are already in the array
print(counter - len(words))


# ## Another way to count 
# 

# In[ ]:





# ### Building a basic hash : coding each letter by its in the alphabet 

# In[130]:


from string import ascii_lowercase


LETTERS = {letter: str(index) for index, letter in enumerate(ascii_lowercase, start=1)} 

def alphabet_position(text):
    text = text.lower()

    numbers = [LETTERS[character] for character in text if character in LETTERS]

    return ' '.join(numbers)


# In[131]:


print(words[50])
alphabet_position(words[50])


# In[132]:


encoded = []

for i in words:
    encoded.append(alphabet_position(i))
print(encoded)


# In[133]:


counter = 0
for i in encoded:
    counter +=  encoded.count(i)
    
# since all elements are already in the array
print(counter - len(words))


# ### Function to decode for a given number

# In[134]:


def alphabet_encode(number, alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
    """Converts an integer to an alphabet equivilent"""
    if not isinstance(number, (int, long)):
        raise TypeError("number must be an integer")

    if 0 <= number - 1 < len(alphabet):
        return alphabet[number - 1]

    base = ''
    while number != 0:
        number, r = divmod(number, len(alphabet))
        if r == 0:
            number = number - 1
        base = alphabet[r - 1] + base
    return base


# ## A more complex way to hash 

# In[135]:


import sys
import hashlib

hashed = []
for i in words:
    hashed.append(hashlib.sha256(i.encode('utf-8')).hexdigest())
    
print(hashed)


# In[136]:


hashed[2]


# In[137]:


counter = 0
for i in hashed:
    counter +=  hashed.count(i)
    
# since all elements are already in the array
print(counter - len(words))


# ### Fonction hashage Lemasquerier 

# In[138]:


# Fonction de hachage simple
def lemasquerier_bon_hashage(my_str, size):
    current=size
    n=len(my_str)
    toggle = True
    for x in range(len(my_str)):
        if toggle:
            current+=ord(my_str[x])
        else:
            current*=ord(my_str[x])
        toggle = not toggle
    current = (current+n)%size
    return current


# ### Adapting my code to Lemasquerier hash function to pass my array

# In[143]:


n = len(words)
hash_max = []
for i in range(n):
    hash_max.append(lemasquerier_bon_hashage(words[i], n))

print(hash_max)


# ### Counting its collision

# In[144]:


counter = 0
for i in hash_max:
    counter +=  hash_max.count(i)
    
# since all elements are already in the array
print(counter - len(words))


# ## end of Jupiter Notebook

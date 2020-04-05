#!/usr/bin/env python
# coding: utf-8

# # TP Julien Pelegri hash

# Pour plus de clareté et mieux comprendre mon travail je vous invite à consulter mon Jupiter
# Notebook au lien suivant : https://github.com/glaiveVII/bigdata
# Aller dans le file 'hash' et cliquer sur le jupiter : il deja loader avec mes resultats

# ## Goal : play around with hash funcitons, build some and encode some .txt file. Try to optimize time and space complexity and have as few collision as possible.

# ## Plan :
# - 1/ Play around
# - 2/ Test of a not build in hash function
# - Conclusion

# ------------------------------

# <img src="hash.png",width=400,height=400>
#

# # 1/ Play around

# In[1]:


import six
#print("The max size of words I can get : " , six.MAXSIZE)


# ## Some Hash test

# In[2]:


# hash for integer unchanged
#print('Hash for 181 is:', hash(181))

# hash for decimal
#print('Hash for 181.23 is:',hash(181.23))

# hash for string
#print('Hash for Python is:', hash('Python'))


# ### Evaluation of the .txt file size with the wc command line

# ### J'ai cree un word.txt file that has only 500 words to test faster
#
# wc word.txt
#
# >> 500
#
# wc word2.txt
#
# >> 235886
#
# wc texte_Shakespeare.txt
#
# >> 22906
#

# ## Read the file first

# ### I have create a smaller .txt file with only a to go faster when testing since the file is long

# In[34]:


import hashlib

inputFile = input("Enter the name of a small .txt file (like my word.txt, only 500 words) to test basic hashing function : ")

f=open(inputFile, "r")


# In[35]:


#print(f)
txt = f


# ## Now read the file line per line :

# In[36]:


def count(file):
    words =[] #Liste pour stocker les différentes lignes
    # Use str.rstrip() to remove a trailing newline
    countword = 0

    for line in f:
        countword += 1
       # print(len(words))
        words.append(line.rstrip("\n"))
    save = words
    return(countword, save)


# In[37]:


x = count(f)
words = x[1]


# In[38]:


#print(x[0])


# In[39]:


#print(len(words))


# In[42]:


#print(words[235500:235600])


# In[43]:


#print(type(x[1][3]))


# ## Now going through words array and hash it

# In[44]:


import hashlib

#print(hashlib.algorithms_available)


# ### Basic python hash : use the hash function

# In[45]:


hashed = []
for i in words:
    hashed.append(hash(i))

#print(hashed[0:100])


# ### Basic counting collision, just to have an idea

# In[46]:


counter = 0
for i in hashed:
    counter +=  hashed.count(i)

# since all elements are already in the array
print("nombre colision pour le premeir hash", counter - len(words))
print("\n")

# Cette methode est bien evidement pas la plus optimale mais tres pratique, pour word2.txt, cela prends quelques minutes sur google colab (j'ai changé l'allocation GPU pour aller plus vite)

# ### Of crouse this hash function is efficient it is a build-in one

# ### Building a basic hash : coding each letter by its in the alphabet

# In[47]:


from string import ascii_lowercase


LETTERS = {letter: str(index) for index, letter in enumerate(ascii_lowercase, start=1)}

def alphabet_position(text):
    text = text.lower()

    numbers = [LETTERS[character] for character in text if character in LETTERS]

    return ' '.join(numbers)


# In[48]:


#print(words[50])
#alphabet_position(words[50])


# In[49]:


encoded = []

for i in words:
    encoded.append(alphabet_position(i))
#print(encoded[0:100])


# In[50]:


counter = 0
#print(len(encoded))
for i in encoded:
    counter +=  encoded.count(i)

# since all elements are already in the array
#print(counter - len(words))


# ### This hash function that is at first sight a bit naive is efficient due to the fact that I write each letter on a float that I concatenate in a big string

# ### Function to decode for a given number

# In[ ]:


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


# ### cette fonction de hashage est bien plus longue est pas forcement per'tinente, elle met bcp de temps pour word2.txt, pour la tester utiliser un .txt file plus petit

# ## A more complex way to hash

# In[ ]:


import sys
import hashlib

hashed = []
for i in words:
    hashed.append(hashlib.sha256(i.encode('utf-8')).hexdigest())

#print(hashed[0:10])


# In[ ]:


hashed[2]


# In[ ]:


counter = 0
for i in hashed:
    counter +=  hashed.count(i)

# since all elements are already in the array
#print(counter - len(words))


# 68447 collisions sur 235886 mots

# ## We want to avoid colisions : it happens when two different words receive the same hashes

# <img src="colisions.png",width=400,height=400>
#

# In this diagram, you can see the key (a string) is run through a hash function which produces an integer 0-15 which is used as the index in a 16-element array.

# ### Here it is the case for John Smith and Sandra Dee, they have the hash 01. Once we want to encode it they will receive the same key. We want to avoid this phenomenon as much as possible

# ### Now that we have experienced hashing in Python lets get more in depth by building ou hashing function

# -----------------------------------------------------------

# ## 2/ Test on a not build in hash function

# ## Whole process of hashing to a file :

# ### We have to re-read the file

# En effet pour des problemes de memoire variable il vaut mieux tout faire d'un coup

# ### hashage polynomial et le plus simple et pertinent à mettre en place :
#

# In[162]:


def wordcount(file):
    with open( file , "r") as f:
        counter = 0
        for word in f:
            counter += 1
    return(counter)

def hash_fct(file):
    x = wordcount(file)
    table = [0 for i in range(3*x)]
    with open( file , "r") as f:
        y = 0
        for word in f:
            h = (hachage1(word,3*x) + 3 * hachage2(word,3*x) + 2 * hachage3(word,3*x))%(3*x)
            if table[h] != 0:
                y = y+1
            table[h] = word
        print("\n")
        print("We have found", y, "on", x, "words in this file!")
        print("\n")
        return(0)

def hachage1(word,n):
    i = 1
    h = 0
    l = len(word)
    for car in word:
        h = h+(26**(l-i))*(ord(car) - 96)
        i += 1
    return (h%n)

def dec2bin(x):
    return int(bin(x)[2:])

def leftRotate(n, g):
    INT_BITS = len(str(dec2bin(n)))
    return (n << g)|(n >> (INT_BITS - g))

def hachage2(word,n):
    i = 1
    h = 0
    l = len(word)
    for car in word:
        h = h+(26**(l-i))*(ord(car) - 96)
        i += 1
        h = h >> 1
        h = h << 0
    return (h%n)

def hachage3(word,n):
    i = 1
    h = 0
    l = len(word)
    for car in word:
        h = h+(26**(l-i))*(ord(car) - 96)
        i += 1
        h = leftRotate(h,5)
    return (h%n)


# In[163]:


def pelegri_word2():
    print("Julien Pelegri hashing function for word2.txt")
    hash_fct("word2.txt")
    print("Fin hashage et comptage collisions")


# In[164]:


def pelegri_word():
    print("Julien Pelegri hashing function for word.txt")
    hash_fct("word.txt")
    print("Fin hashage et comptage collisions")


# In[165]:


def pelegri_shakespeare():
    print("Julien Pelegri hashing function for texte_Shakespeare.txt")
    hash_fct("texte_Shakespeare.txt")
    print("Fin hashage et comptage collisions")


# In[166]:
print("\n")

def pelegri_corn():
    print("Julien Pelegri hashing function for corncob_lowercase.txt")
    hash_fct("corncob_lowercase.txt")
    print("Fin hashage et comptage collisions")


# ## To run the block above run the function pelegri_AAAA()

# In[167]:


pelegri_word()


# In[168]:


pelegri_word2()


# In[169]:


pelegri_shakespeare()


# In[170]:


pelegri_corn()


# ### On fait des rotations à gauche pour reduire le nombre colisions (astuce toruvée sur stackoverflow), on peut faire aussi a droite mais ca reduit que de peu les collisions pour un temps de calcul bcp plus important

# ## Conclusion

# ### On est sur plus de 10% de hashage mal classifié, les resultats ne sont pes tres bons, on se rend compte que des qu'on utilise pas une librairie python c'est difficile de faire quelque chose de pertinent si on veut garder un temps et un espace pertinent. C'etait neanmoins le but de l'exerice de ne pas utiliser des fonctions de python et de rester performant en temps et espace.

# ---------------------------------------------------------------

# ### Fonction hashage de Monsieur Lemasquerier

# I will test it on the word.txt file

# In[175]:
inputFile2 = input("Enter the name of a .txt file to test Lemasquerier hash function : ")

m=open(inputFile2, "r")

#print(m)

def count_max(file):
    words =[] #Liste pour stocker les différentes lignes
    # Use str.rstrip() to remove a trailing newline
    countword = 0

    for line in m:
        countword += 1
       # print(len(words))
        words.append(line.rstrip("\n"))
    save = words
    return(countword, save)


z = count_max(m)
#print(z)
words_max = z[1]
#print(len(words_max))


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


# ### Adapting my code to Lemasquerier hash function to pass my string

# In[176]:


n = len(words_max)
hash_max = []
for i in range(n):
    hash_max.append(lemasquerier_bon_hashage(words_max[i], n))

#print(hash_max)


# In[177]:


counter = 0
for i in hash_max:
    counter +=  hash_max.count(i)

# since all elements are already in the array
print("The number of colisions in Lemasquerier hash function is :", counter - len(words_max))


# ## end of Jupiter Notebook

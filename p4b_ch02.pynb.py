#!/usr/bin/env python
# coding: utf-8

# In[1]:


#print ("Hello World")
print ("Hello World")


# In[3]:


# print 'Hello World'
print ('Hello World')


# In[4]:


# using quotes
print ("She said 'Hello World'")


# In[5]:


print ('He said "Hello World"')


# In[6]:


#This is a comment, it will be ignored by the computer


# In[7]:


print ('Comments are very useful!')


# In[8]:


# print a friendly greeting
print ('Hello World')


# In[9]:


print(Hello World)


# In[10]:


prin("hello world")


# In[11]:


print("Hello
      World") 
      


# In[12]:


print("Hello\nWorld")


# In[13]:


print("Hello\tWorld")


# In[14]:


print('Hello\rWorld')


# In[15]:


#store a short DNA sequence in the varialbe my_dna
my_dna = "ATGCGTA"


# In[16]:


#now print the DNA sequence
print(my_dna)


# In[17]:


#change value of my_dna
my_dna = "TGGTCCA"


# In[18]:


print(my_dna)


# In[19]:


#store a short DNa sequence for banana
banana_dna = "ATCGGTA"


# In[20]:


print(banana_dna)


# In[21]:


my_dna = "AAT" + "GGCC"


# In[22]:


print(my_dna)


# In[23]:


upstream = "AAA"


# In[24]:


my_dna = upstream + "ATGC"


# In[25]:


print(my_dna)


# In[26]:


downstream = "GGG"


# In[27]:


my_dna = upstream + downstream


# In[28]:


print(my_dna)


# In[29]:


print("Hello" + "" "World")


# In[30]:


#this line doesn't produce any output
len("ATGC")


# In[31]:


dna_length = len("ATGC")


# In[32]:


print(dna_length)


# In[33]:


#in len the return value is a number, NOT a string! Pyhton treats numbers and strings differently 


# In[34]:


#store the dna seqeunce in a varialbe
my_dna = "ATGCGAGT"
#calculate the length of the sequence and store it in a variable
dna_length = len(my_dna)
#print a message telling us the DNA sequence length
print("The length of the DNA sequence is " + dna_length)my_dna = "ATGCGAGT"
#calculate the length of the sequence and store it in a variable
dna_length = len(my_dna)
#print a message telling us the DNA sequence lenth
print("The length of the DNA sequence is " + dna_length)


# In[35]:


my_dna = "ATGCGAGT"
dna_length = len(my_dna)
print("The length of the DNA sequence is " + str(dna_length))


# In[36]:


my_dna = "ATGC"
# print my_dna in lower case
print(my_dna.lower())


# In[37]:


print("ATGC")
len(my_dna)


# In[38]:


my_dna = "ATGC"
# print the variable
print("before: " + my_dna)


# In[39]:


# run the lower method and store the result
lowercase_dna = my_dna.lower()
# print the variable again
print("after: " + my_dna)


# In[40]:


my_number = len("AGTC")
# my_number is 4
print(my_number.lower())


# In[41]:


my_number = len("atgc")
# my_number is 4
print(my_number.upper())


# In[42]:


my_dna = "ATGC"
# print my_dna in upper case
print(my_dna.upper())


# In[43]:


protein = "vlspadktnv"
# replace valine with tyrosine
print(protein.replace("v", "y"))


# In[44]:


# we can replace more than one character
print(protein.replace("vls", "ymt"))


# In[45]:


# the original variable is not affected
print(protein)


# In[46]:


protein = "vlspadktnv"
# print positions three to five
print(protein[3:5])

# positions start at zero, not one
print(protein[0:6])

# if we use a stop position beyond the end, it's the same as using the end
print(protein[0:60])


# In[47]:


protein = "vlspadktnv"
first_residue = protein[0]


# In[48]:


print(first_residue)


# In[49]:


protein = "vlspadktnv"
# count amino acid residues
valine_count = protein.count('v')
lsp_count = protein.count('lsp')
tryptophan_count = protein.count('w')


# In[50]:


# now print the counts
print("valines: " + str(valine_count))
print("lsp: " + str(lsp_count))
print("tryptophans: " + str(tryptophan_count))


# In[51]:


protein = "vlspadktnv"
print(str(protein.find('p')))
print(str(protein.find('kt')))
print(str(protein.find('w')))


# In[52]:


my_dna.count(my_motif)


# In[53]:


my_motif.count(my_dna)


# In[ ]:





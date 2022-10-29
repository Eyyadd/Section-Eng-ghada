#!/usr/bin/env python
# coding: utf-8

# In[1]:


with open('bookstore.xml') as file:
    for l in file:
        print(l.strip())


# In[2]:


import xml.etree.ElementTree as ET
tree = ET.parse('bookstore.xml')
root = tree.getroot()
print(root.tag)


# In[3]:


for child in root:
    print(child.tag, child.attrib)


# In[4]:


print(root[0][1].text)


# In[5]:


for title in root.iter('title'):
    print(title.attrib)


# In[6]:


file=open("test.txt","w")
file.write("Now the file has more content!")
file.close()


# In[7]:


f = open("test.txt", "r")


# In[8]:


print(f.read())


# In[9]:


file = open("sample.bin", "wb")


# In[10]:


file.write(b"This binary string will be written to sample.bin")


# In[11]:


file.close()


# In[12]:


file = open("sample.bin", "rb")


# In[13]:


print(file.read(3))


# In[14]:


file.close()


# In[15]:


file=open("array.bin","wb")


# In[16]:


num=[2,4,6,8,10]


# In[17]:


array=bytearray(num)


# In[18]:


file.write(array)


# In[19]:


file.close()


# In[20]:


f=open("array.bin","rb")
num=list(f.read())
print(num)
f.close()


# In[ ]:





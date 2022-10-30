#!/usr/bin/env python
# coding: utf-8

# In[1]:


from pyopenms import*


# In[2]:


seq=AASequence.fromString("VAKA")


# In[3]:


seq_wz_MonoWeight=seq.getMonoWeight()


# In[4]:


seq_monoweight_2=seq.getMonoWeight(Residue.ResidueType.Full,2)


# In[5]:


mz=seq.getMZ(2)


# In[12]:


print(f"The Peptide {seq} and The Peptide With MonoWeight (mass Without Water) ==> {seq_wz_MonoWeight}")
print(f"The Peptide With MonoWeight and 2H ==> {seq_monoweight_2} and The MZ ==> {mz}")


# In[10]:


print(f"The Peptide {seq} Are Consist of the following Amino-Acid :")
resultOfAllMonoWeight=0
for aa in seq:
    print(aa.getName()+" ===> "+str(aa.getMonoWeight()))
    resultOfAllMonoWeight+=aa.getMonoWeight()


# In[11]:


print(f"The Sum of All Amino Acid VAKA {resultOfAllMonoWeight}")


# In[13]:


print(f"Is The VAKA == V + A + K + A ? {bool(seq_monoweight_2==resultOfAllMonoWeight)}")


# In[ ]:





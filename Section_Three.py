#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pyopenms


# In[2]:


from pyopenms import*


# In[4]:


seq=AASequence.fromString("DFPIANGER")


# In[5]:


prefix=seq.getPrefix(5)


# In[6]:


sufix=seq.getSuffix(5)


# In[7]:


concatnate=seq+seq


# In[9]:


print(f"The Sequence is {seq}\n The Prefix is {prefix}\n The Suffix is {sufix}\n The Concatnate is {concatnate}")


# In[10]:


mfull=seq.getMonoWeight()


# In[13]:


pre=seq.getMonoWeight(Residue.ResidueType.Full,2)


# In[12]:


print(f"The Monoisotopic mass of peptide [M] is {mfull}")


# In[15]:


print(f"Monoisotopic mass of peptide precursor [M+2H]2+ is {pre}")


# In[16]:


mz=seq.getMZ(2)


# In[17]:


print(f"Monoisotopic m/z of [M+2H]2+ is {mz}")


# In[19]:


print(f"The Peptide {seq} Consist of the following Amino-Acid")
for aa in seq:
    print(aa.getName()+"==>"+str(aa.getMonoWeight()))


# In[20]:


seq_mol=seq.getFormula()


# In[21]:


print(f"The peptide {seq} has the Molecular Formula ==> {seq_mol}")


# In[22]:


sufix=seq.getSuffix(3)


# In[23]:


print(f"Y3 ion sequence {sufix}")


# In[24]:


y3_formula=sufix.getFormula(Residue.ResidueType.YIon,2)


# In[25]:


sufix.getMonoWeight(Residue.ResidueType.YIon,2)


# In[26]:


sufix.getMonoWeight(Residue.ResidueType.XIon,2)


# In[27]:


print(f"Y3 MZ {sufix.getMonoWeight(Residue.ResidueType.YIon,2)}")


# In[28]:


print("y3 molecular formula:", y3_formula)


# In[29]:


seq_2 = AASequence.fromString("PEPTIDESEKUEM(Oxidation)CER")


# In[31]:


print(seq_2.toUnmodifiedString())


# In[32]:


print(seq_2.toString())


# In[33]:


print(seq_2.toUniModString())


# In[34]:


print(seq_2.toBracketString())


# In[35]:


print(seq_2.toBracketString(False))


# In[36]:


print(AASequence.fromString("DFPIAM(UniMod:35)GER"))

print(AASequence.fromString("DFPIAM[+16]GER"))

print(AASequence.fromString("DFPIAM[+15.99]GER"))

print(AASequence.fromString("DFPIAM[147]GER"))

print(AASequence.fromString("DFPIAM[147.035405]GER"))


# In[38]:


fil = FASTAEntry()


# In[39]:


fil.sequence = "MKWVTFISLLLLFSSAYSRGVFRRDTHKSEIAHRFKDLGE"


# In[40]:


fil.description = "BSA Bovine Albumin (partial sequence)"


# In[41]:


fil.identifier = "BSA"


# In[43]:


fil_2 = FASTAEntry()


# In[44]:


fil_2.sequence = "MKWVTFISLLFLFSSAYSRGVFRRDAHKSEVAHRFKDLGE"

fil_2.description = "ALB Human Albumin (partial sequence)"

fil_2.identifier = "ALB"


# In[45]:


entries = [fil, fil_2]


# In[46]:


f = FASTAFile()


# In[47]:


f.store("example.fasta", entries)


# In[50]:


entries = []

f = FASTAFile()


# In[ ]:





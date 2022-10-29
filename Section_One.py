#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install pyopenms')


# In[5]:


import pyopenms


# In[6]:


print(f"The Avogadro Number Equal > {pyopenms.Constants.AVOGADRO}")


# In[7]:


from pyopenms import *


# In[8]:


element=ElementDB()
element.hasElement("O")


# In[10]:


oxygen=element.getElement("O")


# In[11]:


oxygen.getName()


# In[12]:


oxygen.getSymbol()


# In[13]:


oxygen.getMonoWeight()


# In[14]:


oxygen.getAverageWeight()


# In[15]:


print(f"One Mole of Oxgen weights => {2*oxygen.getAverageWeight()} grams.")


# In[16]:


sulfur=element.getElement("S")


# In[17]:


print(sulfur.getName())


# In[18]:


print(sulfur.getSymbol())


# In[19]:


print(sulfur.getMonoWeight())


# In[20]:


print(sulfur.getAverageWeight())


# In[21]:


oxy_isoDist={"mass":[],"abundance":[]}
oxy=element.getElement("O")


# In[22]:


isotopes=oxy.getIsotopeDistribution()


# In[25]:


for i in isotopes.getContainer():
    print(f"oxygen isotope {i.getMZ()} has abundance {i.getIntensity()*100} %.")
    oxy_isoDist["mass"].append(i.getMZ())
    oxy_isoDist["abundance"].append((i.getIntensity()*100))


# In[28]:


sulfur=element.getElement("S")
isotopes=sulfur.getIsotopeDistribution()
sulfur_isoDist={"mass":[],"abundance":[]}


# In[32]:


for i in isotopes.getContainer():
    print(f"Sulfur isotope {i.getMZ()} has abundance {i.getIntensity()*100}% .")
    sulfur_isoDist["mass"].append(i.getMZ())
    sulfur_isoDist["abundance"].append((i.getIntensity() * 100))


# In[33]:


import math 
from matplotlib import pyplot as plt


# In[39]:


def adjustText(x1,y1,x2,y2):
    if y1>y2:
        plt.annotate(('%0.3f' % (y2), xy(x2, y2), xytext(x2+0.5,y2+9),
                     textcoords('data'),
                     arrowprops(dict(arrowstyle="->", color='r', lw=0.5)),
                     horizontalalignment('right', verticalalignment='top')))
    else :
        plt.annotate('%0.3f' % (y1), xy(x1, y1), xytext(x1+0.5,y1+9),
                     textcoords('data'),
                     arrowprops(dict(arrowstyle="->", color='r', lw=0.5)),
                     horizontalalignment('right', verticalalignment='top'))


# In[40]:


def plotDistribution(distribution):
    n = len(distribution["mass"])
    for i in range(0, n):
        plt.vlines(x=distribution["mass"][i], ymin=0, ymax=distribution["abundance"][i])
        if int(distribution["mass"][i - 1]) == int(distribution["mass"][i])                 and i != 0:
            adjustText(distribution["mass"][i - 1], distribution["abundance"][i - 1],
                       distribution["mass"][i], distribution["abundance"][i])
        else:
            plt.text(x=distribution["mass"][i],
                     y=(distribution["abundance"][i] + 2),
                     s='%0.3f' % (distribution["abundance"][i]), va='center',
                     ha='center')
    plt.ylim([0, 110])
    plt.xticks(range(math.ceil(distribution["mass"][0]) - 2,
                     math.ceil(distribution["mass"][-1]) + 2))


# In[41]:


plt.figure(figsize=(10,7))


# In[42]:


plt.subplot(1,2,1)


# In[44]:


plt.subplot(1,2,1)
plt.title("Isotopic distribution of oxygen")
plotDistribution(oxy_isoDist)
plt.xlabel("Atomic mass (u)")
plt.ylabel("Relative abundance (%)")


# In[50]:


isotopes=element.getElement("C").getIsotopeDistribution().getContainer()


# In[51]:


carbon_isotope_difference = isotopes[1].getMZ() - isotopes[0].getMZ()


# In[52]:


isotopes = element.getElement("N").getIsotopeDistribution().getContainer()


# In[53]:


nitrogen_isotope_difference = isotopes[1].getMZ() - isotopes[0].getMZ()


# In[54]:


print(f"The Mass diferrence between 12C and 13C equal :{carbon_isotope_difference}")


# In[56]:


print(f"The Mass Difference between 14N and 15N equal: {nitrogen_isotope_difference}")


# In[57]:


print (f"Relative deviation equal: {100*(carbon_isotope_difference -nitrogen_isotope_difference)/carbon_isotope_difference}% .")


# In[58]:


meth = EmpiricalFormula("CH3OH")


# In[59]:


water = EmpiricalFormula("H2O")


# In[60]:


eth = EmpiricalFormula("CH2") + meth


# In[61]:


print(f"Ethanol chemical formula: {eth.toString()}")


# In[62]:


print(f"Ethanol composition: {eth.getElementalComposition()}")


# In[64]:


print(f"Ethanol has {eth.getElementalComposition()[b'H']} hydrogen atoms")


# In[65]:


lys = ResidueDB().getResidue("Lysine")


# In[66]:


print(lys.getName())
print(lys.getThreeLetterCode())
print(lys.getOneLetterCode())
print(lys.getAverageWeight())


# In[67]:


print(lys.getMonoWeight())
print(lys.getPka())
print(lys.getFormula().toString())


# In[68]:


ox = ModificationsDB().getModification("Oxidation")
print(ox.getUniModAccession())


# In[69]:


print(ox.getUniModRecordId())


# In[70]:


print(ox.getDiffMonoMass())


# In[71]:


print(ox.getId())


# In[72]:


print(ox.getFullId())


# In[73]:


print(ox.getFullName())
print(ox.getDiffFormula())


# In[74]:


isotopes = ox.getDiffFormula().getIsotopeDistribution(CoarseIsotopePatternGenerator(5))
for iso in isotopes.getContainer():
    print (iso.getMZ(), ":", iso.getIntensity())


# In[75]:


uridine = RibonucleotideDB().getRibonucleotide(b"U")


# In[76]:


print(uridine.getName())
print(uridine.getCode())
print(uridine.getAvgMass())
print(uridine.getMonoMass())
print(uridine.getFormula().toString())
print(uridine.isModified())
methyladenosine = RibonucleotideDB().getRibonucleotide(b"m1A")
print(methyladenosine.getName())
print(methyladenosine.isModified())


# In[ ]:





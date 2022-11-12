#!/usr/bin/env python
# coding: utf-8

# In[1]:


#!/usr/bin/env python
# coding: utf-8
# Problem 1
# In[36]:


# In[2]:



THICKNESS=0.00008
folded_thickness=THICKNESS*(2**43)
print("Thickness:{}meters".format(folded_thickness))


# In[3]:


# Problem 2


# In[4]:


# In[37]:


# In[5]:


print ("Thickness:{:2f}kilometers".format(folded_thickness/10000))


# In[6]:


# problem 3


# In[7]:


# In[38]:


# In[8]:


thickness_list=[0.0008]
for i in range (43):
    thickness_list.append(thickness_list[-1]*2)
    print (thickness_list[-1])


# In[9]:


# Problem 4


# In[10]:


# In[39]:


# In[11]:


import time
start=time.time()
THICKNESS=0.00008
folded_thickness=THICKNESS*(2**43)
elapsed_time=time.time()-start
print("time:{}[s]".format(elapsed_time))


# In[12]:


# In[53]:


# In[13]:


import time
start=time.time()
thickness_list=[0.0008]
for i in range (43):
    thickness_list.append(thickness_list[-1]*2)
    elapsed_time=time.time()-start
print("time:{}[s]".format(elapsed_time))


# In[14]:


# In[15]:


# In[15]:


get_ipython().run_cell_magic('timeit', '', 'thickness_list=[0.0008]\nfor i in range (43):\n    thickness_list.append(thickness_list[-1]*2)\n')


# In[16]:


# problem 5


# In[17]:


# In[61]:


# In[18]:


for i in range (43):
    thickness_list.append(thickness_list[-1]*2)

print (thickness_list[-1])


# In[19]:


# problem 6


# In[20]:


# In[60]:


# In[21]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
plt.title("THICKNESS OF FOLDED PAPER")
plt.xlabel("number of folds")
plt.ylabel("thickness[m]")
plt.plot(thickness_list)
plt.show()


# In[22]:


# problem 7


# In[23]:


# In[24]:


# In[24]:


plt.title("THICKNESS OF FOLDED PAPER")
plt.xlabel("number of folds")
plt.ylabel("thickness[m]")
plt.plot(thickness_list,color='green')
plt.tick_params(labelsize = 15)
plt.show()


# In[ ]:





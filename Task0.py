#!/usr/bin/env python
# coding: utf-8

# In[8]:


import csv
import csv
with open('calls_copy.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    
print("calls first row", calls[0]);

import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

print("texts last row",texts[-1]);


# In[ ]:





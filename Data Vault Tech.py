#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd

print(pd.__version__)


# In[16]:


import pandas as pd

data = {
  "Data Vault": ["Simba", "Coke", "Cadbury", "Pepper Steak", "Pear", "Vanilla", "Spinach"],
      " ": ["Lays", "Fanta", "Tex", "Chicken", "Apple", "Chocolate", "Cabbage"],
      "": ["", "", "", "", "Orange", "", ""]
}

df = pd.DataFrame(data, index = ["Chips:", "Cooldrinks:", "Chocolates:", "Pies:", "Fruits:", "Cupcakes:", "Veggies:"])

print(df) 


# In[ ]:





# In[ ]:





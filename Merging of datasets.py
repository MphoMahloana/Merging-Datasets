#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# In[3]:


# 1. Load the three datasets
sales = pd.read_csv('sales_data.csv')
product = pd.read_csv('product_info.csv')
shipping = pd.read_csv('shipping_details.csv')


# In[5]:


sales_df = pd.read_csv('sales_data.csv')
product_df = pd.read_csv('product_info.csv')
shipping_df = pd.read_csv('shipping_details.csv')


# In[6]:


# STEP 2: Now you can merge without the NameError
# Merge sales with product info
master_df = pd.merge(sales_df, product_df, on='Product_ID', how='left')

# Merge with shipping details
master_df = pd.merge(master_df, shipping_df, on='Order_ID', how='left')

# STEP 3: Create the new column
master_df['Total_Revenue'] = master_df['Quantity'] * master_df['Price']

# STEP 4: Save it
master_df.to_csv('master_dataset.csv', index=False)

print("Success! File 'master_dataset.csv' has been created.")


# In[ ]:





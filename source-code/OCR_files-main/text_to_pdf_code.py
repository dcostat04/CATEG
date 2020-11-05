#!/usr/bin/env python
# coding: utf-8

# In[1]:


##code to turn text file to pdf
from fpdf import FPDF


# In[3]:


pdf = FPDF()


# In[4]:


pdf.add_page()


# In[5]:


pdf.set_font("Arial",size = 7)


# In[6]:


pdf.cell(150,150,txt = "Here we will put the output obtained in the last code",ln = 1,align = "C")


# In[7]:


pdf.output("sample.pdf")


# In[ ]:





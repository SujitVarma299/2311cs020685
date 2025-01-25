#!/usr/bin/env python
# coding: utf-8

# In[2]:


a = float(input("Enter marks for sub1: "))
b = float(input("Enter marks for sub2: "))
c = float(input("Enter marks for sub3: "))
avg = (a+b+c)/3
if avg >= 90:
    result = "A"
elif 80 <= avg < 90:
    result = "B"
elif 70 <= avg < 80:
    result = "C"
else:
    result = "Fail"
    
print("Grade: ",(result))


# In[ ]:
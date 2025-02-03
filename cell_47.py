#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from datetime import date, datetime
import pytz
today = date.today()
time = datetime.now(pytz.timezone('CET')).strftime('%H:%M:%S')
today = today.strftime("%d - %m - %y")
print("today's date: ", today, "\ntime : " , time)


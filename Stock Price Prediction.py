#!/usr/bin/env python
# coding: utf-8

# # Streamlit Application

# In[3]:


#!pip install yfinance
#!pip install streamlit
import yfinance as yf
import streamlit as st
import pandas as pd


# In[ ]:


st.write("""
# Simple Stock Price App

Stock details for Google are shown below

""")


# In[4]:


tickerSymbol = 'GOOGL'
tickerData = yf.Ticker(tickerSymbol)


# In[5]:


tickerDf = tickerData.history(period='id', start='2010-5-31', end='2020-5-31')


# In[6]:


st.line_chart(tickerDf.Close)


# In[ ]:


st.line_chart(tickerDf.Volume)


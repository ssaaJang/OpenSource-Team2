#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st


# In[ ]:


conda create -n stenv python=3.9


# In[ ]:


conda activate stenv


# In[ ]:


pip install streamlit


# In[ ]:


streamlit hello


# In[ ]:


view = [100,150,30]


# In[ ]:


streamlitapp python -3 streamlit run app.py


# In[ ]:


import streamlit as st
view = [100,150,30]
st.write('# Youtube view')
st.write('## raw')
view
st.wrtie('## bar chart')
st.bar_chart(view)
import pandas as pd
sview = pd.Series(view)
sview


# In[ ]:

import streamlit as st

st.title('This is a title')

st.header('This is a header')

st.subheader('This is a subheader')

st.markdown('_Markdown_')

st.text('This is sample text')

st.latex(r''' e^{i\pi} + 1 = 10 ''')

st.caption('This is a caption')



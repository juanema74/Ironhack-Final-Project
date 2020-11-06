#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import streamlit as st
import plotly.graph_objects as go
from plotly import tools
import plotly.offline as py
import plotly.express as px
import cufflinks as cf
from plotly.offline import plot
import chart_studio.plotly as py


# In[2]:


cf.go_offline()


# In[3]:


df = pd.read_csv('../notebooks/summary.csv')
pc = pd.read_csv('../notebooks/pc_comp_scrap/pc.csv')
worten = pd.read_csv('../notebooks/worten_scrap/worten.csv')


# In[ ]:





# In[4]:


st.title("** :desktop_computer:** **TV Marketplace Price Evolution** **:desktop_computer:**")
st.header("This is an App created to visualize the price Evolution of Ultra HD 4K TVs in 2  Manufactures: LG and Samsung, in 2 different marketplaces: Pc Componentes and Worten.")
st.subheader("The Dashboards will show Price evolution since October 3rd.")


# In[5]:


image = ('/Users/juandediegosuanzes/desktop/Ironhack-Final-Project/streamlit/samsung_vs_lg_')


# In[6]:


st.image(image, width=None)


# In[7]:


pc_ok = pc[['PC LG', 'PC SS']]
worten_ok = worten[['Worten LG', 'Worten SS']]
df_ok = df[['PC LG', 'PC SS', 'Worten LG', 'Worten SS']]


# In[8]:


st.markdown("#### " +"Pc Componentes & Worten Price Evolution in LG and Samsung")


# In[9]:


st.line_chart(data=df_ok, width=0, height=0, use_container_width=True)


# In[10]:


st.markdown("#### " +"Select the manufacturer and the marketplace you would like to see the metrics in detail")

selected_metrics = st.selectbox(
    label="Choose...", options=['PC LG','PC SS','Worten LG','Worten SS']
)


# In[11]:


fig = go.Figure()
if selected_metrics == 'PC LG':
	fig.add_trace(go.Scatter(x=df.day, y=df['PC LG'],
                    mode='lines+markers', name='PC LG'))
if selected_metrics == 'PC SS':
	fig.add_trace(go.Scatter(x=df.day, y=df['PC SS'],
	                    mode='lines+markers', name='PC SS'))
if selected_metrics == 'Worten LG':
	fig.add_trace(go.Scatter(x=df.day, y=df['Worten LG'],
	                    mode='lines+markers',name='Worten LG'))
if selected_metrics == 'Worten SS':
	fig.add_trace(go.Scatter(x=df.day, y=df['Worten SS'],
	                    mode='lines+markers',name='Worten SS'))
st.plotly_chart(fig, use_container_width=True)


# In[12]:


if st.checkbox('Show dataframe'):
    st.dataframe(df.style.highlight_max(axis=0))


# In[13]:


st.markdown("#### " +"Pc Componentes Price Evolution by Manufacturer")


# In[14]:


image_pc = ('/Users/juandediegosuanzes/desktop/Ironhack-Final-Project/streamlit/PcComponentes.png')


# In[15]:


st.image(image_pc, width=None)


# In[16]:


st.area_chart(data=pc_ok, width=0, height=0, use_container_width=True)


# In[17]:


if st.checkbox('Show PC Componentes dataframe'):
    st.dataframe(pc.style.highlight_max(axis=0))


# In[18]:


st.markdown("#### " +"Worten Price Evolution by Manufacturer")


# In[19]:


image_worten = ('/Users/juandediegosuanzes/desktop/Ironhack-Final-Project/streamlit/worten_im.webp')


# In[20]:


st.image(image_worten, width=None)


# In[21]:


st.area_chart(data=worten_ok, width=0, height=0, use_container_width=True)


# In[22]:


if st.checkbox('Show Worten dataframe'):
    st.dataframe(worten.style.highlight_max(axis=0))


# In[23]:


#st.title("** :champagne:** **¡¡GRACIAS A TODOS!!: Lead Teachers, TA y enhorabuena compañeros!!** **:champagne:**")


# In[24]:


#video_file = open('/Users/juandediegosuanzes/desktop/video.mp4', 'rb')
#video_bytes = video_file.read()
#st.video(video_bytes)


# In[25]:


#audio_file = open('/Users/juandediegosuanzes/desktop/champ.mp3', 'rb')
#audio_bytes = audio_file.read()
#st.audio(audio_bytes, format='audio/ogg', start_time=34)


# In[26]:


#fig = df.iplot(kind='box', 
#                       histnorm='percent', 
 #                      xTitle='October Scraping', 
  #                     yTitle='Price €', 
   #                    title='Summary Price by Brand and Marketplace',
    #                   subplots=True)

#st.pyplot(fig)


# In[ ]:





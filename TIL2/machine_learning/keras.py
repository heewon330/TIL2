#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tensorflow as tf


# In[2]:


import warnings
warnings.filterwarnings('always')
warnings.filterwarnings('ignore')


# In[3]:


tf.test.gpu_device_name()


# In[4]:


gpu=tf.config.experimental.list_physical_devices('GPU')[0]
tf.config.experimental.set_virtual_device_configuration(
    gpu,
    [tf.config.experimental.VirtualDeviceConfiguration(memory_limit=3000)]
)


# In[9]:


get_ipython().system('pip install seaborn')


# In[5]:


import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns


# In[6]:


temp = np.array([32.13, 25.95, 27.95, 26.3, 26.33, 32.78, 31.48, 
    32.63, 28.2, 31.82, 25.52, 27.42, 28.92, 30.17, 
    29.09, 31.38, 29.52, 27.83, 30.27, 26.91])
elec = np.array([364.5, 105.82, 147.28, 89.57, 114.05, 411.23, 
    301.93, 386.16, 149.09, 327.93, 111.67, 130.59, 180.6, 
    214.77, 188.84, 312.11, 194.13, 135.12, 236.75, 113.6])


# In[7]:


df = pd.DataFrame( np.array( [elec, temp] ).T, columns=['elec', 'temp'] )
df.sort_values(by='temp', inplace=True, ignore_index=True)
df


# In[8]:


x = tf.constant(df[['temp']].to_numpy(), dtype=tf.float64)
y = tf.constant(df['elec'].to_numpy(), dtype=tf.float64)


# In[28]:


model = tf.keras.models.Sequential()

# layer는 생성된 모델 객체에 add를 통해서 쉽게 추가
model.add( tf.keras.layers.Dense(1, input_shape=x.shape) )

# 최적화 옵션
optimizer = tf.keras.optimizers.RMSprop(0.001)
model.compile(
  loss='mse', 
  optimizer = optimizer
)


# In[29]:


history = model.fit(x, y, epochs=100000, verbose=0)


# In[30]:


plt.plot( history.history['loss'] )


# In[31]:


model.get_weights()


# In[32]:


df.plot(kind='scatter', x='temp', y='elec')
plt.plot( df['temp'].to_numpy(), model.predict( df[['temp']]).flatten() )
plt.grid()
plt.show()


# ## 비선형 모델로 
# - 케라스를 사용

# In[38]:


x = tf.constant(df[['temp']].to_numpy(), dtype=tf.float64)
y = tf.constant(df['elec'].to_numpy(), dtype=tf.float64)


# In[56]:


model = tf.keras.models.Sequential()

# hidden layer
model.add( tf.keras.layers.Dense(10, activation='tanh',input_shape=x.shape))
model.add( tf.keras.layers.Dense(4, activation='tanh'))

#output layer
model.add( tf.keras.layers.Dense(1) )

# 최적화 옵션
optimizer = tf.keras.optimizers.Adam(0.01)
model.compile(
  loss='mse', 
  optimizer = optimizer
)


# In[61]:


model.fit(x, y, epochs=100000, verbose=0)


# In[62]:


model.get_weights()


# In[63]:


plt.plot( history.history['loss'] )


# In[64]:


df.plot(kind='scatter', x='temp', y='elec')
plt.plot( df['temp'].to_numpy(), model.predict( df[['temp']]).flatten() )
plt.grid()
plt.show()


# In[ ]:





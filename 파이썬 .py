#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# # DF 구경하기

# In[2]:


df = pd.read_csv("C:\\Users\\kim a hyun\\Desktop\\사고다발지현황.csv",encoding='cp949')
type(df)


# In[3]:


df


# In[4]:


df=df.drop(columns=['다발지식별자','다발지역그룹식별자','법정동코드','위치코드','사고다발지역폴리곤정보'])


# In[5]:


df.head(7)


# In[6]:


df.tail(7)


# In[7]:


df=df.replace(0,np.NaN)


# In[8]:


columns = df.columns
#list(columns)
pd.Series(columns)


# In[9]:


index = df.index
index


# In[10]:


data = df.to_numpy()
data


# In[11]:


df.dtypes.value_counts()


# In[12]:


df.info()


# ## 기술통계

# In[13]:


df.describe()


# ## 결측치

# In[14]:


df.isna()


# In[15]:


df.isna().sum()


# In[16]:


df.fillna(0,inplace=True) # 사망자수~부상자수 NaN값을 0으로 채워넣기


# In[17]:


# df.loc[2035:2037,:'시군명'=='여주군']


# In[18]:


#geos['시군명'=0] == df['여주시']


# In[19]:


#names.loc[len(names)] = ['NaN', ]
#na


# In[ ]:


df.loc[2035:2037,:'시군명']


# In[ ]:


# df.loc[2035:2037,:시군명=='여주시']


# In[ ]:


# df.loc[df['시군명'] == 0, '시군명'] = '여주시'

# df


# In[ ]:


df.shape


# In[ ]:


df.size


# In[ ]:


len(df)


# In[ ]:


df.ndim


# # 오류 수정

# In[41]:


df.fillna('여주시')


# In[42]:


df.loc[df['사고유형구분'] == '자전?', '사고유형구분'] = '자전거사고다발지'

df


# In[43]:


df['사고유형구분']


# In[44]:


df.loc[df['사고유형구분'] == '보헹노', '사고유형구분'] = '보행노인사고다발지'

df


# In[ ]:


df


# In[ ]:


df['사고유형구분']


# ## memory_usage

# In[20]:


df.info()


# In[21]:


df.dtypes


# In[22]:


df.memory_usage(deep=True)


# In[23]:


np.iinfo(np.int8)


# In[24]:


np.iinfo(np.int16)


# In[25]:


df['사고유형구분'] = df['사고유형구분'].astype('object')
df.memory_usage(deep=True)


# In[26]:


df['발생건수'] = df['발생건수'].astype(np.int8)


# In[27]:


df.memory_usage(deep=True)


# In[28]:


df['사상자수'] = df['사상자수'].astype(np.int8)


# In[29]:


df.memory_usage(deep=True)


# In[30]:


df['중상자수'] = df['중상자수'].astype(np.int8)


# In[31]:


df.memory_usage(deep=True)


# In[32]:


df['경상자수'] = df['경상자수'].astype(np.int8)


# In[33]:


df.memory_usage(deep=True)


# In[34]:


df['부상자수'] = df['부상자수'].astype(np.int8)


# In[35]:


df.memory_usage(deep=True)


# In[36]:


df['시군명'] = df['시군명'].astype('object')
df.memory_usage(deep=True)


# In[37]:


df.memory_usage(deep=True)


# # ---------------------------------------------------------------

# In[ ]:


# df.select_dtypes(include=['object']).nunique()


# In[ ]:


# df.memory_usage(deep=True)


# In[ ]:


# df.index


# ## 최대 중 최소, 최소 중 최대 - nsmallest, nlargest

# In[45]:


df1=df[['사고년도','사고유형구분','시도시군구명','발생건수']]
df1.head()


# In[46]:


df1.nlargest(50,'사고년도').head(11)


# In[47]:


# 사고유형을 기준으로 정렬하기
(
    df[['사고년도','사고유형구분','시도시군구명','발생건수']]
.sort_values('사고유형구분',ascending=True)
)


# In[48]:


(
    df[['사고년도','사고유형구분','시도시군구명','발생건수']]
.sort_values('사고유형구분',ascending=False)
)


# ## 데이터 딕셔너리

# In[49]:


pd.read_csv('C:\\Users\\kim a hyun\\Desktop\\사고다발지현황.csv',encoding='cp949',index_col=0)


# In[ ]:





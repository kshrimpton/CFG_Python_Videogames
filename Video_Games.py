#!/usr/bin/env python
# coding: utf-8

# # VIDEO GAMES PROJECT

# In[1]:


import pandas as pd


# In[2]:


import seaborn as sns


# In[3]:


import matplotlib as mpl
mpl.style.use('ggplot')


# In[4]:


import matplotlib.pyplot as plt


# Importing dataset

# In[5]:


df=pd.read_csv('vgsales.csv',engine='python')

#importing dataset


# Dropping NaN values

# In[6]:


df.dropna(how="any",inplace = True)
df.info()

#dropping NaN values


# In[7]:


df.set_index('Rank', inplace = True)

#setting rank as index


# In[8]:


df


# I want to see which genre has been the most popular by number of titles 

# In[9]:


df['Genre'].value_counts()

#I want to see which genre has been the most popular by number of titles 


# Creating a column for count of titles per genre to plot a chart

# In[10]:


df1=pd.DataFrame(df['Genre'].value_counts(ascending = True))
df1

#creating a column for count of titles per genre to plot a chart


# In[11]:


df1.mean()


# In[12]:


df1.columns=['Count']


# Action and action-related titles (sports, role-playing, shooter) produce the most # of titles, with puzzle and strategy
# at the bottom. This is consistent with expectations, since puzzle games tend to be more niche

# In[13]:


#Action and action-related titles (sports, role-playing, shooter) produce the most # of titles, with puzzle and strategy
#at the bottom. This is consistent with expectations, since puzzle games tend to be more niche


# In[14]:


df1.plot(kind='barh', figsize = (10,6), color = '#db3298')
plt.xlabel('Genre')
plt.ylabel('Number of Titles')
plt.title('Number of Titles by Genre')


# Now let's look at Global Sales by Genre

# In[15]:


df3 = df.loc[:,['Genre','Global_Sales']]


# In[16]:


df4 = df3.groupby('Genre').sum()
df4.sort_values('Global_Sales', inplace = True)
df4


# In[17]:


df4.plot(kind='barh', figsize = (10,6), color = '#d67ade')
plt.xlabel('Global Sales (ml)')
plt.ylabel('Genre')
plt.title('Global Sales by Genre')


# - Action clings to 1st spot
# - Adventure marks a hefty decline in ranking: many Adventure titles but few sales per title?
# 

# Now let's look at the average Global Sales per title 

# In[18]:


per_title=df.loc[:,['Global_Sales', 'Genre']]
per_title.groupby('Genre').size()


# In[19]:


per_title1=per_title.groupby('Genre').sum()
per_title1['counts'] = per_title.groupby('Genre').size()
per_title1['average (thousands)'] = (per_title1['Global_Sales']/per_title1['counts'])*1000
per_title1.sort_values(by = 'average (thousands)', inplace = True)
per_title1.loc[:,['average (thousands)']].plot(kind='barh', figsize = (10,6), color = '#19cad2')
plt.title('Sales per Title by Genre')


# - Platform games take top spot for sales per title
# - Adventure reveals the lowest sales per title
# - Not many platform games despite high returns per game - why?
# 

# In[34]:


adventure=df.loc[:,['Name', 'Genre', 'Platform']]

df17=adventure[adventure['Genre']=='Platform']

df17['Platform'].value_counts()


# - Over 1/4 of all Platform games were made for 2 gaming platforms - GBA (GameBoyAdvanced) & PS2, but otherwise there is quite a spread, so this doesn't tell us much

# In[48]:


df[df['Genre']=='Platform'].head(10)


# - All top 10 platform games are from the Super Mario franchise
# - Most likely this has skewed the Sales/Title

# In[36]:


df18=df[df['Genre']=='Platform']['Year'].value_counts()
df19=pd.DataFrame(df18)
df19.reset_index(inplace = True)
df19.sort_values(by = 'index', inplace = True)
df19.columns = ['Year','count']
df19.set_index('Year').plot(kind='bar')
plt.title('Platform Games by Year')


# - 2006-2010 marked period of growth for Adventure games 
# - Sharp decline from 2010 onwards

# Now let's look at the top 10 games 

# In[22]:


top_games=df.loc[:,['Name','Global_Sales']].head(10)
top_games.set_index('Name', inplace = True)
top_games = top_games.sort_values(by = 'Global_Sales', ascending = True)
top_games.plot(kind='barh', figsize = (10,6), color = '#ffa3d4')
plt.title('Top 10 Games by Sales')


# In[ ]:





# In[ ]:





# In[23]:


#Now that we've got a big picture overview, let's break this data down to look at the distribution of sales by territory


# In[24]:


region_sales = df.loc[:,['NA_Sales','EU_Sales','JP_Sales','Other_Sales']].sum()
region_sales.plot(kind='bar', figsize = (10,6), color = '#ffa751')
plt.title('Sales by Region')


# In[25]:


#Let's look at sales by region over time 


# In[28]:


df15=df.loc[:,['Year','NA_Sales','EU_Sales','JP_Sales','Other_Sales']]


# In[30]:


df15=df15.groupby('Year').sum()
df15.reset_index(inplace = True)


# In[33]:


ax = df15.plot(kind="scatter", x="Year",y="NA_Sales", color="b", label="NA Sales", figsize =(16,8))

df15.plot(kind='scatter',x="Year",y="EU_Sales", color="r", label="EU_Sales", ax=ax)

df15.plot(kind='scatter',x="Year",y="JP_Sales", color="orange", label="JP_Sales", ax=ax)
df15.plot(kind='scatter',x="Year",y="Other_Sales", color="green", label="Other_Sales", ax=ax)


# In[ ]:


ax = region_sales_year.plot(kind="scatter", x="Year",y="NA_Sales", color="b", label="NA Sales", figsize =(16,8))

region_sales_year.plot(kind='scatter',x="Year",y="EU_Sales", color="r", label="EU_Sales", ax=ax)

region_sales_year.plot(kind='scatter',x="Year",y="JP_Sales", color="orange", label="EU_Sales", ax=ax)
region_sales_year.plot(kind='scatter',x="Year",y="JP_Sales", color="green", label="EU_Sales", ax=ax)


# In[ ]:





# In[ ]:


#Now let's look at sales by genre in each region


# In[ ]:


df6 = df.loc[:, ['Genre', 'NA_Sales','EU_Sales','JP_Sales','Other_Sales']]


# In[ ]:


df7=df6[(df6['Genre']=='Action')|(df6['Genre']=='Sports')|(df6['Genre']=='Shooter')|(df6['Genre']=='Role-Playing')|(df6['Genre']=='Platform')|(df6['Genre']=='Misc')|(df6['Genre']=='Racing')|(df6['Genre']=='Fighting')|(df6['Genre']=='Simulation')|(df6['Genre']=='Puzzle')|(df6['Genre']=='Adventure')|(df6['Genre']=='Strategy')]


# In[ ]:


df8=df7.groupby('Genre').sum()


# In[ ]:


df8


# In[ ]:


#grouping titles by genre according to geographical distribution 


# In[ ]:


ax = df8.plot(kind='bar', figsize = (16,8))
for m in ax.patches:
    width, height = m.get_width(), m.get_height()
    x, y = m.get_xy()
    ax.annotate('{:.0f}'.format(height), (x, y + height + 4), fontsize = 10)


# In[ ]:


#Through this we can see that North American market dominates every genre apart from Role-Playing, dominated by Japan


# In[ ]:





#%% [markdown]
# ## Markdown title

#%%
import pandas as pd # type: ignore
df = pd.DataFrame({'a':[5,6]})
df.head()



#%% [markdown]
# ## Try to read csv

#%%
ba = pd.read_csv('~/Downloads/Lauren-s-Furniture-Store-Transaction-Table.csv')
ba.shape #dim()

ba.head(10)
#%%
ba.mean()  #not working why? I think it's dataset cause it

#%% [markdown]
# ## Seaborn and plot

#%%
import sys
import seaborn as sns # weird, unable to install



# %%

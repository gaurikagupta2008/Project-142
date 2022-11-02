import pandas as pd
import numpy as np

df = pd.read_csv(r'C:\Users\gauri\OneDrive\Desktop\C and P 136\P141\MAIN.csv')
df=df.sort_values(['total_events'],ascending=False)
df.head()
output=df[['url','title','text','lang','total_events']].head(20).values.tolist()


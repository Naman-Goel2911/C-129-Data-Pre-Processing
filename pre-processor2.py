import pandas as pd
import csv

df = pd.read_csv('dwarf_stars.csv')
df = df[df['Star_name'].notna()]
df = df[df['Mass'].notna()]
df = df[df['Radius'].notna()]
df = df[df['Distance'].dropna()]
df.dtype()

df['Radius'] = df['Radius']*0.102763
df['Mass'] = df['Mass'].apply(lambda x:x.replace('$', ''))
df['Mass'] = df['Mass']*0.000954588

df.head()
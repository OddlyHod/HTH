import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


colors = ['#0E4AB0','#0F76B1', '#0FA3B1', '#3F7680']
df = pd.read_csv('heartStandardized.csv')

plt.figure(figsize = (20,5))
sns.heatmap(df.corr(),cmap = colors,annot = True);

plt.show()

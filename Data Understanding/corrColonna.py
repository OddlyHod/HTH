import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


colors = ['#0E4AB0','#0F76B1', '#0FA3B1', '#3F7680']
df = pd.read_csv('heartStandardized.csv')

plt.figure(figsize = (20,5))
sns.heatmap(df.corr(),cmap = colors,annot = True);

corr = df.corrwith(df['HeartDisease']).sort_values(ascending = False).to_frame()
corr.columns = ['Coefficiente di Correlazione']
plt.subplots(figsize = (5,5))
sns.heatmap(corr,annot = True,cmap = colors,linewidths = 0.4,linecolor = 'black');
plt.title('Correlazioni con HeartDisease');

plt.show()

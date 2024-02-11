import matplotlib.pyplot as plt
import pandas as pd


colors = ['#0E4AB0','#0F76B1', '#0FA3B1', '#3F7680']
df = pd.read_csv('heartStandardized.csv', delimiter=',')
df.drop(columns=['Unnamed: 12'], inplace=True)

l = list(df['HeartDisease'].value_counts())
circle = [l[1] / sum(l) * 100,l[0] / sum(l) * 100]

fig,ax = plt.subplots(nrows = 1,ncols = 1,figsize = (20,5))
plt.subplot(1,1,1)
plt.pie(circle,labels = ['No','Sì'],autopct='%1.1f%%',startangle = 90,explode = (0.1,0),colors = colors,
        wedgeprops = {'edgecolor' : 'black','linewidth': 1,'antialiased' : True})
plt.title('Heart Disease %');


plt.show()

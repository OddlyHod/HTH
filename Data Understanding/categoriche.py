import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import f_classif

colors = ['#0E4AB0','#0F76B1', '#0FA3B1', '#3F7680']
df = pd.read_csv('heartStandardized.csv', delimiter=',')
df.drop(columns=['Unnamed: 12'], inplace=True)

col = list(df.columns)
categorical_features = []
numerical_features = []
for i in col:
    if len(df[i].unique()) > 6:
        numerical_features.append(i)
    else:
        categorical_features.append(i)

le = LabelEncoder()
df1 = df.copy(deep = True)

df1['Sex'] = le.fit_transform(df1['Sex'])
df1['ChestPainType'] = le.fit_transform(df1['ChestPainType'])
df1['RestingECG'] = le.fit_transform(df1['RestingECG'])
df1['ExerciseAngina'] = le.fit_transform(df1['ExerciseAngina'])
df1['ST_Slope'] = le.fit_transform(df1['ST_Slope'])

fig, ax = plt.subplots(nrows=3, ncols=2, figsize=(10, 15))
for i in range(len(categorical_features) - 1):
    plt.subplot(3, 2, i + 1)
    sns.distplot(df1[categorical_features[i]], kde_kws={'bw': 1}, color=colors[0]);
    title = 'Distribution : ' + categorical_features[i]
    plt.title(title)

plt.figure(figsize=(4.75, 4.55))
sns.distplot(df1[categorical_features[len(categorical_features) - 1]], kde_kws={'bw': 1}, color=colors[0])
title = 'Distribution : ' + categorical_features[len(categorical_features) - 1]
plt.title(title);


plt.show()

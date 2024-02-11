import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('heartStandardized.csv')
true = df.duplicated().sum()
false = (~df.duplicated()).sum()
print("Valori VERI", true)
print("Valori FALSI", false)

fig = plt.figure(figsize=(3, 2))

plt.bar(["Duplicati", "Non Duplicati"], [true, false], color='blue',
        width=0.5, align='center')

plt.show()

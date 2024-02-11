import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import missingno as msno

df = pd.read_csv('heartStandardized.csv')
msno.matrix(df)
plt.show()
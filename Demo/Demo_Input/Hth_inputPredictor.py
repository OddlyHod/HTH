import pandas as pd
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import MinMaxScaler,StandardScaler


def predict_diabetes(input_d):
    prediction = model.predict(input_d)
    return prediction[0]


dataset = pd.read_csv("heartStandardized.csv")
attributes = ["Age", "Sex", "ChestPainType", "Cholesterol",
              "FastingBS", "MaxHR", "ExerciseAngina", "Oldpeak", "ST_Slope"]
X = dataset[attributes]
y = dataset["HeartDisease"]

# NB Classificatore
#modello = GaussianNB()
#print("Valutazione - Naive Bayes")

#Decision Tree
#modello = DecisionTreeClassifier(random_state = 42,max_depth = 15,min_samples_leaf = 1)
#print("Valutazione - Decision Tree")

#Random Forest
#modello = RandomForestClassifier(max_depth = 42, random_state = 0)
#print("Valutazione - Random Forest")

#Logistic Regression
model = LogisticRegression(random_state = 42, C=1.0, penalty= 'l2')
model.fit(X, y)
print("Modello addestrato.")

#Andremo a normalizzare/standardizzare i dati di input, poiché il modello lavora su dati normalizzati/standardizzati
mms = MinMaxScaler()
ss = StandardScaler()

# Alcuni esempi su cui il modello non è addestrato
# Age,Sex,ChestPainType,Cholesterol,FastingBS,MaxHR,ExerciseAngina,Oldpeak,ST_Slope
# 62  1   1             208         1         140   0              0       2
# 46  1   0             311         0         120   1              1.8     1

input_data = {
    "Age": 62,
    "Sex": 1,                                #M: 0, F: 1
    "ChestPainType": 1,                      #TA: 0, ATA: 1, NAP: 2, ASY: 3
    "Cholesterol": 208,
    "FastingBS": 1,
    "MaxHR": 140,
    "ExerciseAngina": 0,                     #Y: 0, N: 1
    "Oldpeak": 0,
    "ST_Slope": 2,                           #Up: 0, Flat: 1, Down: 2
}

input_df = pd.DataFrame([input_data.values()], columns=attributes)

input_df['Oldpeak'] = mms.fit_transform(input_df[['Oldpeak']])
input_df['Age'] = ss.fit_transform(input_df[['Age']])
input_df['Cholesterol'] = ss.fit_transform(input_df[['Cholesterol']])
input_df['MaxHR'] = ss.fit_transform(input_df[['MaxHR']])

result = predict_diabetes(input_df)
if result == 0:
    print("Il paziente non è prono a scompensi cardiaci.")
else:
    print("Il paziente è prono a scompensi cardiaci.")

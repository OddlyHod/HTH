import pandas as pd
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler,StandardScaler
from sklearn.metrics import accuracy_score

def model(classifier):
    df = pd.read_csv('heartStandardized.csv', delimiter=',')
    features = df[df.columns.drop(['HeartDisease', 'RestingBP', 'RestingECG'])].values
    target = df['HeartDisease'].values
    x_train, x_test, y_train, y_test = train_test_split(features, target, test_size=0.20, random_state=2)
    classifier.fit(x_train, y_train)
    classifier.predict(x_test)
    print("Modello Addestrato.")


def model_Predict(modell):
    # Una volta addestrato il modello, andremo ad introdurre un nuovo dataset, ed effettueremo predizione,
    # per vederne il funzionamento
    df_Test = pd.read_csv('Hth_heartTest.csv', delimiter=',').drop(columns=['Caa', 'thall'])
    target = df_Test['HeartDisease'].values
    # Effettuiamo la standardizzazione/normalizzazione dei dati
    dff = df_Test.copy(deep=True)
    mms = MinMaxScaler()
    ss = StandardScaler()

    dff['Oldpeak'] = mms.fit_transform(dff[['Oldpeak']])
    dff['Age'] = ss.fit_transform(dff[['Age']])
    dff['Cholesterol'] = ss.fit_transform(dff[['Cholesterol']])
    dff['MaxHR'] = ss.fit_transform(dff[['MaxHR']])
    dff = dff.drop(columns=['RestingECG','RestingBP','HeartDisease'])

    # Visto che stiamo solo VALUTANDO non ci serve testare i dati anche su questo dataset, quindi la test_size sarà uguale ad 1
    pred = modell.predict(dff.values)
    print("Accuracy : ", '{0:.2%}'.format(accuracy_score(target, pred)))


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
#modello = LogisticRegression(random_state = 42, C=1.0, penalty= 'l2')
model(modello)
model_Predict(modello)
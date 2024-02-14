import pandas as pd
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler,StandardScaler
from sklearn.metrics import accuracy_score

def model(classifier):
    df = pd.read_csv('heartStandardized.csv', delimiter=',')
    features = df[df.columns.drop(['HeartDisease', 'RestingBP', 'RestingECG'])].values
    target = df['HeartDisease'].values
    x_train, x_test, y_train, y_test = train_test_split(features, target, test_size=0.20, random_state=2)
    classifier.fit(x_train, y_train)
    c = classifier.predict(x_test)
    print("Modello Addestrato.")


def model_Predict(modell):
    # Una volta addestrato il modello, andremo ad introdurre un nuovo dataset, ed effettueremo predizione,
    # per vedere il funzionamento vero e proprio
    df_Test = pd.read_csv('Hth_heartTest.csv', delimiter=',').drop(columns=['Caa', 'thall'])
    features = df_Test[df_Test.columns.drop(['HeartDisease', 'RestingBP', 'RestingECG'])].values
    # Effettuiamo la standardizzazione/normalizzazione dei dati
    le = LabelEncoder()
    dff = df_Test.copy(deep=True)
    dff['Sex'] = le.fit_transform(dff['Sex'])
    dff['ChestPainType'] = le.fit_transform(dff['ChestPainType'])
    dff['RestingECG'] = le.fit_transform(dff['RestingECG'])
    dff['ExerciseAngina'] = le.fit_transform(dff['ExerciseAngina'])
    dff['ST_Slope'] = le.fit_transform(dff['ST_Slope'])

    mms = MinMaxScaler()
    ss = StandardScaler()

    dff['Oldpeak'] = mms.fit_transform(dff[['Oldpeak']])
    dff['Age'] = ss.fit_transform(dff[['Age']])
    dff['RestingBP'] = ss.fit_transform(dff[['RestingBP']])
    dff['Cholesterol'] = ss.fit_transform(dff[['Cholesterol']])
    dff['MaxHR'] = ss.fit_transform(dff[['MaxHR']])

    target = df_Test['HeartDisease'].values
    # Visto che stiamo solo VALUTANDO non ci serve testare i dati anche su questo dataset, quindi la test_size sarà uguale ad 1
    x_train, x_test, y_train, y_test = train_test_split(features, target, train_size=0.01 ,test_size=0.99, random_state=2)
    pred = modell.predict(x_test)
    print("Accuracy : ", '{0:.2%}'.format(accuracy_score(y_test, pred)))


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
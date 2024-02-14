# Heart to Heart 🩺
![GitHub commit activity](https://img.shields.io/github/commit-activity/t/OddlyHod/HTH)
![GitHub last commit](https://img.shields.io/github/last-commit/OddlyHod/HTH)
![GitHub Repo stars](https://img.shields.io/github/stars/OddlyHod/HTH)


→ Heart Disease Predictor. ←

📁 Data Understanding → Contiene gli script utilizzati per l'analisi dei dati;

📁 Dataset       → Contiene i dataset;

📁 Demo          → Contiene la demo del progetto;

📁 Documents     → Contiene la documentazione.

Collaboratori: [_Di Tella Nazaro_](https://github.com/OddlyHod), [Amendola Alfredo](https://github.com/Alfredoame) e [Xu Xin Yu](https://github.com/XXY126). 🙋🙋🙋


## Tavola dei Contenuti 📋
* [Informazioni Generali](#informazioni-generali-ℹ)
  + [Cos'è?](#cosè-)
  + [Obiettivi](#obiettivi-)
* [Tecnologie Utilizzate](#Tecnologie-Utilizzate-)
* [Features](#features-)
* [Setup](#setup-)
* [Utilizzo](#utilizzo-)
* [Project Status](#project-status-)
* [Migliorie](#migliorie-)
* [Acknowledgements](#ringraziamenti-)


## Informazioni Generali ℹ
### Cos'è ❓
_HtH_ è un progetto per l'analisi di cartelle cliniche al fine di creare, addestrare e validare un modello di ML, annotando quelle che sono le performance dei vari modelli considerati. 
### Obiettivi 🎯
L’obiettivo che HTH si pone è quello di ridurre al minimo l’errore umano creando e sviluppando un modello di intelligenza artificiale per predire uno scompenso cardiaco.
Tramite lo sviluppo di questo modello si prova ad automatizzare la diagnosi di uno scompenso cardiaco lasciando al medico più tempo per concentrarsi sul trattamento.

## Tecnologie Utilizzate 📊
- Python
- Seaborne
- Numpy
- Matplot
- Scikit - Learn


## Features 📝
- Data Analysis
- Data Visualization
- 4 Modelli Predittivi
- Modelli Funzionanti ed Applicabili

## Setup 🖥
Per effettuare il setup del modello, bisognerà semplicemente scaricare nella stessa cartella i file 
+ __*"Hth_datasetPredictor.py"*__, _***heartStandardized.csv***_, _***"Hth_heartTest.csv"***_

Se si vogliono testare i modelli su un dataset completamente scollegato da quello del training (__*"Hth_heartTest.csv"*__) mentre, scericare i file
+ __*"Hth_inputPredictor.py"*__ e "_***heartStandardized.csv***_"

Se si vogliono testare i modelli con una singola cartella clinica. 


## Utilizzo 🖥
Per utilizzare il modello, basterà semplicemente
+ Far partire lo script, nel caso si stia testando col dataset;
+ Inserire dei dati di input e far partire lo script in Python altrimenti, come da esempio:
```
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
``` 

## Project Status 👍
Il Progetto è: **_Completo_**. ✅

## Migliorie 🩺
È possibile migliorare le percentuali di accuratezza dei modelli, integrando il lavoro svolto con un punto di vista medico/statistico.

Migliorie:
- Data Analysis con Approccio Medico 🫀

## Ringraziamenti 🙏
- Si ringraziano il Professore ed i Tutor per averci guidato lungo il percorso; 🥰
- Si ringraziano i medici contattati per il loro riscontro sul Dataset. 🫡

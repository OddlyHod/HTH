# Heart to Heart 🩺
→ Heart Disease Predictor. ←

![GitHub commit activity](https://img.shields.io/github/commit-activity/t/OddlyHod/HTH)
![GitHub last commit](https://img.shields.io/github/last-commit/OddlyHod/HTH)

Collaboratori: [_Di Tella Nazaro_](https://github.com/OddlyHod), [_Amendola Alfredo_](https://github.com/Alfredoame) e [_Xu Xin Yu_](https://github.com/XXY126).


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
- Analisi Dataset
- 4 Modelli Predittivi Diversi
- Modello Predittivo Funzionante

## Setup 🖥
Per effettuare il setup del modello, bisognerà semplicemente scaricare il file __*"Hth_predict.py"*__ ed il file _***"Hth_heartTest.csv"***_. 


## Utilizzo 🖥
Per utilizzare il modello, basterà semplicemente inserire dei dati di input, se già normalizzati, e far partire lo script in Python, come da esempio:
```
 input = {
    "Age": 0.05,
    "Sex": 0,
    "ChestPainType": 1,
    "Cholesterol":35,
    "FastingBS":1,
    "MaxHR":1.38,
    "ExerciseAngina":0,
    "Oldpeak":0.3,
    "ST_Slope":2,
  }
``` 

## Project Status 👍
Il Progetto è: **_Completo_**. ✅

## Migliorie 🩺
È possibile migliorare le percentuali di accuratezza dei modelli, integrato il lavoro svolto, con un punto di vista medico/statistico.

Migliorie:
- Data Analysis con Approccio Medico 🫀

## Ringraziamenti 🙏
- Si ringraziano il Professore ed i Tutor per averci guidato lungo il percorso; 🥰
- Si ringraziano i medici per il loro riscontro sul Dataset. 🫡

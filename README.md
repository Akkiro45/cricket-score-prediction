# cricket-score-prediction
First inning score predictor for IPL, ODI, T20

## Dataset

* 1188 ODI matches -> data/odi.csv
* 1474 T-20 matches -> data/t20.csv
* 617 IPL matches -> data/ipl.csv

## Algorithms 

1. Linear Regression -> linear-ui.py
2. Random Forest Regression -> forest-ui.py

## Features and Label 

* Features: [bat_team,bowl_team,runs,wickets,overs,striker,non-striker]
* Label: [total]

## Requirements

* numpy==1.16.2
* pandas==0.24.1
* python-dateutil==2.8.0
* pytz==2018.9
* scikit-learn==0.20.3
* scipy==1.2.1
* six==1.12.0
* sklearn==0.0

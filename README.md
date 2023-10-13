# Heart Attack Prediction Risk Assessment
<img src="/Images/heart.jpg" /> <br>

## Project Overview
Heart disease or myocardial infarction remains a major global health problem that requires a deeper understanding of its precursors and possible contributing factors.
This project is based on two aspects from our dataset:
* Demographic analysis covers ages and gender <br>
* Lifestyle choices that related to heart health <br>
Develping a perdiction model and a CNN model, amiming for > 75% accuracy.

## Data Source
* [Kaggle: Heart Attack Risk Prediction Dataset](https://www.kaggle.com/datasets/iamsouravbanerjee/heart-attack-prediction-dataset) 
<img src="/Images/dataset.png" />

* [Mendeley Data: ECG Images dataset of Cardiac Patients](https://data.mendeley.com/datasets/gwbz3fsgp8/2)


## ETL Pipeline

### Extract
Data downloaded from the Kaggle source as a CSV.

### Transform
This project used Pandas to clean the data.

### Load
Making Spark SQL query based on the data and create database. Then deploy the database to Python Flask powered API.

## Visualization
* Tableau Story

## [Classification Modeling: ECG images](https://github.com/MahsaBakhtiari/ECG_image_classification)
<img src="/Images/ecg_model.png" />

## Team Member
* Mahsa Bakhtiari
* Riddhi Mistry
* Aliha Ahmed
* Wei Zhang

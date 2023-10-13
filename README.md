# Heart Attack Prediction Risk Assessment
<img src="/Images/heart.jpg" /> <br>

## Project Overview
Heart disease or myocardial infarction remains a major global health problem that requires a deeper understanding of its precursors and possible contributing factors.
This project is based on two aspects from our dataset:
* Demographic analysis covers ages and gender <br>
* Lifestyle choices that related to heart health <br>

Identifying heart defects from ECG Images with Deep Learning, amiming > 75% accuracy.

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

## [Classification Modeling: ECG Images GitHub](https://github.com/MahsaBakhtiari/ECG_image_classification)
Vision Transformer is a recent image processing deep learning model introduced that heavily uses self attention instead of convolutions for processing. This model implemented the ViT architecture with TensorFlow's Keras library and trained it on the training set split of the ECG dataset. Since this is a classification problem, this model used the `SparseCategoricalCrossEntropy` loss on the 4 input classes. To avoid overfitting, modeling also used weight decay within the `Adam` optimizer which improved the validation accuracy from 76% without weight decay to 86% with weight decay. This model also reduced the number of training epochs from 40 to 35 to address the overfitting problem in addition to weight decay.

<img src="/Images/ecg_model.png" />

## Team Member
* Mahsa Bakhtiari
* Riddhi Mistry
* Aliha Ahmed
* Wei Zhang

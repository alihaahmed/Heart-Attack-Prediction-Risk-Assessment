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

* [Mendeley Data: ECG Images dataset of Cardiac Patients](https://data.mendeley.com/datasets/gwbz3fsgp8/2) <br>

The dataset contains ECG images for the following conditons:
* Normal Heart
* Myocardial Infarction
* Abnormal Heart Beat
* Have a History of Myocardial Infraction

## ETL Pipeline

### Extract
Data downloaded from the Kaggle source as a CSV.

### Transform
This project used Pandas to clean the data.

### Load
Making Spark SQL query based on the data and create database. Then deploy the database to Python Flask powered API.

## ECG Data Processing
The original images have a resolution of 2213 x 1572. This resolution is very inefficient for deep learning processing as it quickly fills the precious GPU memory with large feature maps. In order to make the problem practical, I downsapled the images to a resolution of 182 x 256 to keep their original aspect ratio. It is important to use the correct downsampling algorithm so that the ECG lines are still visible and their tiny fluctuations are not destroyed. For this purpose I visually inspected the down sampled images and the "area" interpolation approach yielded the best results.

## [Classification Modeling: ECG Images GitHub](https://github.com/MahsaBakhtiari/ECG_image_classification)
Vision Transformer is a recent image processing deep learning model introduced that heavily uses self attention instead of convolutions for processing. This model implemented the ViT architecture with TensorFlow's Keras library and trained it on the training set split of the ECG dataset. Since this is a classification problem, this model used the `SparseCategoricalCrossEntropy` loss on the 4 input classes. To avoid overfitting, modeling also used weight decay within the `Adam` optimizer which improved the validation accuracy from 76% without weight decay to 86% with weight decay. This model also reduced the number of training epochs from 40 to 35 to address the overfitting problem in addition to weight decay.

<img src="/Images/ecg_model.png" />

## Data Analysis Visualization
* Tableau Story


## Team Member
* Mahsa Bakhtiari
* Riddhi Mistry
* Aliha Ahmed
* Wei Zhang

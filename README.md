# Diabetes Prediction using Machine Learning

## Overview

This project focuses on predicting whether a patient is diabetic based on medical and lifestyle features using machine learning techniques.

## Dataset

The dataset includes several health-related features such as:

* Age
* Blood Pressure (Systolic & Diastolic)
* Glucose level
* BMI (Body Mass Index)
* Height & Weight
* Family medical history

## Preprocessing

* Checked and confirmed no missing values
* Encoded categorical variables
* Split data into training and testing sets
* Handled class imbalance using model techniques (class weights)

## Models Used

* Random Forest
* Support Vector Machine (SVM - RBF Kernel)
* XGBoost

## Evaluation Metrics

* Accuracy
* Precision
* Recall
* F1-Score
* ROC-AUC

## Results

* Best ROC-AUC achieved by SVM (~0.80)
* Dataset is imbalanced, so recall and ROC-AUC are more reliable than accuracy

## Tools & Technologies

* Python
* Pandas
* NumPy
* Scikit-learn
* XGBoost
* Matplotlib

 Notes..

This project demonstrates practical implementation of machine learning models, comparison between algorithms, and handling imbalanced datasets in healthcare prediction.

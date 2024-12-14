# Bank-Term-Deposit-Prediction.
A predictive model for banking term deposits based on client data. Predicting client subscription to term deposits using machine learning models.

## Overview
This project aims to predict whether a client will subscribe to a term deposit based on features derived from direct marketing campaigns of a banking institution.

## Table of Contents
- [Introduction](#introduction)
- [Data Description](#data-description)
- [Exploratory Data Analysis (EDA)](#exploratory-data-analysis-eda)
- [Feature Engineering](#feature-engineering)
- [Model Building](#model-building)
- [Model Evaluation](#model-evaluation)
- [Findings and Insights](#findings-and-insights)
- [Future Work](#future-work)
- [Assessment Report](#assessment-report)
- [File Descriptions](#file-descriptions)
- [Getting Started](#getting-started)
- [Contributing](#contributing)
- [License](#license)

## Introduction
The aim of this project is to develop a predictive model for determining the likelihood of a client subscribing to a financial product, utilizing historical marketing campaign data.

## Data Description
The dataset contains both numerical and categorical variables related to customer demographics and their response to marketing campaigns.

## Exploratory Data Analysis (EDA)
The analysis includes visualizations of data distributions, missing values, and correlation between variables.

## Feature Engineering
Identified significant features that impact subscription likelihood, including age, job type, duration of contact, etc.

## Model Building
A logistic regression model was constructed using standard machine learning practices for binary classification.

## Model Evaluation
The model's performance was evaluated using accuracy, precision, recall, and F1 score metrics.

## Findings and Insights
Key features impacting client subscriptions were identified, with actionable recommendations for the marketing team provided.

## Future Work
Further enhancements could include testing additional algorithms, expanding feature sets, and optimizing model performance through hyperparameter tuning.

## Assessment Report
An assessment report detailing the analysis, methodologies, and findings of this project can be accessed [here](https://docs.google.com/document/d/1GBvXILQBgsFkdjd8mBx9gHqmGP5_sd-YgxTuHhMQmws/edit?usp=sharing).

## File Descriptions
This repository contains various resources related to a project for predicting whether a client will subscribe to a term deposit, using machine learning models and data analytics techniques.
The following files are included in this repository:
- **`.ipynb_checkpoints/`**: This folder contains Jupyter notebook checkpoints for saving progress.
- **`BankCode.ipynb`**: Jupyter notebook for initial data processing and code.
- **`BankTask.ipynb`**: Jupyter notebook for completing tasks associated with the bank term deposit analysis.
- **`Data Analytics Pathway Assessment Report.docx`**: The detailed report of the project assessment.
- **`TryTest.ipynb`**: Notebook used for testing various models and solutions during project development.
- **`app.py`**: Main Python file to run the model and user interface (if applicable).
- **`bank-additional-full.csv`**: Dataset with additional features and a larger sample of clients to analyze.
- **`bank-additional.csv`**: Shorter version of the dataset with selected features.
- **`bank-full.csv`**: Original dataset used for initial analysis.
- **`bank-names.txt`**: Text file containing the names of the features in the dataset.
- **`bank.csv`**: Another version of the dataset with base features.
- **`logistic_model.pkl`**: Saved logistic regression model for deployment.
- **`term_deposit_model.pkl`**: Saved predictive model for client subscriptions.

## Getting Started
To run this project locally:
1. Clone the repository.
   ```bash
   git clone https://github.com/yourusername/bank-term-deposit-prediction.git
2. Deployed Model
The predictive model is hosted and accessible via a Flask API. Details of the hosted application:
API Endpoint: http://127.0.0.1:5000/


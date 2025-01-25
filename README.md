# Depression Prediction Model

## Overview
This project aims to predict the likelihood of depression based on a set of numerical and categorical predictors. Using a logistic regression model, the dataset was preprocessed and analyzed, achieving an accuracy of **85%**.

### Performance:
- **Accuracy:** ![85%](https://img.shields.io/badge/Accuracy-85%25-brightgreen?style=for-the-badge)

## Dataset Details
### Initial Dataset:
- **Shape:** 27901 rows, 18 columns
- **After EDA:** 27901 rows, 14 columns

### Features:
#### Numerical Predictors:
- Age
- Academic Pressure
- Work Pressure
- CGPA
- Study Satisfaction
- Job Satisfaction

#### Categorical Predictors:
- Gender
- Sleep Duration (hrs)
- Dietary Habits
- Had Suicidal Thoughts
- Family History of Mental Illness

#### Target:
- Depression (1 = Depressed, 0 = Not Depressed)

### Dropped Columns:
- ID
- City
- Profession
- Degree

## Preprocessing
To standardize the dataset for machine learning and visualization, the following preprocessing steps were applied:
- **Gender:** Encoded as `0` (Male) and `1` (Female).
- **Sleep Duration:**
  - `0` = Less than 5 hours
  - `1` = 5-6 hours
  - `2` = 7-8 hours
  - `3` = More than 8 hours
  - `4` = Others
- **Family History of Mental Illness:** Encoded as `0` (No) and `1` (Yes).
- **Dietary Habits:**
  - `0` = Unhealthy
  - `1` = Moderate
  - `2` = Healthy
  - `3` = Others
- **Had Suicidal Thoughts:** Encoded as `0` (No) and `1` (Yes).

## Feature Engineering
The final features used for model training are:
- Age
- Academic Pressure
- Work Pressure
- CGPA
- Study Satisfaction
- Job Satisfaction
- Sleep Duration
- Dietary Habits
- Had Suicidal Thoughts
- Work/Study Hours
- Financial Stress
- Family History

## Model Details
### Algorithm:
- **Logistic Regression** ![Logistic Regression](https://img.shields.io/badge/Model-Logistic_Regression-FFD700?style=for-the-badge)

### Performance:
- Accuracy: **85%** ![85%](https://img.shields.io/badge/Accuracy-85%25-brightgreen?style=for-the-badge)

![Alt text](static\image.png)


## Tech Stack
- **Languages:** ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
- **Libraries:** 
  - ![pandas](https://img.shields.io/badge/pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
  - ![numpy](https://img.shields.io/badge/numpy-013243?style=for-the-badge&logo=numpy&logoColor=white)
  - ![matplotlib](https://img.shields.io/badge/matplotlib-003B57?style=for-the-badge&logo=matplotlib&logoColor=white)
  - ![seaborn](https://img.shields.io/badge/seaborn-009cde?style=for-the-badge&logo=seaborn&logoColor=white)
  - ![scikit-learn](https://img.shields.io/badge/scikit_learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)

## Project Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/Gul-Fatima/Student_Depression_Predictor
   ```

2. Setup venv dependencies:
   ```bash
   python -m venv venv
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Visualization
- **Stacked Bar Charts:** ![Stacked Bars](https://img.shields.io/badge/Visualization-Stacked_Bar_Charts-blue?style=for-the-badge)
- **KDE Plots:** ![KDE](https://img.shields.io/badge/Visualization-KDE_Plots-4B0082?style=for-the-badge)
- **Heatmaps:** ![Heatmap](https://img.shields.io/badge/Visualization-Heatmaps-FF6347?style=for-the-badge)

## Future Enhancements
- Incorporate additional models like Random Forest and XGBoost for comparison.
- Explore feature importance to refine predictors.
- Deploy the model using Flask or Django for real-time predictions.

## Contributions
Feel free to open issues and submit pull requests. Contributions are welcome!

## License
This project is licensed under the MIT License. ![MIT License](https://img.shields.io/badge/License-MIT-blue?style=for-the-badge)


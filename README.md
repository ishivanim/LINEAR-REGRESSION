# Linear Regression: TV Advertising Budget vs Sales

## Overview
This repository contains a simple linear regression model that analyzes the impact of TV advertising budgets on sales. The dataset includes advertising expenditures across multiple media (TV, radio, etc.) in dollars and their corresponding sales figures also in dollars.

## Dataset
### The dataset consists of:
  1) Advertising budget spent on various media (TV, Radio, Newspaper)
  2) Corresponding sales data

## Implementation

  1) The following steps were carried out in this project:
  2) Data Preprocessing: Loaded the dataset and extracted relevant features.
  3) Model Training: Built a linear regression model to predict sales based on TV advertising budget.
  4) Visualization: Plotted a regression line to visualize the relationship between TV advertising spend and sales.

## Results

  We save the intercept value and multiple weights for different advertising media to use it for further app deployment. 
  We create a different .py file and name it advertising.py where we use these intercept and weights values for our unseen data prediction.

## Usage
  To run the model:

## Clone the repository
    git clone <repo-url>
    cd <repo-folder>

## Run the script (replace with your script name)
    python linear_regression.py

    ### To run the streamlit app 
      Run following code in terminal
      streamlit run advertising.py

## Dependencies
###  Ensure you have the following libraries installed:
    pip install numpy pandas matplotlib scikit-learn

## Conclusion:
  This project demonstrates the application of linear regression in analyzing advertising impact. The findings help understand how multiple ad budgets influence sales and provide a basis for optimizing marketing expenditures.

## License
  This project is open-source and available for modification and reuse.

## Author
  Shivani Lange

# Bengluru-House-Price-Predictor (Regression Problem)

<img width="90%" src="https://user-images.githubusercontent.com/70078572/174433131-b5eac5a2-edc1-4baf-b99d-45fe80fccde9.gif">

## 1. Problem Definition

  Buying a home, especially in a city like Bengaluru, is a tricky choice. While the major factors are usually the same for all metros, there are others to be considered for the Silicon Valley of India. With its help millennial crowd, vibrant culture, great climate and a slew of job opportunities, it is difficult to ascertain the price of a house in Bengaluru.

Goal is to predict the price of houses in Banglore city based on Area, No. of BHK, No. of Bathrooms and Area in Sqft.

## 2. Data

[dataset from Kaggle](https://www.kaggle.com/datasets/amitabhajoy/bengaluru-house-price-data)

In the data set, historical house prices of Banglore city. Include things like location, total_sqft, balcony and more.

## 3. Model

I have tried Liner regression, Ridge & Lasso model and their respective scores are as follows;

"Linerregression": 0.8381860339652341
"Lasso": 0.8263029869374969
"Ridge": 0.8383227066936583


## 4. Deployment

I have used Ridge model and created webapp using flask,HTMLand bootstrap.
Deployment is done on Heroku: [Web App]([[https://house-price-predictor-banglore.herokuapp.com/](https://bangalore-home-price-predictor.herokuapp.com/)https://bangalore-home-price-predictor.herokuapp.com/]

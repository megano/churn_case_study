# Case Study - Churn Prediction

## How to Navigate This Repo
Scroll down in this README file to read about the problem, data set and our findings. See src and model folders for code used to build the model. See churn-deck for the deck we presented. 

Our verbal presentation and deck answered:
  * How we computed the target
  * Model did we chose and why
  * Alternative models we considered and why they wouldn't work
  * Performance metric we used and why
  * Based on insights from the model, actionable plans we propose to reduce churn

## Problem
Ride-sharing Company X is interested in predicting rider retention. What factors are best predictors for retention? Offer suggestions to operationalize those insights. Build a model that minimizes error and you can interpret factors that contributed to your predictions.

## Data
A sample of users who signed up in January 2014 pulled on July 1, 2014. We consider a user retained if they were “active” (i.e. took a trip) in the preceding 30 days (from the day the data was pulled). Latest day of last_trip_date is when the data was pulled.

Data Description:

  * city: city this user signed up in
  * phone: primary device for this user
  * signup_date: date of account registration; in the form `YYYYMMDD`
  * last_trip_date: the last time this user completed a trip; in the form `YYYYMMDD`
  * avg_dist: the average distance (in miles) per trip taken in the first 30 days after signup
  * avg_rating_by_driver: the rider’s average rating over all of their trips
  * avg_rating_of_driver: the rider’s average rating of their drivers over all of their trips
  * surge_pct: the percent of trips taken with surge multiplier > 1
  * avg_surge: The average surge multiplier over all of this user’s trips
  * trips_in_first_30_days: the number of trips this user took in the first 30 days after signing up
  * luxury_car_user: TRUE if the user took a luxury car in their first 30 days; FALSE otherwise
  * weekday_pct: the percent of the user’s trips occurring during a weekday

# Data Analysis

The process we followed was:
  * Exploratory analysis, cleaning, visualizations.
  * Build a predictive model to determine whether or not a user will be retained.
  * Evaluate the model
  * Identify / interpret features that are the most influential in affecting our predictions
  * Discuss the validity of our model and issues such as leakage
  * Repeat 2 - 5 until we have a satisfactory model

Findings:
Our best model was a Random Forest on polynomial data of degree 2. In absence of cost information or loss functions we chose the metrics accuracy, precision and recall. Our result was accuracy 0.77, precision 0.72 and recall 0.64. 


![ROC Curve](https://github.com/megano/churn_case_study/blob/master/img/roc-curve.png "Result")


Possible alternatives we considered were Logistic Regression, Adaboost, and KNN. 

Important features are:

![Feature Importance List](https://github.com/megano/churn_case_study/blob/master/img/feature-importance.png "Feature Importance")

Our actionable recommendations are:
  * Surge % has a bigger impact than # times surged -> Try fewer but higher surges
  * iPhone churn less -> Try improving android app experience
  * People who take a luxury car churn less -> Try promos for luxury car rides
  * People who ride more in 30 days churn less -> Try promos, ads for 1st 30 days
  * Avg rating BY > OF driver. -> Match riders scored low w/drivers w/high scores, pre-drop off hide passenger ratings from drivers, hide aggregate passenger rating from users, only show most recent ride score. 

Visualizations we generated:
![Various Plots](https://github.com/megano/churn_case_study/blob/master/img/more-plots.png "Visually Check the Data")
![Metrics by City](https://github.com/megano/churn_case_study/blob/master/img/metrics_by_city.jpg "Metrics by City")
![Feature Importance List1](https://github.com/megano/churn_case_study/blob/master/img/feature-importance1.png "Feature Importance")

## Future Analysis
Data we’d like to analyze:
  * Number of declined rides
  * Individual trip data per user including each ride’s cost
  * All rider’s data for multiple yrs (currently have 6 months of aggregate data from Jan sign ups)
  * A list of changes (with dates) for rider and passenger interfaces
  * Additional biz info for ex: cost benefit tradeoffs, profit curves
  * More info on ratings. Maybe a rider w/ low score is assigned worse drivers?  

# Case Study - Churn Prediction

# Problem
Ride-sharing Company X is interested in predicting rider retention. What factors are best predictors for retention? Offer suggestions to operationalize those insights. Build a model that minimizes error and you can interpret factors that contributed to your predictions.

# Data
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

# Data Analysis Work Flow

Analysis Process:
  * Exploratory analysis, cleaning, visualizations.
  * Build a predictive model to determine whether or not a user will be retained.
  * Evaluate the model
  * Identify / interpret features that are the most influential in affecting our predictions
  * Discuss the validity of our model and issues such as leakage
  * Repeat 2 - 5 until we have a satisfactory model

Deliverables
Code used to build the model
Verbal presentation including:
  * How did you compute the target?
  * What model did you use in the end? Why?
  * Alternative models you considered? Why are they not good enough?
  * What performance metric did you use? Why?
  * Based on insights from the model, what actionable plans do you propose to reduce churn?

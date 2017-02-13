library(rpart) # For regression tree
library(rpart.plot) # for plotting the regression tree
library(hydroGOF) # For statistical metrics (MAE, MSE, and RMSE)

# Setting the working directory
setwd("D:/Users/Miller/OneDrive - DePaul University/B2W/BW2 Labs Pricing Challenge/BW2_Labs-Pricing_Challenge/Scripts")





##### Preprocessing data

# Reading correlated data from file
correlated=read.table("dataset/correlated_data.csv", header=T, sep=';')

# Keeping only the data about P3
correlated = correlated[correlated$PROD_ID == "P3",]

# Converting Variable as Date type
tempDate = correlated$DATE
correlated$DATE = as.Date(tempDate)

# Removing data that do not have competitors' price monitoring
correlated = correlated[correlated$DATE >= "2015-03-15",]

# # Adding variable day of week in the dataset
# correlated$DAY_OF_WEEK = weekdays(correlated$DATE)

# Removing SALES_COUNT outliers
outliers <- boxplot.stats(correlated$SALES_COUNT)$out

for (i in 1:length(outliers)){
  correlated = correlated[correlated$SALES_COUNT != outliers[i],]
}




# Setting a list of variables to be removed from the data set
# Removing variables that are less informative for prediction
# listvar = c()
# listvar = c("C5_PRICE_1", "C5_PRICE_2", "MEDIAN_PRICE")
# listvar = c("C5_PRICE_1", "C5_PRICE_2", "MEDIAN_PRICE", "DATE")
listvar = c("C5_PRICE_1", "C5_PRICE_2", "MEDIAN_PRICE", "DATE")
correlated.pred = correlated[!(names(correlated) %in% listvar)]




##### Sampling data randomly for training and validation

# Random seed
set.seed(2802)

# Setting 80% of the data for training and 20% for validation
train.size=round(0.80*nrow(correlated.pred))

# Random sampling
id.train = sample(1:nrow(correlated.pred), train.size, replace=FALSE)
correlated.train = correlated.pred[id.train,]
correlated.val= correlated.pred[-id.train,]





##### Regression Tree for prediction
# Training regression tree
dtree = rpart(SALES_COUNT~., data=correlated.train, method="anova", parms=list(split="gini"))

# Plotting regression tree
prp(dtree, type=4,fallen.leaves=FALSE, main="Regression Tree for P3", faclen=0)

# Plotting a barplot that shows the importance of each variable for the prediction
barplot(dtree$variable.importance)

# Predicting SALES_COUNT from validation set using the regression tree
dtree.pred = predict(dtree, newdata=correlated.val, type="vector")

# Evaluating predictions using MAE, MSE, and RMSE
mse_val = mse(dtree.pred, correlated.val$SALES_COUNT)
mse_val
rmse_val = rmse(dtree.pred, correlated.val$SALES_COUNT)
rmse_val
mae_val = mae(dtree.pred, correlated.val$SALES_COUNT)
mae_val

# Creating a dataframe to look to the observed and predicted values
predicted_vector = data.frame(correlated.val$SALES_COUNT, dtree.pred)
colnames(predicted_vector) <- c("Observed", "Predicted")

# Write CSV in R
write.table(predicted_vector, file = "predictions/regression_tree_P3.csv",row.names=FALSE, na="",col.names=TRUE, sep=";")

summary(correlated$SALES_COUNT)


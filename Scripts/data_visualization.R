# Setting the working directory
setwd("D:/Users/Miller/OneDrive - DePaul University/B2W/BW2 Labs Pricing Challenge/BW2_Labs-Pricing_Challenge/Scripts")

# Reading sales data from file
sales=read.table("dataset/ordered_sales.csv", header=T, sep=';')

# Reading competitors' prices from file 
cprices=read.table("dataset/ordered_comp_prices_nmv.csv", header=T, sep=';')

summary(sales[sales$prod_id=="P2",])
summary(cprices)

describe(sales)
describe(cprices)


# Separating dataset per products
cprices.p1 = cprices[cprices$prod_id=="P1",]
cprices.p2 = cprices[cprices$prod_id=="P2",]
cprices.p3 = cprices[cprices$prod_id=="P3",]
cprices.p4 = cprices[cprices$prod_id=="P4",]
cprices.p5 = cprices[cprices$prod_id=="P5",]
cprices.p6 = cprices[cprices$prod_id=="P6",]
cprices.p7 = cprices[cprices$prod_id=="P7",]
cprices.p8 = cprices[cprices$prod_id=="P8",]
cprices.p9 = cprices[cprices$prod_id=="P9",]


summary(cprices.p1)
summary(cprices.p2)
summary(cprices.p3)
summary(cprices.p4)
summary(cprices.p5)
summary(cprices.p6)
summary(cprices.p7)
summary(cprices.p8)
summary(cprices.p9)


boxplot(cprices.p1$price~cprices.p1$comp, ylab="Price", xlab="Competitor", main="Competitors Price for P1")
boxplot(cprices.p2$price~cprices.p2$comp, ylab="Price", xlab="Competitor", main="Competitors Price for P2")
boxplot(cprices.p3$price~cprices.p3$comp, ylab="Price", xlab="Competitor", main="Competitors Price for P3")
boxplot(cprices.p4$price~cprices.p4$comp, ylab="Price", xlab="Competitor", main="Competitors Price for P4")
boxplot(cprices.p5$price~cprices.p5$comp, ylab="Price", xlab="Competitor", main="Competitors Price for P5")
boxplot(cprices.p6$price~cprices.p6$comp, ylab="Price", xlab="Competitor", main="Competitors Price for P6")
boxplot(cprices.p7$price~cprices.p7$comp, ylab="Price", xlab="Competitor", main="Competitors Price for P7")
boxplot(cprices.p8$price~cprices.p8$comp, ylab="Price", xlab="Competitor", main="Competitors Price for P8")
boxplot(cprices.p9$price~cprices.p9$comp, ylab="Price", xlab="Competitor", main="Competitors Price for P9")



sales.p1 = sales[sales$prod_id=="P1",]
sales.p2 = sales[sales$prod_id=="P2",]
sales.p3 = sales[sales$prod_id=="P3",]
sales.p4 = sales[sales$prod_id=="P4",]
sales.p5 = sales[sales$prod_id=="P5",]
sales.p6 = sales[sales$prod_id=="P6",]
sales.p7 = sales[sales$prod_id=="P7",]
sales.p8 = sales[sales$prod_id=="P8",]
sales.p9 = sales[sales$prod_id=="P9",]

summary(sales.p1)
summary(sales.p2)
summary(sales.p3)
summary(sales.p4)
summary(sales.p5)
summary(sales.p6)
summary(sales.p7)
summary(sales.p8)
summary(sales.p9)

boxplot(sales.p1$count)
boxplot(sales.p2$count)
boxplot(sales.p3$count)
boxplot(sales.p4$count)
boxplot(sales.p5$count)
boxplot(sales.p6$count)
boxplot(sales.p7$count)
boxplot(sales.p8$count)
boxplot(sales.p9$count)




boxplot(cprices$price~cprices$comp*cprices$prod_id, ylab="Price", xlab="Competitor.Product", main="Competitors Price")
boxplot(sales$count~sales$prod_id, ylab="Number of Sales", xlab="Product", main="Quantity Sold")


# Reading correlated data from file
correlated=read.table("dataset/correlated_data.csv", header=T, sep=';')

outliers <- boxplot.stats(correlated$SALES_COUNT[correlated$PROD_ID == "P1"])$out
for (i in 1:length(outliers)){
  correlated = correlated[correlated$SALES_COUNT != outliers[i],]
}

outliers <- boxplot.stats(correlated$SALES_COUNT[correlated$PROD_ID == "P2"])$out
for (i in 1:length(outliers)){
  correlated = correlated[correlated$SALES_COUNT != outliers[i],]
}

outliers <- boxplot.stats(correlated$SALES_COUNT[correlated$PROD_ID == "P3"])$out
for (i in 1:length(outliers)){
  correlated = correlated[correlated$SALES_COUNT != outliers[i],]
}

outliers <- boxplot.stats(correlated$SALES_COUNT[correlated$PROD_ID == "P4"])$out
for (i in 1:length(outliers)){
  correlated = correlated[correlated$SALES_COUNT != outliers[i],]
}

outliers <- boxplot.stats(correlated$SALES_COUNT[correlated$PROD_ID == "P5"])$out
for (i in 1:length(outliers)){
  correlated = correlated[correlated$SALES_COUNT != outliers[i],]
}

outliers <- boxplot.stats(correlated$SALES_COUNT[correlated$PROD_ID == "P6"])$out
for (i in 1:length(outliers)){
  correlated = correlated[correlated$SALES_COUNT != outliers[i],]
}

outliers <- boxplot.stats(correlated$SALES_COUNT[correlated$PROD_ID == "P7"])$out
for (i in 1:length(outliers)){
  correlated = correlated[correlated$SALES_COUNT != outliers[i],]
}

outliers <- boxplot.stats(correlated$SALES_COUNT[correlated$PROD_ID == "P8"])$out
for (i in 1:length(outliers)){
  correlated = correlated[correlated$SALES_COUNT != outliers[i],]
}

outliers <- boxplot.stats(correlated$SALES_COUNT[correlated$PROD_ID == "P9"])$out
for (i in 1:length(outliers)){
  correlated = correlated[correlated$SALES_COUNT != outliers[i],]
}

boxplot(correlated$SALES_COUNT~correlated$PROD_ID, ylab="Number of Sales", xlab="Product", main="Quantity Sold")



#-------------------------------------------------------------------------------------
	# preprocessing_sales -- script to organize sales data
	#
	# Author: Miller Horvath
	#
	# Purpose: B2W Labs | Pricing Challenge
#-------------------------------------------------------------------------------------

import os
import cPickle as cpkl

#---- Reading data -------------------------------------------------------------------

# Opening the sales file
f = open(os.path.join('dataset', 'sales.csv'), 'r')

# Skipping the first line of the file (header)
f.readline()
# Reading sales data from file 
sales = f.readlines()

# Closing the sales file
f.close()



#---- Organizing data ----------------------------------------------------------------

# Dictonary used to organize sales by PROD_ID, DATE_ORDER and price.
split_sales = dict()

# For each sale
for line in sales:
	# Separating values in a list
	s = line.split(',')

	# Organizing sale information
	prod_id = int(s[0][1])
	date = s[1]
	qty = int(float(s[2]))
	revenue = float(s[3])
	unity_price = revenue/qty

	# Creating a dictionary for the first ocurrence of each prod_id
	if prod_id not in split_sales:
		split_sales[prod_id] = dict()

	# Creating a list for the first ocurrence of each prod_id date order
	if date not in split_sales[prod_id]:
		split_sales[prod_id][date] = dict()

	# Creating a list for the first ocurrence of each prod_id date order
	if unity_price not in split_sales[prod_id][date]:
		split_sales[prod_id][date][unity_price] = 0

	# Pushing the sale info in the data structure
	split_sales[prod_id][date][unity_price] += qty



#---- Saving ordered file for vizualization purposes ---------------------------------

f = open(os.path.join("dataset","ordered_sales.csv"), "w")

f.write("prod_id;date;price;count\n")

for prod_id in sorted(split_sales.keys()):
	for date in sorted(split_sales[prod_id].keys()):
		for price in sorted(split_sales[prod_id][date].keys()):
			qty = split_sales[prod_id][date][price]
			f.write("P{};{};{};{}\n".format(prod_id, date, price, qty))

f.close()

#---- Computing statistical info -----------------------------------------------------

# Loop to compute sales per day and median of daily prices
for prod_id in split_sales.keys():
	for date in split_sales[prod_id].keys():
		sales_count = 0
		sales_mean = 0.0

		# Counting the number of sales
		for price in split_sales[prod_id][date].keys():
			qty = split_sales[prod_id][date][price]
			sales_count += qty
			sales_mean = sales_mean + (qty * price)

		sales_mean = round((sales_mean / sales_count), 2)
		sales_median = 0
		temp_count = 0

		# Computing median price value
		for price in sorted( split_sales[prod_id][date].keys() ):
			temp_count += split_sales[prod_id][date][price]
			sales_median = price

			if temp_count >= (sales_count / 2):
				break

		# Modifying dictonarie to store the meaningful values
		split_sales[prod_id][date] = [sales_count, sales_median, sales_mean]



#---- Saving statistical info on disk ------------------------------------------------

# It creates the "dicts" folder if it doesn't exist
if not os.path.exists("dicts"):
    os.makedirs("dicts")

# Save dict on disk
f = open(os.path.join("dicts","dict_sales.pkl"), "wb")
cpkl.dump(split_sales, f)
f.close()

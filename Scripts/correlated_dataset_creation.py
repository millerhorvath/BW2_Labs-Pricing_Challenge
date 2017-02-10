#-------------------------------------------------------------------------------------
	# correlated_dataset_creation -- script that creates a CSV file that contains all
	#    the preprocessed data and some correlation between data that may be
	#    meaningful to the prediction model.
	#
	# Author: Miller Horvath
	#
	# Purpose: B2W Labs | Pricing Challenge
#-------------------------------------------------------------------------------------

import os
import cPickle as cpkl

#---- Loading dicts from file --------------------------------------------------------

f = open(os.path.join("dicts","dict_sales.pkl"), "rb")
sales = cpkl.load(f)
f.close()

f = open(os.path.join("dicts","dict_comp_prices.pkl"), "rb")
comp = cpkl.load(f)
f.close()

#---- Writing data on a CSV file ------------------------------------------------------

# Opening file
f = open(os.path.join("dataset","correlated_data.csv"), "w")

# Writing file header
# f.write("PROD_ID;DATE;SALES_COUNT;MEDIAN_PRICE;MEAN_PRICE;C1_PRICE_1;C1_PAY_TYPE_1;C1_EX_TIME_1;C1_PRICE_2;C1_PAY_TYPE_2;C1_EX_TIME_2;C2_PRICE_1;C2_PAY_TYPE_1;C2_EX_TIME_1;C2_PRICE_2;C2_PAY_TYPE_2;C2_EX_TIME_2;C3_PRICE_1;C3_PAY_TYPE_1;C3_EX_TIME_1;C3_PRICE_2;C3_PAY_TYPE_2;C3_EX_TIME_2;C4_PRICE_1;C4_PAY_TYPE_1;C4_EX_TIME_1;C4_PRICE_2;C4_PAY_TYPE_2;C4_EX_TIME_2;C5_PRICE_1;C5_PAY_TYPE_1;C5_EX_TIME_1;C5_PRICE_2;C5_PAY_TYPE_2;C5_EX_TIME_2;C6_PRICE_1;C6_PAY_TYPE_1;C6_EX_TIME_1;C6_PRICE_2;C6_PAY_TYPE_2;C6_EX_TIME_2\n")
f.write("PROD_ID;DATE;SALES_COUNT;MEDIAN_PRICE;MEAN_PRICE;C1_PRICE_1;C1_PRICE_2;C2_PRICE_1;C2_PRICE_2;C3_PRICE_1;C3_PRICE_2;C4_PRICE_1;C4_PRICE_2;C5_PRICE_1;C5_PRICE_2;C6_PRICE_1;C6_PRICE_2\n")

for prod in sales.keys():
	for date in sales[prod].keys():
		sales_count = sales[prod][date][0]
		median_price = sales[prod][date][1]
		mean_price = sales[prod][date][2]
		f.write("P{};{};{};{};{}".format(prod, date, sales_count, median_price, mean_price))

		for c in range(1, 7):
			for i in range(1,3):
				try:
					cprice = comp[prod][date][c][i]
				except:
					cprice = "NA"

				f.write(";{}".format(cprice))
		f.write("\n")

f.close()
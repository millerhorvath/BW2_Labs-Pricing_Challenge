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

f = open(os.path.join("dicts","dict_comp_prices_nmv.pkl"), "rb")
comp_nmv = cpkl.load(f)
f.close()



#---- Writing data on a CSV file ------------------------------------------------------

# Opening file
f = open(os.path.join("dataset","correlated_data.csv"), "w")

# Writing file header
f.write("PROD_ID;DATE;SALES_COUNT;MEDIAN_PRICE;MEAN_PRICE;C1_PRICE_1;C1_PRICE_2;C2_PRICE_1;C2_PRICE_2;C3_PRICE_1;C3_PRICE_2;C4_PRICE_1;C4_PRICE_2;C5_PRICE_1;C5_PRICE_2;C6_PRICE_1;C6_PRICE_2\n")

for prod in sorted(sales.keys()):
	for date in sorted(sales[prod].keys()):
		sales_count = sales[prod][date][0]
		median_price = sales[prod][date][1]
		mean_price = sales[prod][date][2]
		f.write("P{};{};{};{};{}".format(prod, date, sales_count, median_price, mean_price))

		for c in range(1, 7):
			for i in range(1,3):
				try:
					cprice = comp[prod][c][i][date]
				except:
					cprice = "NA"

				f.write(";{}".format(cprice))
		f.write("\n")

f.close()



#---- Writing data on a CSV file for no missing values file ---------------------------

# Opening file
f = open(os.path.join("dataset","correlated_data_nmv.csv"), "w")

# Writing file header
f.write("PROD_ID;DATE;SALES_COUNT;MEDIAN_PRICE;MEAN_PRICE;C1_PRICE_1;C1_PRICE_2;C2_PRICE_1;C2_PRICE_2;C3_PRICE_1;C3_PRICE_2;C4_PRICE_1;C4_PRICE_2;C5_PRICE_1;C5_PRICE_2;C6_PRICE_1;C6_PRICE_2\n")

for prod in sorted(sales.keys()):
	for date in sorted(sales[prod].keys()):
		sales_count = sales[prod][date][0]
		median_price = sales[prod][date][1]
		mean_price = sales[prod][date][2]
		f.write("P{};{};{};{};{}".format(prod, date, sales_count, median_price, mean_price))

		for c in range(1, 7):
			for i in range(1,3):
				try:
					cprice = comp_nmv[prod][c][i][date]
				except:
					cprice = "NA"

				f.write(";{}".format(cprice))
		f.write("\n")

f.close()



#---- Creating a correlated file considering difference of prices ---------------------

# Opening file
f = open(os.path.join("dataset","correlated_data_diff.csv"), "w")

# Writing file header
f.write("PROD_ID;DATE;SALES_COUNT;MEDIAN_PRICE;C1_DIFF_1;C1_DIFF_2;C2_DIFF_1;C2_DIFF_2;C3_DIFF_1;C3_DIFF_2;C4_DIFF_1;C4_DIFF_2;C5_DIFF_1;C5_DIFF_2;C6_DIFF_1;C6_DIFF_2\n")

for prod in sorted(sales.keys()):
	for date in sorted(sales[prod].keys()):
		sales_count = sales[prod][date][0]
		median_price = sales[prod][date][1]
		mean_price = sales[prod][date][2]
		f.write("P{};{};{};{}".format(prod, date, sales_count, median_price))

		for c in range(1, 7):
			for i in range(1,3):
				try:
					cprice = median_price - comp[prod][c][i][date]
				except:
					cprice = "NA"

				f.write(";{}".format(cprice))
		f.write("\n")

f.close()



#---- Creating a correlated file considering difference of prices ---------------------

# Opening file
f = open(os.path.join("dataset","correlated_data_diff_nmv.csv"), "w")

# Writing file header
f.write("PROD_ID;DATE;SALES_COUNT;MEDIAN_PRICE;C1_DIFF_1;C1_DIFF_2;C2_DIFF_1;C2_DIFF_2;C3_DIFF_1;C3_DIFF_2;C4_DIFF_1;C4_DIFF_2;C5_DIFF_1;C5_DIFF_2;C6_DIFF_1;C6_DIFF_2\n")

for prod in sorted(sales.keys()):
	for date in sorted(sales[prod].keys()):
		sales_count = sales[prod][date][0]
		median_price = sales[prod][date][1]
		mean_price = sales[prod][date][2]
		f.write("P{};{};{};{}".format(prod, date, sales_count, median_price))

		for c in range(1, 7):
			for i in range(1,3):
				try:
					cprice = median_price - comp_nmv[prod][c][i][date]
				except:
					cprice = "NA"

				f.write(";{}".format(cprice))
		f.write("\n")

f.close()

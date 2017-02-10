#--------------------------------------------------------------------------------------
	# preprocessing_comp_prices -- script to organize competitors prices data
	#
	# Author: Miller Horvath
	#
	# Purpose: B2W Labs | Pricing Challenge
#--------------------------------------------------------------------------------------

import os
import cPickle as cpkl

#---- Reading data -------------------------------------------------------------------

# Opening the competitors' prices file
f = open(os.path.join('dataset', 'comp_prices.csv'), 'r')

# Skipping the first line of the file (header)
f.readline()
# Reading sales data from file 
cprices = f.readlines()

#Closing the competitors's prices file
f.close()

#---- Organizing data ----------------------------------------------------------------

# Dictonary used to organize competitors prices by PROD_ID, DATE_EXTRACTION,
# COMPETITOR_PRICE and PAT_TYPE.
comp_prices = dict()

for line in cprices:
	# Separating values in a list
	cp = line.split(',')

	# Organizing competitor's price information
	prod_id = int(cp[0][1])
	date = cp[1][0:10]
	time = cp[1][11:]
	comp = int(cp[2][1])
	price = float(cp[3])
	pay_type = int(cp[4])

	# Creating a dictionary for the first ocurrence of each prod_id
	if prod_id not in comp_prices:
		comp_prices[prod_id] = dict()

	# Creating a list for the first ocurrence of each prod_id date order
	if date not in comp_prices[prod_id]:
		comp_prices[prod_id][date] = dict()

	# Creating a list for the first ocurrence of each prod_id date order
	if comp not in comp_prices[prod_id][date]:
		comp_prices[prod_id][date][comp] = list()

	# Pushing the price monitoring info in the data structure
	comp_prices[prod_id][date][comp].append([time, price, pay_type])



#---- Saving statistical info on disk ------------------------------------------------

# It creates the "dicts" folder if it doesn't exist
if not os.path.exists("dicts"):
    os.makedirs("dicts")

# Save dict on disk
f = open(os.path.join("dicts","dict_comp_prices.pkl"), "wb")
cpkl.dump(comp_prices, f)
f.close()

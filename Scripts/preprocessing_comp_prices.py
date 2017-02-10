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
		comp_prices[prod_id][date][comp] = dict()

	# Creating a list for the first ocurrence of each prod_id date order
	if pay_type not in comp_prices[prod_id][date][comp]:
		comp_prices[prod_id][date][comp][pay_type] = dict()

	# Pushing the price monitoring info in the data structure
	comp_prices[prod_id][date][comp][pay_type][time] = price



#---- Saving ordered file for vizualization purposes ---------------------------------

f = open(os.path.join("dataset","ordered_comp_prices.csv"), "w")

f.write("prod_id;date;comp;time;price;pay_type\n")

for prod_id in sorted(comp_prices.keys()):
	for date in sorted(comp_prices[prod_id].keys()):
		for comp in sorted(comp_prices[prod_id][date].keys()):
			for pay_type in sorted(comp_prices[prod_id][date][comp].keys()):
				for time in sorted(comp_prices[prod_id][date][comp][pay_type].keys()):
					price = comp_prices[prod_id][date][comp][pay_type][time]
					f.write("P{};{};C{};{};{};PT{}\n".format(prod_id, date,comp, time,
						price, pay_type))

f.close()



#---- Computing the mean price of day ------------------------------------------------

for prod_id in comp_prices.keys():
	for date in comp_prices[prod_id].keys():
		for comp in comp_prices[prod_id][date].keys():
			for pay_type in comp_prices[prod_id][date][comp].keys():
				mean_price = 0.0
				count_flag = 0
				for time in comp_prices[prod_id][date][comp][pay_type].keys():
					price = comp_prices[prod_id][date][comp][pay_type][time]
					mean_price += price
					count_flag += 1
				mean_price = round((mean_price / count_flag), 2)
				comp_prices[prod_id][date][comp][pay_type] = mean_price
				



f = open(os.path.join("dataset","temp.csv"), "w")

f.write("prod_id;comp;date;time;pay_type;price\n")

for prod_id in sorted(comp_prices.keys()):
	for date in sorted(comp_prices[prod_id].keys()):
		for comp in sorted(comp_prices[prod_id][date].keys()):
			for pay_type in sorted(comp_prices[prod_id][date][comp].keys()):
				price = comp_prices[prod_id][date][comp][pay_type]
				f.write("{};{};{};{};{};{}\n".format(prod_id, comp, date, time,
						pay_type, price))

f.close()


#---- Saving statistical info on disk ------------------------------------------------

# It creates the "dicts" folder if it doesn't exist
if not os.path.exists("dicts"):
    os.makedirs("dicts")

# Save dict on disk
f = open(os.path.join("dicts","dict_comp_prices.pkl"), "wb")
cpkl.dump(comp_prices, f)
f.close()
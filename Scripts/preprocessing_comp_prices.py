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

# Dictonary of competitors prices without missing values
comp_prices_nmv = dict()

all_dates = dict()
all_prod_id = dict()
all_comp = dict()

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

	# Auxiliary variables used to fill in missing values of competitors price
	# monitoring
	all_dates[date] = 1
	all_comp[comp] = 1
	all_prod_id[prod_id] = 1

	# Creating a dictionary for the first ocurrence of each prod_id
	if prod_id not in comp_prices:
		comp_prices[prod_id] = dict()
		comp_prices_nmv[prod_id] = dict()

	# Creating a list for the first ocurrence of each prod_id date order
	if comp not in comp_prices[prod_id]:
		comp_prices[prod_id][comp] = dict()
		comp_prices_nmv[prod_id][comp] = dict()

	# Creating a list for the first ocurrence of each prod_id date order
	if pay_type not in comp_prices[prod_id][comp]:
		comp_prices[prod_id][comp][pay_type] = dict()
		comp_prices_nmv[prod_id][comp][pay_type] = dict()

	# Creating a list for the first ocurrence of each prod_id date order
	if date not in comp_prices[prod_id][comp][pay_type]:
		comp_prices[prod_id][comp][pay_type][date] = list()
		comp_prices_nmv[prod_id][comp][pay_type][date] = list()

	# Pushing the price monitoring info in the data structure
	# Avoiding outliers caused by mistakes on price monitoring
	if(price < 5000.0):
		comp_prices[prod_id][comp][pay_type][date].append((time, price))
		comp_prices_nmv[prod_id][comp][pay_type][date].append((time, price))



#---- Saving ordered file for vizualization purposes ---------------------------------

f = open(os.path.join("dataset","ordered_comp_prices.csv"), "w")

f.write("prod_id;comp;date;time;price;pay_type\n")

for prod_id in sorted(comp_prices.keys()):
	for comp in sorted(comp_prices[prod_id].keys()):
		for pay_type in sorted(comp_prices[prod_id][comp].keys()):
			for date in sorted(comp_prices[prod_id][comp][pay_type].keys()):
				comp_prices[prod_id][comp][pay_type][date].sort()

				for item in comp_prices[prod_id][comp][pay_type][date]:
					time = item[0]
					price = item[1]

					f.write("P{};C{};{};{};{};PT{}\n".format(prod_id, comp, date, time,
						price, pay_type))

f.close()



#---- Filling in missing values of competitors price ---------------------------------

# Sorting list to use as indexes
all_dates = sorted(all_dates.keys())
all_comp = sorted(all_comp.keys())
all_prod_id = sorted(all_prod_id.keys())

# Loop that will assigned the last known competitor price to the missing values
for pay_type in range(1, 3):
	for i in range(len(all_comp)):
		for j in range(len(all_prod_id)):
			for k in range(len(all_dates)):
				comp = all_comp[i]
				prod_id = all_prod_id[j]
				date = all_dates[k]

				if comp_prices_nmv[prod_id].has_key(comp) and comp_prices_nmv[prod_id][comp].has_key(pay_type):
					if comp_prices_nmv[prod_id][comp][pay_type].has_key(date) == False:
						l = k-1
						
						while l >= 0 and comp_prices_nmv[prod_id][comp][pay_type].has_key(all_dates[l]) == False:
							l -= 1
						
						if l >= 0:
							o_date = all_dates[l]
							if type(comp_prices_nmv[prod_id][comp][pay_type][o_date]) == type(1.1):
								comp_prices_nmv[prod_id][comp][pay_type][date] = comp_prices_nmv[prod_id][comp][pay_type][o_date]
							else:
								comp_prices_nmv[prod_id][comp][pay_type][date] = comp_prices_nmv[prod_id][comp][pay_type][o_date][-1][1]
						# else:
						# 	l = k+1
						
						# 	while l < len(all_dates) and comp_prices_nmv[prod_id][comp][pay_type].has_key(all_dates[l]) == False:
						# 		l += 1

						# 	if l < len(all_dates):
						# 		o_date = all_dates[l]
						# 		if type(comp_prices_nmv[prod_id][comp][pay_type][o_date]) == type(1.1):
						# 			comp_prices_nmv[prod_id][comp][pay_type][date] = comp_prices_nmv[prod_id][comp][pay_type][o_date]
						# 		else:
						# 			comp_prices_nmv[prod_id][comp][pay_type][date] = comp_prices_nmv[prod_id][comp][pay_type][o_date][-1][1]
						# 	else:
						# 		raise Exception



#---- Saving ordered file without missing values for vizualization purposes ----------

f = open(os.path.join("dataset","ordered_comp_prices_nmv.csv"), "w")

f.write("prod_id;comp;date;time;price;pay_type\n")

for prod_id in sorted(comp_prices_nmv.keys()):
	for comp in sorted(comp_prices_nmv[prod_id].keys()):
		for pay_type in sorted(comp_prices_nmv[prod_id][comp].keys()):
			for date in sorted(comp_prices_nmv[prod_id][comp][pay_type].keys()):
				if type(comp_prices_nmv[prod_id][comp][pay_type][date]) == type(list()):
					comp_prices_nmv[prod_id][comp][pay_type][date].sort()

					for item in comp_prices_nmv[prod_id][comp][pay_type][date]:
						time = item[0]
						price = item[1]
						
						f.write("P{};C{};{};{};{};PT{}\n".format(prod_id, comp, date, time,
							price, pay_type))
				else:
					time = 0
					price = comp_prices_nmv[prod_id][comp][pay_type][date]
					
					f.write("P{};C{};{};{};{};PT{}\n".format(prod_id, comp, date, time,
						price, pay_type))


f.close()



#---- Computing the mean price of day ------------------------------------------------

for prod_id in comp_prices_nmv.keys():
	for comp in comp_prices_nmv[prod_id].keys():
		for pay_type in comp_prices_nmv[prod_id][comp].keys():
			for date in comp_prices_nmv[prod_id][comp][pay_type].keys():
				
				mean_price = 0.0
				count_flag = 0
				if type(comp_prices_nmv[prod_id][comp][pay_type][date]) == type(list()):
					for item in comp_prices_nmv[prod_id][comp][pay_type][date]:
						price = item[1]
						mean_price += price
						count_flag += 1
					mean_price = round((mean_price / count_flag), 2)
				else:
					mean_price = comp_prices_nmv[prod_id][comp][pay_type][date]

				comp_prices_nmv[prod_id][comp][pay_type][date] = mean_price
				
				try:
					mean_price = 0.0
					count_flag = 0
					for item in comp_prices[prod_id][comp][pay_type][date]:
						price = item[1]
						mean_price += price
						count_flag += 1
					mean_price = round((mean_price / count_flag), 2)
					comp_prices[prod_id][comp][pay_type][date] = mean_price
				except:
					pass



#---- Saving dictionaries info on disk -----------------------------------------------

# It creates the "dicts" folder if it doesn't exist
if not os.path.exists("dicts"):
    os.makedirs("dicts")

# Save dict on disk
f = open(os.path.join("dicts","dict_comp_prices.pkl"), "wb")
cpkl.dump(comp_prices, f)
f.close()

# Save dict with no missing values on disk
f = open(os.path.join("dicts","dict_comp_prices_nmv.pkl"), "wb")
cpkl.dump(comp_prices_nmv, f)
f.close()
def check_products(range_tuples, product_ids):
	fresh = []
	unfresh = []

	for product_id in product_ids:
		
		#grab ranges where range_max > product_id
		plausible = [range for range in range_tuples if int(range[1]) >= int(product_id)]

		#then check those ranges to see if range_min < product_id
		confirmed = [range for range in plausible if int(range[0]) <= int(product_id)]

		if len(confirmed):
			fresh.append(product_id)
		else:
			unfresh.append(product_id)

	return fresh, unfresh

if __name__ == "__main__":

    #read in input
	with open("9-input.txt", "r") as f:
		data = f.read()
	
	ranges, products = data.split("\n\n")
	ranges = [range.split("-") for range in ranges.split("\n")]
	products = products.split("\n")[:-1] #knock off that final \n

	fresh, unfresh = check_products(ranges, products)


	print(len(fresh), len(unfresh))
	
	

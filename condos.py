class Condo(object):

	condo_insurance = 50

	def __init__(self, price, monthly_mortgage, squarefootage, maintenance, tax, rent, locker = False):
		self.price = price
		self.monthly_mortgage = monthly_mortgage
		self.squarefootage = squarefootage
		self.maintenance = maintenance
		self.tax = tax
		self.rent = rent
		self.locker	= locker

	def monthly_fees(self):
		total_fees = self.maintenance + (self.tax/12) + self.monthly_mortgage + self.condo_insurance
		print "Your condo's total monthly fee will be ${fees} \n".format(fees = total_fees)

	def print_condo(self):
		print "Here are the condo's specifications:", '\n'*2 , \
	    "Price:", self.price, '\n', \
	    "Monthly Mortgage Payment:", self.monthly_mortgage, '\n', \
	    "Square Footage:", self.squarefootage, '\n', \
        "Maintenance Fee:", self.maintenance, '\n', \
	    "Tax:", self.tax, '\n', \
	    "Rent:", self.rent, '\n', \
	    "Includes Locker:", self.locker, '\n' 

duke_of_york = Condo(price = 487000, monthly_mortgage = 1881.96, squarefootage = 937, maintenance = 608, tax = 2792.31, rent = 2200, locker = True)
duke_of_york.monthly_fees()
duke_of_york.print_condo()

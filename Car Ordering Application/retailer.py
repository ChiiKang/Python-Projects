import random

class Retailer:
	"""
	A class contains all operations related to a retailer
	"""

	# Class Variables
	retailer_list = []

	def __init__(self, retailer_name):
		"""
		Constructs retailer object

		Parameters
		----------
		retailer_id : int (8 digits)
		retailer_name : str

		"""
		self.retailer_id = self.generate_retailer_id(Retailer.retailer_list)
		self.retailer_name = retailer_name

	# Construct a formatted car string
	def __str__(self):
		"""
		Generate string of retailer object

		Parameters
		----------
		None

		Returns
		----------
		str
		"""
		return f"{self.retailer_id}, {self.retailer_name}"

	def generate_retailer_id(self, list_retailer):
		"""
		Generate random 8 digits ID different from existing retailer ID

		Parameters
		----------
		list_retailer: list

		Returns
		----------
		self.retailer_id: string
		"""
		# Generate random ID different from existing retailer ID
		while True:
			# Generate random 8 digits number
			new_retailer_id = random.randint(10000000, 99999999)
			unique_id = True
			# If list_retailer is not empty
			if len(list_retailer) != 0:
				# Loop through retailers objects in list_retailer
				for retailer in list_retailer:
					# If generated retailer id is not unique, break loop to regenerate id
					if new_retailer_id == retailer.retailer_id:
						unique_id = False
						break
				# If generated retailer id is unique, set it as self.retailer_id
				if unique_id:
					self.retailer_id = new_retailer_id
					break
			# If list_retailer is empty, set generated retailer id as self.retailer_id
			else:
				self.retailer_id = new_retailer_id
				return self.retailer_id

# Test code for Retailer Class
# if __name__ == "__main__":
# 	# Create retailer object
# 	first_retailer = Retailer(retailer_name = "Tang Chii Kang")
# 	# Print first retailer
# 	print(first_retailer)



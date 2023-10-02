from car import Car
from retailer import Retailer
from car_retailer import CarRetailer
import re
import time

def main_menu():
	"""
	Prints main menu of Car Purchase Advisor System.
	This function has no parameters and returns
	"""
	menu_page = '''
	Main Menu
	a) Look for the nearest car retailer
	b) Get car purchase advice
	c) Place a car order
	d) Exit
	'''
	print(menu_page)

def generate_test_data():
	"""
	Generate test data containing 3 retailers and 12 cars where each retailer has 4 cars
	"""
	# Generate 12 car objects
	car1 = Car(car_code="MB123456", car_name="BMW", car_capacity=6, car_horsepower=180, car_weight=2000,
				car_type="FWD")
	car2 = Car(car_code="LM654321", car_name="Mercedes", car_capacity=4, car_horsepower=200, car_weight=1800,
				car_type="AWD")
	car3 = Car(car_code="LK654820", car_name="Audi", car_capacity=4, car_horsepower=200, car_weight=1800,
				car_type="RWD")
	car4 = Car(car_code="WE604327", car_name="BYD", car_capacity=6, car_horsepower=300, car_weight=1800,
				car_type="AWD")
	car5 = Car(car_code="ER751823", car_name="AppleCar", car_capacity=4, car_horsepower=200, car_weight=1900,
				car_type="AWD")
	car6 = Car(car_code="RT154371", car_name="Toyota", car_capacity=2, car_horsepower=300, car_weight=2000,
				car_type="FWD")
	car7 = Car(car_code="YU254728", car_name="Honda", car_capacity=4, car_horsepower=200, car_weight=1800,
				car_type="FWD")
	car8 = Car(car_code="BN354327", car_name="Hyundai", car_capacity=6, car_horsepower=300, car_weight=1700,
				car_type="RWD")
	car9 = Car(car_code="FG454301", car_name="Volvo", car_capacity=2, car_horsepower=400, car_weight=1800,
				car_type="AWD")
	car10 = Car(car_code="WQ554721", car_name="Mercedes", car_capacity=4, car_horsepower=180, car_weight=2000,
				car_type="RWD")
	car11 = Car(car_code="GH654120", car_name="Audi", car_capacity=6, car_horsepower=300, car_weight=1700,
				car_type="AWD")
	car12 = Car(car_code="KS139364", car_name="Bentley", car_capacity=6, car_horsepower=400, car_weight=2000,
				car_type="FWD")

	# Generate 3 car retailers
	car_retailer1 = CarRetailer(retailer_name="Bryant Shop",
								carretailer_address="20 Kajang, 43000",
								carretailer_business_hours=(0.0, 24.0),carretailer_stock=[])

	car_retailer2 = CarRetailer(retailer_name="Lebron Shop",
								carretailer_address="30 Kuala Lumpur, 51000",
								carretailer_business_hours=(0.0, 24.0),carretailer_stock=[])

	car_retailer3 = CarRetailer(retailer_name="Nicole Shop",
								carretailer_address="40 Serdang, 43300",
								carretailer_business_hours=(9.0, 17.0),carretailer_stock=[])

	# Add cars to stock.txt, Car.car_list and carretailer_stock
	car_retailer1.add_to_stock(car1)
	car_retailer1.add_to_stock(car2)
	car_retailer1.add_to_stock(car3)
	car_retailer1.add_to_stock(car4)
	car_retailer2.add_to_stock(car5)
	car_retailer2.add_to_stock(car6)
	car_retailer2.add_to_stock(car7)
	car_retailer2.add_to_stock(car8)
	car_retailer3.add_to_stock(car9)
	car_retailer3.add_to_stock(car10)
	car_retailer3.add_to_stock(car11)
	car_retailer3.add_to_stock(car12)

	# Store retailers into retailer_list
	Retailer.retailer_list = [car_retailer1, car_retailer2, car_retailer3]

def main():
	# Empty stock.txt
	file_path = r'..\data\stock.txt'
	file = open(file_path, 'r+')
	file.truncate(0)
	file.close()

	# Initialization
	Car.car_list = []

	# Generate test data
	generate_test_data()

	# Start application of Car Purchase Advisor System
	while True:
		# Print main menu
		main_menu()
		# Ask user to select from main menu
		menu_option = input("Please input selection: ")

		# When user select menu option a
		if menu_option == "a":
			# Loop until user input an integer
			while True:
				input_postcode_string = input("Please input your postcode: ")
				# Check if input_postcode is digit
				if input_postcode_string.isdigit():
					# Convert string to integer
					input_postcode = int(input_postcode_string)
					# Assume minimum postcode distance with a maximum 5 digit value
					min_postcode_distance = 99999
					# Initialize nearest_retailer
					nearest_retailer = None

					# Replace min_postcode_distance with the lower postcode difference
					for car_retailer in Retailer.retailer_list :
						postcode_distance = car_retailer.get_postcode_distance(input_postcode)
						if postcode_distance < min_postcode_distance:
							min_postcode_distance = postcode_distance
							nearest_retailer = car_retailer

					# Print message after user selected option
					print("This is your nearest car retailer:")
					print(f"Retailer ID:{nearest_retailer.retailer_id}, Name:{nearest_retailer.retailer_name}, "
						  f"Address:{nearest_retailer.carretailer_address}, "
						  f"Business Hour:{nearest_retailer.carretailer_business_hours}")
					break
				# If input_postcode is not a digit
				else:
					print("Invalid input. Please input an integer.")

		# When user select menu option b
		elif menu_option == "b":
			# Initialize index for printing retailer index
			i = 1
			print("List of Car Retailer: ")
			# Print all retailers
			for car_retailer in Retailer.retailer_list :
				print(f"{i}. Retailer ID:{car_retailer.retailer_id}, Name:{car_retailer.retailer_name}, "
					  f"Address:{car_retailer.carretailer_address}, "
					  f"Business Hour:{car_retailer.carretailer_business_hours}")
				i += 1

			# Loop for Car Retailer Selection
			submenu_option = None
			while True:
				# Break from while loop if submenu_option = 5
				if submenu_option == "5":
					break
				# Prompt user to input the order of selected car retailer
				option_carretailer_string = input("Select Car Retailer by index e.g.\"1\"or \"2\": ")

				# Check if option_carretailer_string is digit
				if option_carretailer_string.isdigit():
					# Convert string to integer
					option_carretailer = int(option_carretailer_string)

					# Check if selected option is within the index of retailer_list
					if 0 < option_carretailer <= (len(Retailer.retailer_list)):
						# Store selected retailer
						selected_retailer = Retailer.retailer_list[option_carretailer-1]
						# Print selected retailer
						print(f"You selected: ")
						print(f"Retailer ID:{selected_retailer.retailer_id}, Name:{selected_retailer.retailer_name}, "
							  f"Address:{selected_retailer.carretailer_address}, "
							  f"Business Hour:{selected_retailer.carretailer_business_hours}")

						# Loop for sub menu selection
						while True:
							# Print sub_menu
							sub_menu = '''
	1) Recommend a car
	2) Get all cars in stock
	3) Get cars in stock by car types
	4) Get probationary licence permitted cars in stock
	5) Back to Main Menu
												'''
							print(sub_menu)
							# Prompt user to input sub menu selection
							submenu_option= input("Select Option: ")

							# Check if input is within 1 to 5
							if submenu_option in ["1", "2", "3", "4","5"]:

								# If user input 1, recommend a car
								if submenu_option == "1":
									print(f"Retailer ID    : {selected_retailer.retailer_id}")
									print(f"Retailer Name  : {selected_retailer.retailer_name}")
									selected_car = selected_retailer.car_recommendation()

									# Check if the selected_car exist
									if selected_car != None:
										print(f"Recommended Car ")
										print(f"Car ID:{selected_car.car_code}, Car Name:{selected_car.car_name}, "
											  f"Car Capacity:{selected_car.car_capacity}, "
											  f"Car HP:{selected_car.car_horsepower}, "
											  f"Car Weight:{selected_car.car_weight}, Car Type:{selected_car.car_type}")
									# If the selected_car exist print no available cars
									else:
										print("There are no available cars.")

								# If user input 2, get all cars in stock
								elif submenu_option == "2":
									print(f"Retailer ID    : {selected_retailer.retailer_id}")
									print(f"Retailer Name  : {selected_retailer.retailer_name}")
									get_all_stock_item = selected_retailer.get_all_stock()

									# Check if the get_all_stock_item exist
									if get_all_stock_item != None:
										print("List of cars in stock")
										# Initialize index for printing stock index
										i = 1
										for car in get_all_stock_item:
											print(f"{i}. Car ID:{car.car_code}, Car Name:{car.car_name}, "
												  f"Car Capacity:{car.car_capacity}, Car HP:{car.car_horsepower}, "
												  f"Car Weight:{car.car_weight}, Car Type:{car.car_type}")
											i += 1
									# If if get_all_stock_item does not exist, print no available cars
									else:
										print("There are no available cars.")

								# If user input 3, get stocks by car types
								elif submenu_option == "3":
									print("This is the list of car types: FWD, RWD, AWD")

									# Loop for car types input
									while True:
										# Prompt user to input car types in all uppercase with space in between
										car_type_input = input("Please input preferred car type(s) with space in between, "
															   "e.g. \"FWD RWD\": ")
										# Split car_type_input string based on the space
										car_type_list = car_type_input.split()

										# Initialize correct_input
										correct_input = True
										# Loop through car_type_list
										for car_type_list_item in car_type_list:
											# Check if all items in car_type_list only contains "AWD", "FWD", "RWD"
											if car_type_list_item not in ["AWD", "FWD", "RWD"]:
												print("Invalid input. Please input again.")
												# When input is invalid, change correct_input to False
												correct_input = False
												break

										# If input is valid, print all cars by car type
										if correct_input:
											# Call get_stock_by_car_type which returns a list of car objects
											car_type_item = selected_retailer.get_stock_by_car_type(car_type_list)

											# Check if get_stock_by_car_type_item is empty
											if car_type_item != []:
												print(f"Retailer ID    : {selected_retailer.retailer_id}")
												print(f"Retailer Name  : {selected_retailer.retailer_name}")
												car_type_string = " , ".join(map(str, car_type_list))
												print(f"List of cars with {car_type_string} type in stock")

												# Initialize index for printing stock index
												i = 1
												for car in car_type_item:
													print(f"{i}. Car ID:{car.car_code}, Car Name:{car.car_name}, "
														 f"Car Capacity:{car.car_capacity}, Car HP:{car.car_horsepower}"
														  f", Car Weight:{car.car_weight}, Car Type:{car.car_type}")
													i += 1

											# If car_type_item is empty, print no available cars
											else:
												print("There are no available cars by your selected type(s).")
											# Break while loop for car types input
											break

								# If user input 4, get probationary licence permitted cars
								elif submenu_option == "4":
									# Call get_stock_by_licence_type which returns a list of car objects
									get_stock_by_licence_type_item = selected_retailer.get_stock_by_licence_type("P")

									# Check if get_stock_by_licence_type_item is not empty
									if get_stock_by_licence_type_item != []:
										print(f"Retailer ID    : {selected_retailer.retailer_id}")
										print(f"Retailer Name  : {selected_retailer.retailer_name}")
										print("List of probationary licence permitted cars in stock")

										# Initialize index for printing stock index
										i = 1
										for car in get_stock_by_licence_type_item:
											print(f"{i}. Car ID:{car.car_code}, Car Name:{car.car_name}, "
												  f"Car Capacity:{car.car_capacity}, Car HP:{car.car_horsepower}, "
												  f"Car Weight:{car.car_weight}, Car Type:{car.car_type}")
											i += 1

									# If get_stock_by_licence_type_item is empty, print no available cars
									else:
										print("There are no available probationary licence permitted cars.")

								# If user input 5, break loop for sub menu selection
								elif submenu_option == "5":
									break

							# If sub_menu input is not within 1 to 5
							else:
								print("Invalid input. Please input again.")

					# If retailer option is not within available retailer list
					else:
						print("Invalid input. Please input again.")

				# If inputted retailer option is not in digits
				else:
					print("Invalid input. Please input again.")

		# When user select menu option c, creates order
		elif menu_option == "c":
			# Loop for postcode input
			while True:
				# Prompt user to input retailer ID and car ID with a space between
				input_postcode = input("Please input retailer ID and car ID, e.g. \"12345678 MB123456:\", "
									   "or \"B\" back to Main Menu:")
				# Using Regular Expression to detect the input IDs
				pattern = r'\b\d{8} [A-Z]{2}\d{6}\b'
				# If pattern of input match with retailer ID and car ID
				if re.match(pattern, input_postcode):
					# Split input into retailer ID and car ID
					retailer_ID = int(input_postcode.split()[0])
					car_ID = input_postcode.split()[1]

					# Initialize retailer_found
					retailer_found = False

					# Loop for car_retailer in Retailer.retailer_list
					for car_retailer in Retailer.retailer_list:
						# Check if user input retailer id can be found in retailer_list(program)
						if car_retailer.retailer_id == retailer_ID:
							# Change retailer_found to be True
							retailer_found = True
							# Determine Current time in 24hours format
							# source: https://www.geeksforgeeks.org/python-time-localtime-method/
							time_current = time.localtime()
							hour_current = time_current.tm_hour
							minute_current = time_current.tm_min
							# Convert 24 hours format to 2 decimals number
							time_current_decimal = round(hour_current + minute_current / 60, 2)
							# Check whether current time is within business hour of target retailer
							if car_retailer.is_operating(time_current_decimal):
								# Create order here
								for car in Car.car_list:
									# Check if car is in car_ID list, car_code is in car_retailer.carretailer_stock
									if car.car_code == car_ID and car.car_code in car_retailer.carretailer_stock:
										# Create Order
										new_order = car_retailer.create_order(car.car_code)
										# Print Order Details
										print("Order have been successfully created, here is your order details.")
										print(f"Order ID       :{new_order.order_id}")
										print(f"Order Car      :Car ID:{new_order.order_car.car_code}, "
											  f"Car Name:{new_order.order_car.car_name}, "
											  f"Car Capacity:{new_order.order_car.car_capacity}, "
											  f"Car HP:{new_order.order_car.car_horsepower}, "
											  f"Car Weight:{new_order.order_car.car_weight}, "
											  f"Car Type:{new_order.order_car.car_type}")
										print(f"Order Retailer :{new_order.order_retailer.retailer_name}")
										print(f"Order Timestamp:{new_order.order_creation_time}\n")
										print("Thank you for your order!\n")
										print("Would you like to make another order?")
										break
									# elif car is the last in Car.car_list and still not equal to input car_ID
									elif car == ((Car.car_list)[-1]) and ((Car.car_list)[-1]).car_code != car_ID:
										print("Car ID does not exist, please input again.")
										# Break loop for car in Car.car_list
										break

							# If Retailer is not operating
							else:
								print(f"{car_retailer.retailer_name} is closed, "
									  f"Business Hour is {car_retailer.carretailer_business_hours}")
								print("Please come again!")
							# Break loop for car_retailer in Retailer.retailer_list
							break

					# If user input retailer id cannot be found in retailer_list
					if retailer_found == False:
						print("Retailer ID does not exist, please input again.")

				# If user input B, go back to main menu
				elif input_postcode == "B":
					break
				# If user does not input correct format
				else:
					print("Input is not in the correct format, please input again.")

		# When user select menu option d
		elif menu_option == "d":
			# Confirmation before exit
			exit_app = input("Exit ?(Y/N) :")

			# Y: Yes, No: No
			if exit_app == "Y":
				print("You selected Exit. Goodbye!")
				break
			elif exit_app == "N":
				print("Back to Main Menu.")
			else:
				print("Invalid input. Please input again!")

		# If user input options other than a,b,c,d
		else:
			print("Invalid input. Please input again!")

if __name__ == "__main__":
	main()
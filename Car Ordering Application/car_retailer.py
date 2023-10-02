import random
import os
import re
from retailer import Retailer
from car import Car
from order import Order

class CarRetailer(Retailer):
    """
    A class contains all operations related to a car retailer class.
    This class inherits from retailer class
    """

    def __init__(self, retailer_name, carretailer_address, carretailer_business_hours, carretailer_stock=[]):
        """
        Constructs car retailer object

        Parameters
        ----------
        retailer_name : str
        carretailer_address : str
        carretailer_business_hours : tuple
        carretailer_stock : list (car_codes)

        """
        super().__init__(retailer_name)
        self.carretailer_address = carretailer_address
        self.carretailer_business_hours = carretailer_business_hours
        self.carretailer_stock = carretailer_stock

    def __str__(self):
        """
        Generate string of car retailer object

        Parameters
        ----------
        None

        Returns
        ----------
        str
        """
        return f"{super().__str__()}, {self.carretailer_address}, {self.carretailer_business_hours}, " \
               f"{self.carretailer_stock}"

    def load_current_stock(self, path):
        """
        From stock.txt file, load current stock of the car retailer based on retailer id.
        Regular Expression is used to match the retailer id.
        All stock of retailer is loaded and passed to car constructor to form car objects.
        Car objects is stored in a class variable list named Car.car_list
        car_code is stored in a list saved to carretailer_stock
        Parameters
        ----------
        path : str (path of stock.txt)

        """
        # Check if file exist at the path
        if os.path.isfile(path):
            # Open file in read mode
            input_stock = open(path, "r")
            # Read text files and turn it into list of lines
            generate_lines = input_stock.readlines()

            # Pattern for retailer_id
            # ^: from start of line; (\d+),: decimals more than one and ends with comma
            pattern_id = r'^(\d+),'
            # Pattern for car retailer stock
            # Detect everything inside a bracket, (.*?) captures everything
            # pattern1 = r'\[([^]]+)\]'
            pattern_stock = r'\[(.*?)\]'

            # Load stock.txt file, store car details into car objects and append into Car.car_list
            # Loop through all lines in existing stock.txt file
            for line in generate_lines:
                # Search retailer id
                match_id = re.search(pattern_id, line)
                if match_id:
                    # Convert match object into an int
                    retailer_id = int(match_id.group(1))
                    # If retailer id in stock.txt line matches current retailer id
                    if retailer_id == self.retailer_id:
                        # Search car retailer stock
                        match_stock = re.search(pattern_stock, line)
                        # Convert match object into a string
                        car_retailer_stock_list = match_stock.group(1)
                        # Split the car_retailer_stock_list based on ', ' to categorise car objects
                        car_object_list = car_retailer_stock_list.split('\', \'')

                        # Store car details into car objects and append into Car.car_list
                        for car_object in car_object_list:
                            # Split car_object_list based on comma to categorise car variables
                            car_variable = car_object.split(', ')
                            # Transforming data from string to the required data type
                            car_variable[0] = car_variable[0].strip("'")
                            car_variable[-1] = car_variable[-1].strip("'")
                            car_variable[2] = int(car_variable[2])
                            car_variable[3] = int(car_variable[3])
                            car_variable[4] = int(car_variable[4])

                            # Construct car object
                            car = Car(car_code=car_variable[0], car_name=car_variable[1], car_capacity=car_variable[2],
                                      car_horsepower=car_variable[3], car_weight=car_variable[4],
                                      car_type=car_variable[5])

                            # Append all car object into Car.car_list
                            if car not in Car.car_list:
                                Car.car_list.append(car)

                            # Append all car_code into carretailer_stock
                            if car_variable[0] not in self.carretailer_stock:
                                self.carretailer_stock.append(car_variable[0])

            # Close read mode
            input_stock.close()

        # If file does not exist at the path
        else:
            print("File is not found!")

    def is_operating(self, cur_hour):
        """
        Indicate whether car retailer is operating currently

        Parameters
        ----------
        cur_hour: float (current hour in 24H format)

        Returns
        ----------
        Boolean(True: is operating/ False: is not operating
        """
        # Check whether business is operating currently
        business_start_hour = self.carretailer_business_hours[0]
        business_end_hour = self.carretailer_business_hours[1]
        # If cur hour is between start hour and end hour, return True and vice versa
        return business_start_hour <= cur_hour and business_end_hour >= cur_hour

    def get_all_stock(self):
        """
        returns all available car in stock for the car retailer

        Parameters
        ----------
        None

        Returns
        ----------
        get_all_stock: list (list of Car objects)
        """
        get_all_stock = []
        # Append all cars with car_code belongs to current retailer into a list
        for car in Car.car_list:
            if car.car_code in  self.carretailer_stock:
                get_all_stock.append(car)
        return get_all_stock

    def get_postcode_distance(self, postcode):
        """
        obtain the difference between user input postcode and retailer postcode

        Parameters
        ----------
        postcode: int

        Returns
        ----------
        int (absolute difference between postcodes)
        """
        # Split address to obtain postcode
        carretailer_address_postcode = self.carretailer_address.split(",")
        # Strip off spaces for last part of address which indicates the postcode
        carretailer_address_postcode[-1] = carretailer_address_postcode[-1].strip()
        # Calculate absolute diff of postcode
        if carretailer_address_postcode[-1].isdigit():
            return abs(postcode - int(carretailer_address_postcode[-1]))
        else:
            print("Inappropriate format of car retailer postcode!")

    def remove_from_stock(self, car_code):
        """
        Remove car_code from self.carretailer_stock
        Remove stock from stock.txt by replacing the old with new carretailer details
        Remove car object from Car.car_list

        Parameters
        ----------
        car_code: str (car_code to be removed)

        Returns
        ----------
        Boolean (True: successful/ False: unsuccessful ,car not exist)
        """
        # Check if stock exist
        remove_stock = False

        # Check whether car_code existed
        if car_code not in self.carretailer_stock:
            return remove_stock
        else:
            # Remove from carretailer_stock
            self.carretailer_stock.remove(car_code)
            # Remove from Car.car_list
            remove_from_list = []
            for car in Car.car_list:
                if car_code != car.car_code:
                   remove_from_list.append(car)
            Car.car_list = remove_from_list

            # Update stock.txt
            file_path = r'..\data\stock.txt'
            input_stock = open(file_path, "r")

            # Read text files and turn it into list of lines
            generate_lines = input_stock.readlines()

            # Determine re patterns
            # Pattern for retailer id
            pattern = r'^(\d+),'
            # Detect retailer id for every line
            new_line = []
            for line in generate_lines:
                # Use re to detect retailer id
                match_id = re.search(pattern, line)
                if match_id:
                    # Convert retailer id from text to integer
                    retailer_id = int(match_id.group(1))

                    # Detect the similar retailer id
                    if retailer_id == self.retailer_id:
                        # If detected retailer id, append retailer details including id, name,address and business hour
                        new_line.append(f"{super().__str__()}, {self.carretailer_address}, "
                                        f"{self.carretailer_business_hours}, [")
                        # If retailer id, remove_stock is True
                        remove_stock = True

                        # When carretailer_stock is empty, close retailer stock with a end bracket
                        if len(self.carretailer_stock) == 0:
                            new_line.append(']\n')
                        # When carretailer not empty, append the car stocks to new_line
                        else:
                            i = 1
                            for car in Car.car_list:
                                if car.car_code in self.carretailer_stock:
                                    # Append car with comma if it's not the last stock
                                    if i != len(self.carretailer_stock):
                                        new_line.append(f"\'{car}\',")
                                        i += 1
                                    # Append car with end bracket if it's the last stock
                                    else:
                                        new_line.append(f"\'{car}\']\n")

                    # Append the same line if no stock removing required
                    else:
                        new_line.append(line)

            # Open file with write mode
            file = open(file_path, 'w')
            # Rewrite the file
            file.writelines(new_line)
            file.close()
            input_stock.close()
            return remove_stock

    def add_to_stock(self, car):
        """
        Add car_code to self.carretailer_stock
        Add stock to stock.txt by replacing the old with new updated carretailer details
        Add car object to Car.car_list

        Parameters
        ----------
        car: object (car_code to be added)

        Returns
        ----------
        Boolean (True: successful/ False: unsuccessful ,car already exist)
        """
        # Check if stock exist
        add_stock = False

        # Check whether car_code exist
        if car.car_code in self.carretailer_stock and car in Car.car_list:
            return add_stock
        else:
            # Append to carretailer_stock
            self.carretailer_stock.append(car.car_code)
            # Add to Car.car_list
            Car.car_list.append(car)

            # Update stock.txt
            file_path = r'..\data\stock.txt'
            input_stock = open(file_path, "r")

            # Read text files and turn it into list of lines
            generate_lines = input_stock.readlines()

            # Determine re patterns
            # Pattern for retailer id
            pattern = r'^(\d+),'
            # Detect retailer id for every line
            new_line = []
            for line in generate_lines:
                # Use re to detect retailer id
                match_id = re.search(pattern, line)
                if match_id:
                    # Convert retailer id from text to integer
                    retailer_id = int(match_id.group(1))

                    # Detect the similar retailer id
                    if retailer_id == self.retailer_id:
                        # If detected retailer id, append retailer details including id,name, address and business hour
                        new_line.append(f"{super().__str__()}, {self.carretailer_address}, "
                                        f"{self.carretailer_business_hours}, [")
                        # If retailer id, add_stock is True
                        add_stock = True

                        # When carretailer_stock is empty, close retailer stock with a end bracket
                        if len(self.carretailer_stock) == 0:
                            new_line.append(']\n')
                        # When carretailer not empty, append the car stocks to new_line
                        else:
                            i = 0
                            for car in Car.car_list:
                                if car.car_code in self.carretailer_stock:
                                    # Append car with comma if it's not the last stock
                                    if i != (len(self.carretailer_stock)-1):
                                        new_line.append(f"\'{car}\', ")
                                        i += 1
                                    # Append car with end bracket if it's the last stock
                                    else:
                                        new_line.append(f"\'{car}\']\n")

                    # Append the same line if no stock removing required
                    else:
                        new_line.append(line)

            # Create new retailer if retailer id is not found
            if add_stock == False:
                new_line.append(f"\n{super().__str__()}, {self.carretailer_address}, {self.carretailer_business_hours},"
                                f" [\'{car}\']")
                add_stock = True

            # Open file with write mode
            file = open(file_path, 'w')
            # Rewrite the file
            file.writelines(new_line)
            # Close files
            file.close()
            input_stock.close()
            return add_stock

    def get_stock_by_car_type(self, car_types):
        """
        return list of cars from retailer stock in Car.car_list by specific car type

        Parameters
        ----------
        car_types: list (list of car_types to be fetched)

        Returns
        ----------
        matched_car_type: list (list of car objects)
        """
        matched_car_type = []
        # Store car in matched_car_type if car types matches
        for car in Car.car_list:
            if car.get_car_type() in car_types and car.car_code in self.carretailer_stock:
                matched_car_type.append(car)
        return matched_car_type

    def get_stock_by_licence_type(self, licence_type):
        """
        return list of car from retailer stock in Car.car_list that not forbidden by licence type

        Parameters
        ----------
        licence_type: string ("L": Learner Licence, "P": Probationary Licence, "F": Full Licence)

        Returns
        ----------
        prohibited_vehicles or non_prohibited_vehicles: list (list of car objects)
        """
        prohibited_vehicles = []
        non_prohibited_vehicles = []
        for car in Car.car_list:
            # Store prohibited cars in prohibited_vehicles
            if car.probationary_licence_prohibited_vehicle() and car.car_code in self.carretailer_stock:
                prohibited_vehicles.append(car)
            # Store non prohibited cars in non_prohibited_vehicles
            elif not car.probationary_licence_prohibited_vehicle() and car.car_code in self.carretailer_stock:
                non_prohibited_vehicles.append(car)

        # Return non_prohibited_vehicles and prohibited_vehicles based on licence type
        if licence_type in ["L", "Full"]:
            return non_prohibited_vehicles
        else:
            return prohibited_vehicles

    def car_recommendation(self):
        """
        return random car in Car.car_list from retailer stock

        Returns
        ----------
        car: object
        """
        # Check if carretailer_stock is empty
        if len(self.carretailer_stock) != 0:
            # Recommend a random car by using random
            recommended_car_code = self.carretailer_stock[random.randint(0, len(self.carretailer_stock)-1)]
            for car in Car.car_list:
                if car.car_code == recommended_car_code:
                    return car
        # Print empty when there is no car
        else:
            return None

    def create_order(self, car_code):
        """
        Return an order object.
        When order created, call remove_from_stock() to remove stock from Car.car_list, 
        car_code from self.carretailer_stock and car stock from stock.txt.
        Append new order to order.txt

        Parameters
        ----------
        car_code: string (car_code of car to be ordered)

        Returns
        ----------
        order: object
        """
        # Locate car in Car.car_list based on car_code
        for car in Car.car_list:
            if car.car_code == car_code:
                order_car = car
                break

        # Create order object
        order = Order(order_car=order_car, order_retailer = self)

        # Remove ordered car from stock txt
        self.remove_from_stock(car_code)

        # Update order.txt
        # Order.txt format: order_id, order_car.car_code, order_retailer.retailer_id, order_creation_time)
        file_path = r'..\data\order.txt'
        # Open file using append mode
        order_file = open(file_path, 'a')
        new_order_line = f"{order.order_id},{car_code},{self.retailer_id},{order.order_creation_time}\n"
        # Append new_order_line into order.txt
        order_file.write(new_order_line)
        # Close file
        order_file.close()

        return order

# Test Code for Car Retailer Class
if __name__ == "__main__":
    # Define car and retailer, add car to retailer stock
    first_car_retailer = CarRetailer(retailer_name = "Bryant Shop",
                                     carretailer_address = "123 Kuala Lumpur, 12345",
                                     carretailer_business_hours = (8.0,17.0))

    car1 = Car(car_code="MB123456", car_name="BMW", car_capacity=6, car_horsepower=180, car_weight=2000,
               car_type="FWD")
    car2 = Car(car_code="NM123423", car_name="Benz", car_capacity=6, car_horsepower=200, car_weight=1500,
               car_type="RWD")
    first_car_retailer.add_to_stock(car1)
    first_car_retailer.add_to_stock(car2)

    # Test code for load_current_stock
    # Empty stock.txt
    # file_path = r'..\data\stock.txt'
    # file = open(file_path, 'r+')
    # file.truncate(0)
    # file.close()
    # stock_file_path = r'..\data\stock.txt'
    # first_car_retailer.load_current_stock(stock_file_path)
    # print(Car.car_list)
    # print(first_car_retailer.carretailer_stock)

    # # Test code for is_operating()
    # # Bryant Shop operating hour is (8.0,17,0)
    # cur_hour1 = 12.0
    # cur_hour2 = 18.0
    # print(f"Car Retailer is operating: {first_car_retailer.is_operating(cur_hour1)}")
    # print(f"Car Retailer is operating: {first_car_retailer.is_operating(cur_hour2)}")

    # # Test code for get_all_stock()
    # print(first_car_retailer.get_all_stock())
    #
    # # Test code for get_postcode_distance()
    # # 19000 - 12345 = 6655
    # print(first_car_retailer.get_postcode_distance(19000))
    #
    # # Test code for remove_from_stock()
    # # Try removing car2
    # first_car_retailer.remove_from_stock(car2.car_code)
    # # Only car1 left
    # print(first_car_retailer)
    #
    # # Test code for add_to_stock()
    # # Try adding car2
    # first_car_retailer.add_to_stock(car1)
    # first_car_retailer.add_to_stock(car2)
    # print(first_car_retailer)
    #
    # # Test code for get_stock_by_licence_type()
    # print(first_car_retailer.get_stock_by_licence_type("P"))
    # print(first_car_retailer.get_stock_by_licence_type("L"))
    #
    # # Test code for get_stock_by_licence_type()
    # print(first_car_retailer.get_stock_by_car_type(["RWD","FWD"]))
    # print(first_car_retailer.get_stock_by_car_type(["AWD"]))
    #
    # # Test code for car_recommendation()
    # print(first_car_retailer.car_recommendation())
    #
    # # Test code for create_order()
    # print(first_car_retailer.create_order(car1.car_code))

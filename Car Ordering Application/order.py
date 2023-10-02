import random
import string
import time
# # Uncomment in order to run test code
# from car import Car
# from retailer import Retailer

class Order:
    def __init__(self, order_car, order_retailer):
        """
        Constructs order object

        Parameters
        ----------
        order_id : str
        order_car : object (car object)
        order_retailer : object (retailer object)
        order_creation_time : int (current timestamp)

        """
        self.order_id = self.generate_order_id(order_car.car_code)
        self.order_car = order_car
        self.order_retailer = order_retailer
        self.order_creation_time = int(time.time())

    def __str__(self):
        """
        Generate string of order object

        Parameters
        ----------
        None

        Returns
        ----------
        str
        """
        return f"{self.order_id}, {self.order_car.car_code}, {self.order_retailer.retailer_id}, " \
               f"{self.order_creation_time}"

    def generate_order_id(self, car_code):
        """
        Generate random order ID using 7 steps

        Parameters
        ----------
        car_code: str (car_code related to current order

        Returns
        ----------
        order_id: string
        """
        # Step 1: Generate a list of random characters
        random_characters = []
        string_len = 6
        # Source from: https://www.geeksforgeeks.org/python-string-ascii_lowercase/
        lowercase_char = string.ascii_lowercase
        # Generate 6 random characters in a list
        for i in range(string_len):
            random_char = lowercase_char[random.randint(0, len(lowercase_char)-1)]
            random_characters.append(random_char)

        # Step 2: Convert 2nd character in the string to uppercase letter
        i = 1
        # Starting from second position, convert even positions from lower to uppercase
        while i < string_len:
            random_characters[i] = random_characters[i].upper()
            i += 2

        # Step 3 & 4: get ASCII code of letter using ord
        char_to_ascii = []
        for char in random_characters:
            char_to_ascii.append(ord(char))

        # Step 4: Power 2 of ASCII code divide length of str_1
        remainders = []
        str_1 = "~!@#$%^&*"
        for ascii_code in char_to_ascii:
            remainders.append((ascii_code ** 2) % (len(str_1)))

        # Step 5: Obtain corresponding char from str_1 using remainder as index
        new_str = []
        for i in remainders:
            new_str.append(str_1[i])

        # Step 6: Append each char from Step 5 according to index of char from Step 2
        # Join random characters generated from Step 2
        order_id = "".join(random_characters)
        n = 0
        # Append char into order_id
        for char in new_str:
            order_id += char * n
            n += 1

        # Step 7: Append car_code and order creation time to string generated
        order_id += car_code + str(int(time.time()))
        return order_id

# Test code for Order Class:
# if __name__ == "__main__":
#     car = Car(car_code="KS136564", car_name="Huawei Car", car_capacity=6, car_horsepower=400, car_weight=2000,
#                 car_type="FWD")
#     car_retailer = CarRetailer(retailer_name="David Shop",
#                                 carretailer_address="40 Bangsar, 43300",
#                                 carretailer_business_hours=(9.0, 17.0), carretailer_stock=[])
#     order = Order(order_car = car, order_retailer = car_retailer)
#     print(order)


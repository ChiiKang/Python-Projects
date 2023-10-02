class Car:
    """
    A class contains all operations related to a car
    """

    # Class Variable
    car_list = []

    def __init__(self, car_code, car_name, car_capacity, car_horsepower, car_weight, car_type="FWD"):
        """
        Constructs car object

        Parameters
        ----------
        car_code : str
        car_name : str
        car_capacity : int
        car_horsepower : int
        car_weight : int
        car_type : str
        """
        self.car_code = car_code
        self.car_name = car_name
        self.car_capacity = car_capacity
        self.car_horsepower = car_horsepower
        self.car_weight = car_weight
        self.car_type = car_type

    def __str__(self):
        """
        Generate string of car object

        Parameters
        ----------
        None

        Returns
        ----------
        str
        """
        return f"{self.car_code}, {self.car_name}, {self.car_capacity}, {self.car_horsepower}, {self.car_weight}, " \
               f"{self.car_type}"

    def probationary_licence_prohibited_vehicle(self):
        """
        Determine whether vehicle is a prohibited vehicle for probationary licence drivers

        Parameters
        ----------
        None

        Returns
        ----------
        Boolean (True if vehicle is a prohibited vehicle, Vice versa)
        """
        # car with Power/Mass ratio > 130kW/tonne is prohibited vehicle
        power_mass_ratio = 1000 * (self.car_horsepower / self.car_weight)
        return power_mass_ratio > 130

    def found_matching_car(self, car_code):
        """
        Determine whether current vehicle is found based on car_code

        Parameters
        ----------
        car_code: str

        Returns
        ----------
        Boolean (True if car_code is found, Vice versa)
        """
        return self.car_code == car_code

    def get_car_type(self):
        """
        Return car type of current car

        Parameters
        ----------
        None

        Returns
        ----------
        car_type: string
        """
        return self.car_type

# Test Code for Car Class
# if __name__ == "__main__":
#     # Create car object
#     first_car = Car(car_code="MB123456", car_name="BMW", car_capacity=6, car_horsepower=180, car_weight=2000,
#                     car_type="FWD")
#     # Print car object
#     print(first_car)
#     # Determine whether first_car is a prohibited vehicle
#     print(first_car.probationary_licence_prohibited_vehicle())
#     # Determine is "MB123456", first_car's car code
#     print(first_car.found_matching_car("MB123456"))
#     # Determine type of first car
#     print(first_car.get_car_type())

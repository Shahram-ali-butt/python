class CAR:
    total_cars_made = 0 # Class variable (only accessible by a class not an instance)

    def __init__(self, brand, model): # constructor
        self.__brand = brand # Use __ before attribute to privatize
        self.__model = model
        CAR.total_cars_made += 1 #Manipulating class variable using class name

    def full_name(self): # simple method showing you can access private attr from within the class
        return f"{self.__brand} {self.__model}"
    
    # Encapsulation (getter for controlled access of private attribute)
    def get_brand(self):
        return self.__brand
    
    # Polymorphism (same method in related classes but in diferent forms)
    def fuel_type(self):
        return "petrol/diesel"
    
    # Decoraters (start with @. Add functionality) 
    @staticmethod # Static Method (not connected with class nor instance)(does not take self or cls)
    def general_description():
        return "Cars are the basic means of transport in the modern world."
    
    @property #Converting a method into a property
    def model(self):
        return self.__model + " (@property model)"


# inheritence (creating child class)
class ELECTRIC_CAR(CAR):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model) #super() to access parent constructor/attr/methods
        self.battery_size = battery_size #added functionality of child class
    
    # Polymorphism (same method in related classes)
    def fuel_type(self):
        return "Elecric charge"

my_toyota = CAR("Toyota", "Corolla")
my_tesla = ELECTRIC_CAR("Tesla", "Model Y", "85kWh")

# Basic operations (note that the attributes are private)
# print(my_tesla.get_brand())
# print(my_tesla.full_name())

# Access class variable using class name
# print(CAR.total_cars_made)

# Accessing static functions using both the instance and class
# print(my_tesla.general_description())
# print(CAR.general_description())

# accessing the @property method named model
# print(my_tesla.model) 

# checking inheritence using isinstance() method
# print(isinstance(my_tesla, CAR), isinstance(my_tesla, ELECTRIC_CAR))



# Advance/Complex stuff

#copy of the CAR class other than 'optionaly' including **kwargs
class AUTOMOBILE: 
    total_cars_made = 0

    def __init__(self, brand, model):
        # super().__init__(**kwargs) #Used for Cooperative Multiple Inheritence. If want to enable give it's own constructor **kwargs
        self.__brand = brand
        self.__model = model
        AUTOMOBILE.total_cars_made += 1
    def get_brand(self):
        return self.__brand 
    def full_name(self):
        return f"{self.__brand} {self.__model}"
    def fuel_type(self):
        return "petrol/diesel"
    @staticmethod
    def general_description():
        return "Cars are the basic means of transport in the modern world."
    @property 
    def model(self):
        return self.__model + " (@property model)"


class BATTERY:
    def __init__(self, battery_spec, battery_type):
        # super().__init__(**kwargs) #Used for Cooperative Multiple Inheritence. If want to enable give it's own constructor **kwargs 
        self.__battery_type = battery_type
        self.__battery_spec = battery_spec

    def get_battery_info(self):
        return f"{self.__battery_spec} {self.__battery_type}"

class ENGINE:
    def __init__(self, engine_size, engine_type, **kwargs):
        # super().__init__(**kwargs) #Used for Cooperative Multiple Inheritence. If want to enable give it's own constructor **kwargs
        self.__engine_size = engine_size
        self.__engine_type = engine_type

    def get_engine_info(self):
        return f"{self.__engine_size} {self.__engine_type}"

class HYBRID_CAR(AUTOMOBILE):
    def __init__(self, brand, model, engine_size, engine_type, battery_spec, battery_type):
    
# 1st Strategy
# Explicit Calls to the constructors of parent classes
        # Note that HYBRID_CAR would have to inherit from BATTERY and ENGINE too
        # AUTOMOBILE.__init__(self, battery_spec, battery_type) 

# 2nd Strategy
# Coperative Multiple Inheritence
        # - Call super().__init__() in their own __init__ methods and take in **kwargs
        # - Also give the parent class constructor **kwargs
        # Note that HYBRID_CAR would have to inherit from BATTERY and ENGINE too
        
        # super().__init__(brand = brand, model = model, engine_size = engine_size, 
        #                  engine_type = engine_type, battery_spec = battery_spec, 
        #                  battery_type = battery_type)
    
# 3rd Strategy
# Composition instead of Inheritence (actually a combination)
    # Composition is explained at the end of the file

        #This is inheritence
        super().__init__(brand, model) 
        # This is composition
        self.engine = ENGINE(engine_size, engine_type)
        self.battery = BATTERY(battery_spec, battery_type)

    def get_car_info(self):
        return f"{self.full_name()}, Engine: {self.engine.get_engine_info()}, Battery: {self.battery.get_battery_info()}"


my_koeningsegg = HYBRID_CAR("Koeningsegg", "Regera", "5.0ltr", "V8", "800Volt 4.5kWh", "Lithiem Ion")
print(my_koeningsegg.get_car_info())


# A word about "Composition":
# Composition is a design principle where a class is built using instances of other classes, 
# rather than inheriting from them. Instead of saying “I am a BATTERY,” you say “I have a BATTERY.”
# It’s the classic “has-a” relationship, as opposed to inheritance’s “is-a” relationship.
# HYBRID_CAR doesn’t inherit from ENGINE or BATTERY. Instead, it contains them as attributes.

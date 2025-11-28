from vehicle import Vehicle

class Car(Vehicle):
    from vehicle import Vehicle  # Assuming relative import is required
    
  # Assuming relative import is required
    # This class inherits __init__, wheel_size, wheel_number, and fill_up_tank() 
    # from the Vehicle superclass.

    # Overwriting the inherited go() method
    def go(self):
        return "VRRROOOOOOOOOOOOOOOOOOOOOOOM!!!!!"

    pass
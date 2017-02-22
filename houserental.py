from rental import Rental
from house import House


class HouseRental(Rental, House):
    """
    Has info about house rent.
    """
    def prompt_init():
        """
        Calls prompt_init() from House and updates it with a dictionary from Rental.
        """
        init = House.prompt_init()
        init.update(Rental.prompt_init())
        return init
    prompt_init = staticmethod(prompt_init)

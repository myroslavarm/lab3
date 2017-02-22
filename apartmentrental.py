from rental import Rental
from apartment import Apartment


class ApartmentRental(Rental, Apartment):
    """
    Has info about apartment rental.
    """
    def prompt_init():
        """
        Calls prompt_init() from Apartment and updates it with a dictionary from Rental.
        """
        init = Apartment.prompt_init()
        init.update(Rental.prompt_init())
        return init
    prompt_init = staticmethod(prompt_init)

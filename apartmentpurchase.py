from purchase import Purchase
from apartment import Apartment


class ApartmentPurchase(Purchase, Apartment):
    """
    Has info about apartment purchase.
    """
    def prompt_init():
        """
        Calls prompt_init() from Apartment and updates it with a dictionary from Purchase.
        """
        init = Apartment.prompt_init()
        init.update(Purchase.prompt_init())
        return init
    prompt_init = staticmethod(prompt_init)

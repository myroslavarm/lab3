from purchase import Purchase
from house import House


class HousePurchase(Purchase, House):
    """
    Has info about house purchase.
    """
    def prompt_init():
        """
        Calls prompt_init() from House and updates it with a dictionary from Purchase.
        """
        init = House.prompt_init()
        init.update(Purchase.prompt_init())
        return init
    prompt_init = staticmethod(prompt_init)

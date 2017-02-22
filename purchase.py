class Purchase:
    """
    Contains info about purchases.
    """
    def __init__(self, price='', taxes='', **kwargs):
        """
        Contains info on taxes and prices.
        """
        super().__init__(**kwargs)
        self.price = price
        self.taxes = taxes

    def display(self):
        """
        Displays info about purchases.
        """
        super().display()
        print("PURCHASE DETAILS")
        print("selling price: {}".format(self.price))
        print("estimated taxes: {}".format(self.taxes))

    def prompt_init():
        """
        Reads input and converts it into a dictionary.
        """
        return dict(
            price=input("What is the selling price? "),
            taxes=input("What are the estimated taxes? "))
    prompt_init = staticmethod(prompt_init)

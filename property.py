class Property:
    """
    Base class for Apartment and House. Contains info about property.
    """
    def __init__(self, square_feet='', beds='', baths='', **kwargs):
        """
        Defines and contains info about attributes.
        """
        super().__init__(**kwargs)
        self.square_feet = square_feet
        self.num_bedrooms = beds
        self.num_baths = baths

    def display(self):
        """
        Displays property details.
        """
        print("PROPERTY DETAILS")
        print("================")
        print("square footage: {}".format(self.square_feet))
        print("bedrooms: {}".format(self.num_bedrooms))
        print("bathrooms: {}".format(self.num_baths))
        print()

    def prompt_init():
        """
        Creates a dictionary from input.
        """
        while True:
            try:
                area = input("Enter the square feet: ")
                area = int(area)
                break
            except:
                print("Not a number.")
        return dict(square_feet=area,
                    beds=input("Enter number of bedrooms: "),
                    baths=input("Enter number of baths: "))
    prompt_init = staticmethod(prompt_init)

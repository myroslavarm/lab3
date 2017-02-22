from property import Property


def check():
    """
    Checks whether the class Property is valid.
    >>> check()
    PROPERTY DETAILS
    ================
    square footage: 150
    bedrooms: 2
    bathrooms: 1
    <BLANKLINE>
    """
    property_check = Property()
    property_check.square_feet = 150
    property_check.num_bedrooms = 2
    property_check.num_baths = 1
    property_check.display()

if __name__ == '__main__':
    import doctest
    doctest.testmod()

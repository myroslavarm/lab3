from houserental import HouseRental
from housepurchase import HousePurchase
from apartmentrental import ApartmentRental
from apartmentpurchase import ApartmentPurchase
from apartment import get_valid_input


class Agent:
    """
    Implicitly calls all the functions.
    """
    def __init__(self):
        self.property_list = []

    def display_properties(self):
        """
        Displays all the property with details.
        """
        for property in self.property_list:
            property.display()

    type_map = {
        ("house", "rental"): HouseRental,
        ("house", "purchase"): HousePurchase,
        ("apartment", "rental"): ApartmentRental,
        ("apartment", "purchase"): ApartmentPurchase
    }

    def add_property(self):
        """
        Adds new property.
        """
        property_type = get_valid_input(
            "What type of property? ",
            ("house", "apartment")).lower()
        payment_type = get_valid_input(
            "What payment type? ",
            ("purchase", "rental")).lower()
        PropertyClass = self.type_map[
            (property_type, payment_type)]
        init_args = PropertyClass.prompt_init()
        self.property_list.append(PropertyClass(**init_args))

    def remove_property(self):
        """
        Removes property if there is property to remove.
        """
        if len(self.property_list) == 0:
            print('Nothing to delete.')
            return None
        while True:
            try:
                a = int(input("Enter a number between {} and {}: ".format(1, len(self.property_list))))
                break
            except:
                print('Wrong data.')
        del self.property_list[a - 1]
        print('Done.')

    def house_comparison(self):
        """
        Compares houses' sizes.
        """
        result = 0
        while True:
            try:
                number = input('Input number: ')
                number = int(number)
                break
            except:
                print('Wrong data.')
        for item in self.property_list:
            if item.square_feet >= number:
                item.display()
                result += 1
        if result == 0:
            print('Nothing to show you.')

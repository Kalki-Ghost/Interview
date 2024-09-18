"""Ask user to enter country name. If country exists in the dictionary, print its points with proper message"""
"""If not, print "No such country in points table" """
"""It will ask user again and again until it finds name in dictionary"""

points_table = {'India': 8, 'Pakistan': 6, 'South Africa': 4, 'Bangladesh': 4, 'Netherland': 2, 'Bermuda': 2}


def points():
    try:
        country = input("Enter the country name:")
        value = points_table[country.title()]
    except KeyError:
        print("Key is not present in dictionary.")
        points()
    finally:
        return f"The {country} have {value} points"


print(points())

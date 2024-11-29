# Step 1: Define Class, Constructor, Getters, and Setters
class Polygon:
    def __init__(self, name, sides):
        """Initialize a polygon with a name and a list of side lengths."""
        self.__name = name
        self.__sides = sides

    def get_name(self):
        """Getter for the name of the polygon."""
        return self.__name

    def set_name(self, name):
        """Setter for the name of the polygon."""
        self._name = name

    def get_sides(self):
        """Getter for the sides of the polygon."""
        return self.__sides

    def set_sides(self, sides):
        """Setter for the sides of the polygon."""
        self._sides = sides

    # Step 2: Implement (__eq__) and (__ne__) Methods
    def __eq__(self, other):
        """Check if two polygons are equal by comparing their name and sides."""
        if type(self) == type(other) :
            return self.__name == other.__name and self.__sides == other.__sides
        else:
            False

    def __ne__(self, other):
        """Check if two polygons are not equal."""
        return not self.__eq__(other)

    # Step 3: Implement String Representation (__str__) Method
    def __str__(self):
        """Return a string representation of the polygon."""
        return f"polygon: {self.__name} with sides: {self.__sides}"

    # Step 4: Implement the calculate_circumference Method
    def calculate_circumference(self):
        """Calculate the circumference (sum of all sides) of the polygon."""
        return sum(self.__sides)


# Step 5: Create a Main Script
def main():
    """show how tp use the Polygon class."""
    triangle = Polygon("Triangle", [3, 3, 3])
    square = Polygon("Square", [4,4,4,4])
    hexagon = Polygon("Hexagon", [6, 6, 6, 6, 6, 6])

    print(triangle)
    print("Circumference of triangle:", triangle.calculate_circumference())

    print(square)
    print("Circumference of square:", square.calculate_circumference())

    print(hexagon)
    print("Circumference of hexagon:", hexagon.calculate_circumference())


if __name__ == "__main__":
    main()

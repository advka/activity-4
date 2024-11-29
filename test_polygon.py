import pytest
from polygon import Polygon

# Step 1: Test Initialization, Getters, and Setters
def test_polygon_initialization():
    polygon = Polygon("Triangle", [3, 3, 3])
    assert polygon.get_name() == "Triangle"
    assert polygon.get_sides() == [3, 3, 3]

def test_getters_and_setters():
    polygon = Polygon("Square", [4, 4, 4, 4])
    polygon.set_name("Rectangle")
    polygon.set_sides([4, 6, 4, 6])
    assert polygon.get_name() == "Rectangle"
    assert polygon.get_sides() == [4, 6, 4, 6]

# Step 2: Test Equality and Inequality
def test_polygon_equality():
    poly1 = Polygon("Triangle", [3, 3, 3])
    poly2 = Polygon("Triangle", [3, 3, 3])
    assert poly1 == poly2

def test_polygon_inequality():
    poly1 = Polygon("Triangle", [3, 3, 3])
    poly2 = Polygon("Square", [4, 4, 4, 4])
    assert poly1 != poly2

# Step 3: Test String Representation
def test_polygon_str():
    polygon = Polygon("Hexagon", [6, 6, 6, 6, 6, 6])
    assert str(polygon) == "Hexagon with sides: [6, 6, 6, 6, 6, 6]"

# Step 4: Test Circumference Calculation
def test_calculate_circumference():
    polygon = Polygon("Pentagon", [5, 5, 5, 5, 5])
    assert pytest.approx(polygon.calculate_circumference()) == 25

    polygon = Polygon("Triangle", [3.5, 4.5, 5.0])
    assert pytest.approx(polygon.calculate_circumference()) == 13.0

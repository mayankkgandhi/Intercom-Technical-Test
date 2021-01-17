from pytest import approx, raises
from src.calculate_distance import distance_between_coordinates

# Test for same coordinates
def test_same_location():
    random_coordinates = (53.2707, 9.0568)
    distance = distance_between_coordinates(
        random_coordinates[0], random_coordinates[1],
        random_coordinates[0], random_coordinates[1])
    assert distance == approx(0.000, rel=0.001)

# Test for coordinates given as lists
def test_distance_with_lists():
    random_coordinates = ([53.2707], [9.0568])
    with raises(TypeError):
        assert distance_between_coordinates(
            random_coordinates[0], random_coordinates[1],
            random_coordinates[0], random_coordinates[1])

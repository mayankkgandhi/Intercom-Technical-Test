from math import acos, sin, cos, pi

EARTH_RADIUS = 6371  # in kilometers

def degree_to_radians(degree):
    """
    Calculate radians from degrees by dividing by constant.
    """
    return degree * pi / 180

def distance_between_coordinates(lat1, long1, lat2, long2):
    """
    Calculate distance between given coordinates
    Parameters:
        lat1,long1 : Intercom's coordinates
        lat2,long2 : Customer's coordinates
    Returns:
        Total distance between coordinates
    """
    # Reference: To calulate Great Circle Distance - https://en.wikipedia.org/wiki/Great-circle_distance

    lat1 = float(lat1)
    lat2 = float(lat2)
    long1 = float(long1)
    long2 = float(long2)

    # converting degrees to radians
    lat1 = degree_to_radians(lat1)
    long1 = degree_to_radians(long1)
    lat2 = degree_to_radians(lat2)
    long2 = degree_to_radians(long2)

    # delta between longitudes
    delta_long = abs(long1 - long2)

    # central angle between point 1 and point 2
    central_angle = acos( sin(lat1)
                            * sin(lat2)
                            + cos(lat1)
                            * cos(lat2)
                            * cos(delta_long))


    return EARTH_RADIUS * central_angle

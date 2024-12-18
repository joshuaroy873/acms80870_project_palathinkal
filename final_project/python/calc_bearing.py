import math

def calc_bearing(bs_lat, bs_lon, ue_lat, ue_lon, bs_azimuth):
    """
    Calculate the bearing or azimuth angle of the User Equipment (UE) relative to the sector's orientation.

    This function computes the bearing using the GPS coordinates of the UE and the sector's orientation.
    The resulting angle indicates the direction of the UE concerning the sector it is connected to and 
    serves as an essential parameter for further antenna calculations.

    Parameters:
    bs_lat (float): Latitude of the base station (in degrees).
    bs_lon (float): Longitude of the base station (in degrees).
    ue_lat (float): Latitude of the user equipment (in degrees).
    ue_lon (float): Longitude of the user equipment (in degrees).
    bs_azimuth (float): Azimuth angle of the base station (in degrees).

    Returns:
    float: The azimuth angle of the UE relative to the sector's orientation, rounded to two decimal places.
    """
    bs_lat_rad = math.radians(bs_lat)
    bs_lon_rad = math.radians(bs_lon)
    ue_lat_rad = math.radians(ue_lat)
    ue_lon_rad = math.radians(ue_lon)
    dlon = ue_lon_rad - bs_lon_rad
    x = math.sin(dlon) * math.cos(ue_lat_rad)
    y = math.cos(bs_lat_rad) * math.sin(ue_lat_rad) - (math.sin(bs_lat_rad) * math.cos(ue_lat_rad) * math.cos(dlon))
    initial_bearing = math.atan2(x, y)
    initial_bearing = math.degrees(initial_bearing)
    compass_bearing = (initial_bearing + 360) % 360
    ue_azimuth = (compass_bearing - bs_azimuth + 360) % 360
    return round(ue_azimuth,2)
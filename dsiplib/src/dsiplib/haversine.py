import numpy as np

## Function to calculate the haversine of two lat-lon pair

def haversine(ue_lat, ue_lon, bs_lat, bs_lon, bs_height, rx_height=1.5):
    """
    Calculate the 2D and 3D distances between two points on the Earth's surface using the Haversine formula.

    Parameters:
    ue_lat (float): Latitude of the user equipment (UE) in degrees.
    ue_lon (float): Longitude of the user equipment (UE) in degrees.
    bs_lat (float): Latitude of the base station (BS) in degrees.
    bs_lon (float): Longitude of the base station (BS) in degrees.
    bs_height (float): Height of the base station (BS) in meters.
    rx_height (float, optional): Height of the receiver (default is 1.5 meters).

    Returns:
    tuple: A tuple containing:
        - distance_2d (float): The 2D distance between the two points in meters.
        - distance_3d (float): The 3D distance between the two points in meters, accounting for height difference.
    """
    lat1_rad = np.radians(ue_lat)
    lon1_rad = np.radians(ue_lon)
    lat2_rad = np.radians(bs_lat)
    lon2_rad = np.radians(bs_lon)
    dlat = lat2_rad - lat1_rad
    dlon = lon2_rad - lon1_rad
    a = np.sin(dlat/2)**2 + np.cos(lat1_rad)*np.cos(lat2_rad)*np.sin(dlon/2)**2
    c = 2*np.arctan2(np.sqrt(a),np.sqrt(1-a))
    r = 6371  # Radius of the Earth in kilometers
    distance_2d = c * r * 1e3
    distance_3d = np.sqrt(distance_2d**2 + (bs_height-rx_height)**2)
    return distance_2d, distance_3d
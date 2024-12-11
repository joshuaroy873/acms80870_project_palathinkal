import numpy as np

## Function to calculate the haversine of two lat-lon pair

def haversine(ue_lat, ue_lon, bs_lat, bs_lon, bs_height, rx_height=1.5):
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
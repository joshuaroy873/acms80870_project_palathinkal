import math

def calc_bearing(bs_lat, bs_lon, ue_lat, ue_lon, bs_azimuth):
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
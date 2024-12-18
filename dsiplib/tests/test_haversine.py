from dsiplib import haversine

def test_haversine():
    ue_lat, ue_lon = 52.5200, 13.4050  # Berlin
    bs_lat, bs_lon = 48.8566, 2.3522   # Paris
    bs_height = 50  # Base station height in meters

    distance_2d, distance_3d = haversine(ue_lat, ue_lon, bs_lat, bs_lon, bs_height)

    # Validate distances
    assert round(distance_2d / 1e3, 1) == 878.1  # ~878 km
    assert distance_3d > distance_2d  # 3D distance should be larger
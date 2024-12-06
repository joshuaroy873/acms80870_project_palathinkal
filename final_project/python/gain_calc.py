from scipy.interpolate import interp1d
import numpy as np

def gain_calc(df_antenna, ue_azimuth, ue_elevation):
    gain_azimuth = df_antenna['gain_azimuth'].values
    angle_azimuth = df_antenna['angle_azimuth'].values
    azimuth_gain_interp = np.interp(ue_azimuth, angle_azimuth, gain_azimuth)
    gain_elevation = df_antenna['gain_elevation'].dropna().values
    angle_elevation = df_antenna['angle_elevation'].dropna().values
    elevation_interpolation_fn = interp1d(angle_elevation,gain_elevation, kind='linear') # Strangely, np.interp() is not working for elevation.
    # Figured it out! angle_elevation is in decreasing order instead of increasing order. Will change it to np.interp() later.
    elevation_gain_interp = elevation_interpolation_fn(ue_elevation)
    gain_total = azimuth_gain_interp * elevation_gain_interp
    return azimuth_gain_interp, elevation_gain_interp
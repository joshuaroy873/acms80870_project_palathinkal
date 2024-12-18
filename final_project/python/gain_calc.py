from scipy.interpolate import interp1d
import numpy as np

def gain_calc(df_antenna, ue_azimuth, ue_elevation):
    """
    Calculate the interpolated antenna gain for given azimuth and elevation angles.

    Parameters:
    df_antenna (pd.DataFrame): DataFrame containing antenna gain data with columns 'gain_azimuth', 'angle_azimuth', 'gain_elevation', and 'angle_elevation'.
    ue_azimuth (float): User equipment azimuth angle in degrees.
    ue_elevation (float): User equipment elevation angle in degrees.

    Returns:
    tuple: A tuple containing:
        - azimuth_gain_interp (float): Interpolated gain value for the given azimuth angle.
        - elevation_gain_interp (float): Interpolated gain value for the given elevation angle.
    """
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
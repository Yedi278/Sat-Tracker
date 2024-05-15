from Epoch import*

class TLE:
    
    name = None
    NORAD_ID = None
    International_designation_ID = None
    Epoch = None
    First_time_derivative_of_the_mean_motion = None
    Second_time_derivative_of_mean_motion = None
    BSTAR_drag_term = None
    Ephemeris_type = None
    Element_set_number = None
    Inclination = None
    Right_ascension_of_the_ascending_node = None
    Eccentricity = None
    Argument_of_perigee = None
    Mean_anomaly = None
    Mean_motion = None
    Revolution_count_at_epoch = None
    
    def __init__(self, TLE_data_dict: dict):
        self.__dict__ = TLE_data_dict
        self.name = TLE_data_dict.get('name', '')
        self.NORAD_ID = TLE_data_dict.get('NORAD ID', '')
        self.International_designation_ID = TLE_data_dict.get('International designation ID', '')
        self.Epoch = TLE_data_dict.get('Epoch', '')
        self.First_time_derivative_of_the_mean_motion = TLE_data_dict.get('First time derivative of the mean motion', '')
        self.Second_time_derivative_of_mean_motion = TLE_data_dict.get('Second time derivative of mean motion', '')
        self.BSTAR_drag_term = TLE_data_dict.get('BSTAR drag term', '')
        self.Ephemeris_type = TLE_data_dict.get('Ephemeris type', '')
        self.Element_set_number = TLE_data_dict.get('Element set number', '')
        self.Inclination = TLE_data_dict.get('Inclination', '')
        self.Right_ascension_of_the_ascending_node = TLE_data_dict.get('Right ascension of the ascending node', '')
        self.Eccentricity = TLE_data_dict.get('Eccentricity', '')
        self.Argument_of_perigee = TLE_data_dict.get('Argument of perigee', '')
        self.Mean_anomaly = TLE_data_dict.get('Mean anomaly', '')
        self.Mean_motion = TLE_data_dict.get('Mean motion', '')
        self.Revolution_count_at_epoch = TLE_data_dict.get('Revolution count at epoch', '')

    def __str__(self):
        return f'\nTLE data for \033[95m{self.name}\x1b[0m \nNORAD ID: {self.NORAD_ID}\nEpoch: {self.Epoch}\nInclination: {self.Inclination}\nRight ascension of the ascending node: {self.Right_ascension_of_the_ascending_node}\nEccentricity: {self.Eccentricity}\nArgument of perigee: {self.Argument_of_perigee}\nMean anomaly: {self.Mean_anomaly}\nMean motion: {self.Mean_motion}\n'

    def epoch_to_utc(self, dict:bool=False):
        time,time_d = epochToUTC(self.Epoch)
        if dict:
            return time_d
        return time
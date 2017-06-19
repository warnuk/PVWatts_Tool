import pvwatts_request
import process_output

datetime_reference = "resources/datetime_defaults.csv"

class PVWatts_Run(object):
    def __init__(self, area, module_type, lat, lon, losses,
                array_type, tilt, azimuth, timeframe):
        '''PVWatts_Run object takes location/system attributes to
        call PVWatts API and assign output to its output attribute'''
        self.area = area
        self.module_type = module_type
        self.lat = lat
        self.lon = lon
        self.losses = losses
        self.array_type = array_type
        self.tilt = tilt
        self.azimuth = azimuth
        self.timeframe = timeframe

        self.output = pvwatts_request.get_output(area = self.area,
                                                module_type = self.module_type,
                                                lat = self.lat,
                                                lon = self.lon,
                                                losses = self.losses,
                                                array_type = self.array_type,
                                                tilt = self.tilt,
                                                azimuth = self.azimuth,
                                                timeframe = self.timeframe)

        self.hourly_data = process_output.populate_df(self.output,
                            template=datetime_reference)

        self.daily_data = process_output.kW_per_day(self.hourly_data)

        self.max = process_output.peak_days(self.daily_data)['max']
        self.max_ratio = self.max.iloc[0,2]/self.area

        self.min = process_output.peak_days(self.daily_data)['min']
        self.min_ratio = self.min.iloc[0,2]/self.area

        self.median = process_output.peak_days(self.daily_data)['median']
        self.median_ratio = self.median.iloc[0,2]/self.area

        self.annual_ratio = self.output['ac_annual']/self.area

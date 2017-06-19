import pvwatts_request

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

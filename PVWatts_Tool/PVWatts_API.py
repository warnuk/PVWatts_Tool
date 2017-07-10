"""PVWAtts_API.py
by warnuk

This module uses the request functions from the nrel_requests module to build an object for each scenario and
assign that object attributes which are called to deliver output.

The PVWatts_Run object collects the necessary parameters to make a request to the PVWatts API as attributes.
Hourly output, annual production, max/min/median days, and rate information are stored as attributes as well."""

from PVWatts_Tool import nrel_requests
from PVWatts_Tool import process_output

__author__ = "warnuk"
__credits__ = ["warnuk", "NREL", "PVWatts"]
__license__ = "MIT"
__version__ = "1.0.5"
__maintainer__ = "warnuk"
__email__ = "warnuk@umich.edu"
__status__ = "Development"
datetime_reference = "datetime_defaults.csv"

class PVWatts_Run(object):
    def __init__(self, api_key, area, module_type, lat, lon, losses,
                 array_type, tilt, azimuth, timeframe, ratetype, incentivized):
        """PVWatts_Run object takes location/system attributes to
        call PVWatts API and assign output to its output attribute"""
        self.api_key = api_key
        self.area = area
        self.module_type = module_type
        self.lat = lat
        self.lon = lon
        self.losses = losses
        self.array_type = array_type
        self.tilt = tilt
        self.azimuth = azimuth
        self.timeframe = timeframe
        self.ratetype = ratetype
        self.incentivized = incentivized

        # Use proper efficiency rating for module_type.
        if self.module_type == 0:
            self.system_capacity = round(0.15 * self.area, 1)
        elif self.module_type == 1:
            self.system_capacity = round(0.19 * self.area, 1)
        elif self.module_type == 2:
            self.system_capacity = round(0.1 * self.area, 1)

        self.pvwatts_output = nrel_requests.pvwatts_output(api_key=self.api_key,
                                                           system_capacity=self.system_capacity,
                                                           module_type=self.module_type,
                                                           lat=self.lat,
                                                           lon=self.lon,
                                                           losses=self.losses,
                                                           array_type=self.array_type,
                                                           tilt=self.tilt,
                                                           azimuth=self.azimuth,
                                                           timeframe=self.timeframe)

        self.utility_output = nrel_requests.utility_output(lat=self.lat, lon=self.lon, api_key=self.api_key)

        self.util_name = self.utility_output['utility_name']
        self.rate = self.utility_output[self.ratetype]

        self.ac_annual = self.pvwatts_output['ac_annual']

        self.energy_value = round(self.ac_annual * self.rate, 2)

        # EIA AEO 2017 estimates LCOE of solar pv to be $77.7 / MWh, or $58.8 / MWh with tax credits
        if self.incentivized:
            self.cost = round(self.ac_annual * (58.8 / 1000), 2)
        else:
            self.cost = round(self.ac_annual * (77.7 / 1000), 2)

        self.savings = round(self.energy_value - self.cost, 2)

        self.hourly_data = process_output.populate_df(self.pvwatts_output)

        self.daily_data = process_output.kW_per_day(self.hourly_data)

        self.max = process_output.peak_days(self.daily_data)['max']
        self.max_ratio = self.max.iloc[0, 2] / self.area

        self.min = process_output.peak_days(self.daily_data)['min']
        self.min_ratio = self.min.iloc[0, 2] / self.area

        self.median = process_output.peak_days(self.daily_data)['median']
        self.median_ratio = self.median.iloc[0, 2] / self.area

        self.annual_ratio = self.pvwatts_output['ac_annual'] / self.area

    def describe(self):
        return (f"System Capacity: {self.system_capacity} (kWdc)"
                f"\n\nPeak Day (max) Ratio: {self.max_ratio} (kWh/m^2/day)"
                f"\nLow Day (min) Ratio: {self.min_ratio} (kWh/m^2/day)"
                f"\nAvg. Day (median) Ratio: {self.median_ratio} (kWh/m^2/day)"
                f"\nAnnual Ratio: {self.annual_ratio} (kWh/m^2/yr)"
                f"\n\nAnnual AC Solar Potential: {self.ac_annual} (kWh)"
                f"\nUtility: {self.util_name}"
                f"\nRate: ${self.rate}/kWh"
                f"\nEnergy Value: ${self.energy_value}"
                f"\nEstimated Cost: ${self.cost}"
                f"\nEstimated Savings: ${self.savings}")

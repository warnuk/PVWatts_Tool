#!/usr/bin/env python
import PVWatts_API

standard_fixed = PVWatts_API.PVWatts_Run(area=1, module_type=0,
                                    lat="42.3", lon="-83.7", losses="14",
                                    array_type="0", tilt="34",
                                    azimuth="180", timeframe="hourly")

standard_rooftop = PVWatts_API.PVWatts_Run(area=1, module_type=0,
                                    lat="42.3", lon="-83.7", losses="14",
                                    array_type="1", tilt="34",
                                    azimuth="180", timeframe="hourly")

standard_rotating = PVWatts_API.PVWatts_Run(area=1, module_type=0,
                                    lat="42.3", lon="-83.7", losses="14",
                                    array_type="4", tilt="34",
                                    azimuth="180", timeframe="hourly")

premium_fixed = PVWatts_API.PVWatts_Run(area=1, module_type=1,
                                    lat="42.3", lon="-83.7", losses="14",
                                    array_type="0", tilt="34",
                                    azimuth="180", timeframe="hourly")

premium_rooftop = PVWatts_API.PVWatts_Run(area=1, module_type=1,
                                    lat="42.3", lon="-83.7", losses="14",
                                    array_type="1", tilt="34",
                                    azimuth="180", timeframe="hourly")

premium_rotating = PVWatts_API.PVWatts_Run(area=1, module_type=1,
                                    lat="42.3", lon="-83.7", losses="14",
                                    array_type="4", tilt="34",
                                    azimuth="180", timeframe="hourly")

print("Ratios for Standard-Fixed Arrays:")
standard_fixed.describe()

print("Ratios for Standard-Rooftop Arrays:")
standard_rooftop.describe()

print("Ratios for Standard-Rotating Arrays:")
standard_rotating.describe()

print("Ratios for Premium-Fixed Arrays:")
premium_fixed.describe()

print("Ratios for Premium-Rooftop Arrays:")
premium_rooftop.describe()

print("Ratios for Premium-Rotating Arrays:")
premium_rotating.describe()

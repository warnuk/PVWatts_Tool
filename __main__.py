#!/usr/bin/env python
import PVWatts_API

run = PVWatts_API.PVWatts_Run(area=1, module_type=0,
                                    lat="42.3", lon="-83.7", losses="14",
                                    array_type="0", tilt="34",
                                    azimuth="180", timeframe="hourly")

print(run.max_ratio, run.min_ratio, run.median_ratio, run.annual_ratio,
        sep="\n")

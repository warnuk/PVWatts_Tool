#!/usr/bin/env python
import PVWatts_API
import process_output

datetime_reference = "resources/datetime_defaults.csv"

run = PVWatts_API.PVWatts_Run(area=1000, module_type=0,
                                    lat="42.3", lon="-83.7", losses="14",
                                    array_type="0", tilt="34",
                                    azimuth="180", timeframe="hourly")

print(process_output.populate_df(run.output,
        template=datetime_reference).head(24))

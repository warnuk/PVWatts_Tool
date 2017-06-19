#!/usr/bin/env python
import PVWatts_API
import process_output

datetime_reference = "resources/datetime_defaults.csv"

run = PVWatts_API.PVWatts_Run(area=1000, module_type=0,
                                    lat="42.3", lon="-83.7", losses="14",
                                    array_type="0", tilt="34",
                                    azimuth="180", timeframe="hourly")

hourly_data = process_output.populate_df(run.output,
                    template=datetime_reference)

daily_data = process_output.kW_per_day(hourly_data)

summary_days = process_output.peak_days(daily_data)

for case in summary_days:
    print(case, summary_days[case], sep='\n')
    print('\n')

""""nrel_requests.py
by warnuk

This module contains functions that take input parameters and call the PVWatts API and Utility Rates API."""

import requests

__author__ = "warnuk"
__credits__ = ["warnuk", "NREL", "PVWatts"]
__license__ = "MIT"
__version__ = "1.0.1"
__maintainer__ = "warnuk"
__email__ = "warnuk@umich.edu"
__status__ = "Development"

def pvwatts_output(system_capacity, module_type, api_key, **kwargs):
    """ Uses the PVWatts API to retrieve output from PVWatts API for given inputs."""

    # Define url and individual params seperately.
    url = "https://developer.nrel.gov/api/pvwatts/v5.json?"
    system_capacity = str(system_capacity)
    module_type = str(module_type)
    # Join params and url together to form request statement.
    params = "api_key=%s&system_capacity=%s&module_type=%s" %(api_key,system_capacity,module_type)
    for key, value in kwargs.items():
        params += "&%s=%s" % (key, value)
    params += "&format=JSON"
    request = url + params
    outputs = requests.get(request).json()['outputs']
    return(outputs)

def utility_output(lat, lon, api_key):
    """ utility_output uses the NREL Utility Rates API to retrieve
    utility info/rates for a given location"""

    url = "https://developer.nrel.gov/api/utility_rates/v3.json?"
    params = f"api_key={api_key}&lat={lat}&lon={lon}"
    request = url + params
    outputs = requests.get(request).json()['outputs']
    return(outputs)


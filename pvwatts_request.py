import requests


def pvwatts_output(area, module_type, **kwargs):
    """ pvwatts_output uses the PVWatts API to retrieve output from PVWatts API
    for given inputs."""
    # use proper efficiency rating for module_type
    if module_type == 0:
        efficiency = .15
    elif module_type == 1:
        efficiency = .19
    elif module_type == 2:
        efficiency = .1
    # calculate system_capacity
    system_capacity = area * efficiency
    # define url and individual params seperately
    url = "https://developer.nrel.gov/api/pvwatts/v5.json?"
    api_key = "9YITybCEf9bCw7Kd2ykYGppgJFSjHd9qWlNd09bS"
    system_capacity = str(system_capacity)
    module_type = str(module_type)
    #join params and url together to form request statement
    params = "api_key=%s&system_capacity=%s&module_type=%s" %(api_key,system_capacity,module_type)
    for key, value in kwargs.items():
        params += "&%s=%s" % (key, value)
    params += "&format=JSON"
    request = url + params
    outputs = requests.get(request).json()['outputs']
    return(outputs)

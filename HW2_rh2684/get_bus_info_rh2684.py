# Author: Ruben Hambardzumyan

# Importing libraries

from __future__ import print_function
import os
import json
import sys
import pandas as pd

try:
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib
	
# Defining parameters for console, <PROGRAM_NAME> <MTA_KEY> and <BUS_LINE>

programName = sys.argv[0] # Program name
apikey = sys.argv[1] # Utilizes the MTA apikey, i.e. $MTA_KEY
busLine = sys.argv[2] # Specifies the Bus Line, i.e. B54
outputFile = sys.argv[3] # Specifies the output .csv file name, i.e. B54

if not len(sys.argv) == 4:
    print ("Invalid number of arguments. Run example: script.py $MTA_KEY B61 B61")
    sys.exit()

# Constucting the MTA URL

url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s"%(apikey, busLine)

response = urllib.urlopen(url)

data = response.read().decode("utf-8")
data = json.loads(data)

# Output to CSV using pandas empty DataFrame

df = pd.DataFrame()

# Constructing the output

for item in data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']:
	busID = (item['MonitoredVehicleJourney']['VehicleRef'])
	latitude = (item['MonitoredVehicleJourney']['VehicleLocation']['Latitude'])
	longitude = (item['MonitoredVehicleJourney']['VehicleLocation']['Longitude'])
	stopName = (item['MonitoredVehicleJourney']['MonitoredCall']['StopPointName'])
	stopStatus = (item['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['Extensions']['Distances']['PresentableDistance'])
	busData = [{
        "Bus ID" : busID,
		"Latitude" : latitude,
		"Longitude" : longitude,
		"Stop Name" : stopName,
		"Stop Status" : stopStatus
		}]
	df = df.append(busData)

# Replacing the empty stop statuses with N/A

stopName = stopName.replace("", "N/A")
stopStatus = stopStatus.replace("", "N/A")

# Generating output
		
df.to_csv(outputFile + ".csv", index = False)
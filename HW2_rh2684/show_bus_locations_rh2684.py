# Author: Ruben Hambardzumyan

# Importing libraries

from __future__ import print_function
import os
import json
import sys

try:
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib
	
# Defining parameters for console, <PROGRAM_NAME> <MTA_KEY> and <BUS_LINE>

programName = sys.argv[0] # Program name
apikey = sys.argv[1] # Utilizes the MTA apikey
busLine = sys.argv[2] # Specifies the Bus Line number, i.e. B54

if not len(sys.argv) == 3:
    print ("Invalid number of arguments. Run example: script.py $MTA_KEY B61")
    sys.exit()

# Constucting the MTA URL

url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s"%(apikey, busLine)

response = urllib.urlopen(url)

data = response.read().decode("utf-8")
data = json.loads(data)

# Getting the total amount of active buses

busNumber = len(data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'])

# Constructing the output

print("Bus Line : " + sys.argv[2])
print("Number of Active Buses : " + str(busNumber))

busID = 0 #replacing the VehicleRef with an ID number

for item in data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']:
	print("Bus " + item['MonitoredVehicleJourney']['VehicleRef'].replace(item['MonitoredVehicleJourney']['VehicleRef'], str(busID)) + " with the ID of " + item['MonitoredVehicleJourney']['VehicleRef'] + " is at lattitude " + str(item['MonitoredVehicleJourney']['VehicleLocation']['Latitude']) + " and longitude " + str(item['MonitoredVehicleJourney']['VehicleLocation']['Longitude']))
	busID += 1
from stravalib.client import Client, unithelper
import logging

logging.basicConfig(level=logging.ERROR)

client = Client(access_token='access_token')

total_distance = 0.0
for activity in client.get_activities(after = "2015-04-06T00:00:00Z"):
    #print dir(activity)
    #break
    print("{}: {}").format(activity.start_date_local, unithelper.kilometers(activity.distance))
    total_distance += float(unithelper.kilometers(activity.distance))

print "Total distance: %.2fkm" % total_distance

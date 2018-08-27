import os
import sys
import competitor_locations as cl
from googlemaps import Client as GoogleMaps

print("imported Distance_Search")

api_key = 'DELETED'
gmaps = GoogleMaps(api_key)

locations = [
    '7600 Kennedy Rd, Markham, ON L3R 9S5',
    '3201 Bur Oak Ave, Markham, ON L6B 0T2',
    '7755 Bayview Ave., Thornhill, ON L3T 7R3',
    '501 Clark Ave. West, Thornhill, ON L4J 4E5',
    '1441 Clark Avenue West, Thornhill, ON L4J 7R4',
    '10190 Keele St., Maple, ON L6A 1R7',
    '9201 Islington Ave., Woodbridge, ON L4L 1A7',
    ]

def distance_to_location(start_location, end_location):
    dirs = gmaps.directions(start_location, end_location, mode="walking")[0]
    dirs_specific1 = dirs['legs'][0]
    dirs_distance = dirs_specific1['distance']['value']
    return dirs_distance
    # takes location #1 and location #2 and checks distance between them in meters

def smallest_distance(start_location, list_of_locations):
    distances = []
    for index, item in enumerate(list_of_locations):
        try:
            distances.insert(index, distance_to_location(start_location, item))
        except: # catches all errors
            distances.insert(index, '')
    return list_of_locations[distances.index(min(distances))], min(distances)
    # takes location #1 and a list of locations and finds the smallest distance

# -*- coding: utf-8 -*-
"""
Created on Thu Jan 17 23:50:53 2019

@author: ADITYA
"""

import ad_utils
import generate_road_name
    
import numpy as np
import pandas as pd

stats = ad_utils.major_minor_stat_creation(r'F:\Files\MajorProject\RAP-ter-master\Data\AADF-data-major-roads.csv', r'F:\Files\MajorProject\RAP-ter-master\Data\AADF-data-minor-roads.csv', 2017)
roadAccidentsSet = ad_utils.stats_set_creation(stats, 'Road')
roadName = generate_road_name.road_name()

roadAccidentsSetUpdated, unassignedRoads = ad_utils.accident_flows(roadAccidentsSet, roadName)
setOfUnassignedRoads = set(unassignedRoads)                                                 #Creating a set of unassigned roads

alteredRoadAccident = ad_utils.road_stats(roadAccidentsSet, stats)
alteredRoadAccident = ad_utils.average_road_stats(alteredRoadAccident)

##Function that takes the roadAccidentSet(Roads and respective number of Accidents on that road) and roadName (Road on which an accident occured) as input and returns updated roadAccidentSet
#def accident_flows(roadAccidentsSet, roadName):
#    unassignedRoads = []
#    for road in roadName:
#        if road in roadAccidentsSet:
#            tempLocation = np.where(roadAccidentsSet == road)                               #The location where the road is in roadAccidentSet
#            indexToBeInc = tempLocation[1][0]                                               #The index of that location that need to be incremented
#            roadAccidentsSet[1][indexToBeInc] = roadAccidentsSet[1][indexToBeInc] + 1       #Incrementing the count on that index
#        else:
#            unassignedRoads.append(road)
#            
#        unassignedRoads = np.array(unassignedRoads)
#    return roadAccidentsSet, unassignedRoads
#!/usr/bin/python
import folium
import csv

infile = "data.csv"

portland = folium.Map(location=[40.75007, -73.9794], tiles='Stamen Toner',
                      zoom_start=13)

with open(infile, 'rb') as csvfile:
     data = csv.reader(csvfile, delimiter=',', quotechar='"')
     i = 0
     for row in data:
         #print ', '.join(row)
         i += 1
         if i > 100:
             break
         slat = row[5]
         slon = row[6]
         elat = row[9]
         elon = row[10]
         startname = row[4]
         print slat, slon
         #ml.line(locations=[[slat,slon],[elat,elon]], line_color='#FF0000', line_weight=5)
         folium.Marker([slat, slon], popup=startname).add_to(portland)

portland.create_map(path="startpoints.html")

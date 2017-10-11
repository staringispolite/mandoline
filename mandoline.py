#!usr/bin/python
import csv

segments = []

# Read in segments DB
# Format: filename, start time(sec), end time(sec), posted (0/1)
with open('segments.db', 'rb') as segmentfile:
  segmentreader = csv.reader(segmentfile)
  for row in segmentreader:
    #row.append(0)  # Add "posted" row, starting with none posted  
    segments.append(row)
    print row

# Write segment DB to disk
with open('segments.db', 'wb') as segmentdb_file:
  segmentwriter = csv.writer(segmentdb_file)
  for row in segments:
    segmentwriter.writerow(row)

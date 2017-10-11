#!usr/bin/python
import csv

segments = []

# Read in segments DB
with open('segment_list.txt', 'rb') as segmentfile:
  segmentreader = csv.reader(segmentfile)
  for row in segmentreader:
    row.append("0") # set to not posted
    segments.append(row)
    print row

# Write segment DB to disk
with open('segments.db', 'wb') as segmentdb_file:
  segmentwriter = csv.writer(segmentdb_file)
  for row in segments:
    segmentwriter.writerow(row)

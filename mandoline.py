#!usr/bin/python
import argparse
import csv
import random
from subprocess import call

# CSV column definitions
FILENAME = 0
TIMESTART = 1
TIMESTOP = 2
POSTED = 3

def buildHashtags():
  possibles = ["#trains", "#train", "#training", "#trainspotting",
      "#slowtrainkeepsonrolling", "#norway", "#choochoo",
      "#railroads", "#rail", "#trainstation", "#locomotive",
      "#clouds", "#outside", "#nature", "#slowtv", "#snow", "#trees",
      "#landscape", "#landscapelovers", "#mountains", "#naturelovers",
      "#outside", "#travel", "#backpacking", "#travelling", "#travelgram",
      "#traintracks", "#followtrain", "#sky", "#winter", "#winterwonderland",
      "#fall", "#leaves", "seasons", "#instamood", "#video", "#relaxing",
      "#autumn", "#traveltheworld"]
  random.shuffle(possibles)
  used = possibles[:10]
  return " ".join(used)

# Build a comment based on randomized hashtags and templates
def buildComment(segment):
  return "On my way across Norway! Wheeee %s" % buildHashtags()


next_to_upload_id = 0
segments = []
parser = argparse.ArgumentParser(description='Upload segments of video to Instagram')
parser.add_argument('--basepath', dest='path', default="./",
    help="The absolute path (ending in /) to a directory containing segment files and a segment list from ffmpeg")
args = parser.parse_args()

# Read in segments DB
# Format: filename, start time(sec), end time(sec), posted (0/1)
with open("%s%s" % (args.path, 'segments.db'), 'rb') as segmentfile:
  segmentreader = csv.reader(segmentfile)
  for row in segmentreader:
    #row.append(0)  # Add "posted" row, starting with none posted  
    #print row
    segments.append(row)

# Find first that hasn't been posted.
i = 0
for row in segments:
  if row[POSTED] == "0":
    next_to_upload_id = i
    break
  i += 1

# Post to IG
username = ''
password = ''
filename = "%s%s" % (args.path, segments[next_to_upload_id][FILENAME])
comment = buildComment(segments[next_to_upload_id])
print "Posting %s..." % filename
print "Comment: %s" % comment
command = "php %s../upload.php %s %s %s \"%s\"" % (
    args.path, username, password, filename, comment)
print "Calling command %s" % command
call(command, shell=True)

segments[next_to_upload_id][POSTED] = 1

# Write segment DB to disk
with open("%s%s" % (args.path, 'segments.db'), 'wb') as segmentdb_file:
  segmentwriter = csv.writer(segmentdb_file)
  for row in segments:
    segmentwriter.writerow(row)


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
  possibles = ["All aboard!", "On my way across Norway!", "Wheeeee", "let's gooo",
      "On my way from Bergen to Oslo", "In the mountains of Norway", "slow & steady",
      "Chugging along", "I am quite slow, but I'm also determined", "steady as she goes",
      "Here we go!", "Norway is the world's largest exporter of salmon. I am a train.",
      "Slow and steady wins the race to Oslo", "Somewhere in the mountains of Norway",
      "tracks for days", "Almost there! (jk it is quite far)", "Somewhere between Bergen and Oslo",
      "Wait am I lost?", "Are... we going in circles?", "Deja vu is common in trains bc we do the same route over and over",
      "I love this part", "Check this part out", "Ooh I saw a moose back there",
      "CHUG-a-chug-a-chug-a-chug-a-chuga...", "choo choooo", "I am a train", "I am quite slow",
      "What I make for in speed, I make up for in social media use",
      "Am I carrying freight or passengers? I can't see back there",
      "Brrr it's cold today", "Great weather today!", "tunnels are my favorite. I wonder if there's one coming up",
      "Bridges are scary. They're too high, and I'm heavy", "I wish I spoke more Norwegian",
      "Hallo", "Hallo, I am a train", "Hallo! Can anyone teach me more Norwegian?",
      "Hei", "Heisann", "Hei pa deg", "Halla", "Hei hei", "I learned some Norwegian! Jeg er et tog",
      "Heading to Whole Foods, want anything",
      "Fun fact: Norwegians founded Dublin, Ireland, in A.D. 836",
      "Fun fact: Norway was originally Nordweg, or the 'Northern Way'. Northern -> North -> Nor' Way?",
      "Fun fact: Norway's formal name is Kongeriket Norge (Kingdom of Norway)",
      "Fun fact: The cheese slicer was invented in Norway in 1925 by Thor Bjorklund",
      "Fun fact: early trains were pulled by horses. Not me though.",
      "Fun fact: The first travel agency started for a train ride, when Thomas Cook a church trip",
      "I know a train that carries ore from mines in the mountains of Sweden down to Narvik in Norway. It generates more electricity than it uses, and powers nearby towns.",
      "Someone just told me you can travel from Portugal to Vietnam, just by train",
      "Did you know the Hogwarts Express Train is played by my friend, a train in Scotland?",
      "Most train horns are based on musical chords. Passenger trains are nice Major 6th chords",
      "Most train horns are based on musical chords. Freight trains are usually something unpleasant, like diminished 7th chords"
      ]
  random.shuffle(possibles)
  commentUsed = possibles[0]
  return "%s %s" % (commentUsed, buildHashtags())


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


# mandoline

## Slice video into 30 second segments, post to Instagram over time

## Setup
- install ffmpeg
- download video
- `> ffmpeg -i video.mp4 -codec copy -f segment -reset_timestamps 1 -segment_list segment_list.txt -segment_list_type csv -segment_time 30 segment%03d.mp4`



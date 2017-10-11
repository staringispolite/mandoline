# mandoline

## Slice video into 30 second segments, post to Instagram over time

## Setup
- Install PHP and composer https://getcomposer.org/doc/00-intro.md#globally
- Install Instagram PHP API https://github.com/mgp25/Instagram-API

## Video splitting
- install ffmpeg
- Split video (assuming it's ./video.mp4)
- `> ffmpeg -i video.mp4 -codec copy -f segment -reset_timestamps 1 -segment_list segment_list.txt -segment_list_type csv -segment_time 30 segment%03d.mp4`
- Scale down if need be (Instagram only accepts 480p-720p width as of this writing)
- `mkdir scaled`
- `> find . -name "segment*.mp4" -exec ffmpeg -i {} -vf scale=720:404 ./scaled/{} \;`
- Optional: Split out story videos (can only be 15 seconds, using 14sec because copy codec can be imprecise). For example:
- `cd scaled; mkdir story`
- `find . -name "segment*.mp4" -exec echo ffmpeg -ss 0:00 -i {} -t 14 -c copy story/{} \;`

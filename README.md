# mandoline

## Slice video into 30 second segments, post to Instagram over time

## Setup
- Install PHP and composer https://getcomposer.org/doc/00-intro.md#globally
- Install Instagram PHP API https://github.com/mgp25/Instagram-API

## Video splitting
- install ffmpeg
- assuming video to split is video.mp4
- `> ffmpeg -i video.mp4 -codec copy -f segment -reset_timestamps 1 -segment_list segment_list.txt -segment_list_type csv -segment_time 30 segment%03d.mp4`



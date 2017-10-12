# mandoline

## Slice video into 30 second segments, post to Instagram over time

## Setup on Digital Ocean:
- DigitalOcean LAMP server (really just need Linux and PHP)
- `apt install curl php-curl php7.0-mbstring zip unzip php7.0-zip ffmpeg ubuntu-restricted-extras` 
- Install composer https://getcomposer.org/doc/00-intro.md#globally
- Install Instagram PHP API https://github.com/mgp25/Instagram-API
- Install Google Chrome https://askubuntu.com/a/510063
- Install pip and upgrade it
- Install InstaPy https://github.com/timgrossmann/InstaPy
- Install the right chrome driver -> InstaPy/assets
- Install all the packages here https://github.com/timgrossmann/InstaPy/issues/35
- `cd InstaPy; cp -r instapy /path/to/mandoline/; ln is /path/to/mandoline/likes.py your_project_name.py`

## Setup on Macbook:
- Install PHP, Python, ffmpeg
- Install composer https://getcomposer.org/doc/00-intro.md#globally
- Install Instagram PHP API https://github.com/mgp25/Instagram-API
- Install InstaPy https://github.com/timgrossmann/InstaPy
- Install the right chrome driver -> InstaPy/assets
- Install packages as they error (use `pip install --user` to avoid OS X El Capitan filesystem perms errors)

## Video splitting:
- Split video (assuming it's ./video.mp4)
- `> ffmpeg -i video.mp4 -codec copy -f segment -reset_timestamps 1 -segment_list segment_list.txt -segment_list_type csv -segment_time 30 segment%03d.mp4`
- Scale down if need be (Instagram only accepts 480p-720p width as of this writing)
- `mkdir scaled`
- `> find . -name "segment*.mp4" -exec ffmpeg -i {} -vf scale=720:404 ./scaled/{} \;`
- Optional: Split out story videos (can only be 15 seconds, using 14sec because copy codec can be imprecise). For example:
- `cd scaled; mkdir story`
- `find . -name "segment*.mp4" -exec echo ffmpeg -ss 0:00 -i {} -t 14 -c copy story/{} \;`

## Get ready to post
- `> git clone https://github.com/staringispolite/mandoline.git`
- `cd mandoline`
- `mkdir segments`
- `cp segment*.mp4 ./segments`
- `cp segment_list.txt ./segments/segments.db`
- Add Instagram username & password to mandoline.py

## Post to Instagram
- `python mandoline.py --basepath="/abs/path/to/segments/"` (end with a /)

## Post automatically via cron
- Adding the following to your crontab, to post at 8am and 8pm UTC:
- `0 8,16 * * *   username    python /absolute/path/to/mandoline.py --basepath="/absolute/path/to/segments/"`

## Make friends
- `cd InstaPy; python your_project_name.py`
or via crontab, eg
- 0 12    * * *   root    cd /path/to/InstaPy; python your_project_name.py

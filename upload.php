<?php

set_time_limit(0);
date_default_timezone_set('UTC');

require __DIR__.'/vendor/autoload.php';

/////// CONFIG ///////
$username = $argv[1];
$password = $argv[2];
$debug = true;
$truncatedDebug = true;
//////////////////////

/////// MEDIA ////////
$videoFilename = $argv[3];
$captionText = $argv[4];
//////////////////////

$ig = new \InstagramAPI\Instagram($debug, $truncatedDebug);

try {
  $ig->login($username, $password);
} catch (\Exception $e) {
  echo 'Something went wrong: '.$e->getMessage()."\n";
  exit(0);
}

try {
  // Note that this performs a few automatic chunk upload retries by default,
  // in case of failing to upload the video chunks to Instagram's server!
  $metadata = ['caption' => $captionText];
  $ig->timeline->uploadVideo($videoFilename, $metadata);
  // Add stories if/when I have different content to post.
  //$ig->story->uploadVideo($videoFilename, $metadata);

  // or...

  // Example of using 8 retries instead of the default amount:
  // $ig->timeline->uploadVideo($videoFilename, ['caption' => $captionText], 8);
} catch (\Exception $e) {
  echo 'Something went wrong: '.$e->getMessage()."\n";
}

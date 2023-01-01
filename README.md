A [yt-dlp](https://github.com/yt-dlp/yt-dlp) postprocessor [plugin](https://github.com/yt-dlp/yt-dlp#plugins) for [Return YouTube Dislike](https://returnyoutubedislike.com)

Note: The API has [rate-limiting](https://returnyoutubedislike.com/docs/usage-rights)


## Installation

Requires yt-dlp `2023.01.01` or above. For older versions, use [this gist](https://gist.github.com/pukkandan/077465b736b861ab1aa6bf8c9bdb322a)

You can install this package with pip:
```
python3 -m pip install -U https://github.com/pukkandan/yt-dlp-ReturnYoutubeDislike/archive/master.zip
```

See [yt-dlp installing plugins](https://github.com/yt-dlp/yt-dlp#installing-plugins) for the many other ways this plugin package can be installed.

## Usage

Pass `--use-postprocessor ReturnYoutubeDislike:when=pre_process` to activate the PostProcessor

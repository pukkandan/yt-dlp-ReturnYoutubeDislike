"""
Fields defined in "RYD_FIELDS" are updated using the information from the API.
The original values of those fields and the response from the API are saved
under "RYD" key in the info dict
"""

from yt_dlp.postprocessor.common import PostProcessor


RYD_FIELDS = {
    'like_count': 'likes',
    'dislike_count': 'dislikes',
    'average_rating': 'rating',
    'view_count': 'viewCount',
}

SUPPORTED_EXTRACTORS = {
    'Youtube',
}


class ReturnYoutubeDislikePP(PostProcessor):
    def run(self, info):
        extractor = info['extractor_key']
        if extractor not in SUPPORTED_EXTRACTORS:
            self.to_screen(f'{self.PP_NAME} is not supported for {extractor}')
            return [], info

        api_data = self._download_json(
            f'https://returnyoutubedislikeapi.com/votes?videoId={info["id"]}') or {}

        info['RYD'] = {
            'response': api_data,
            'original': {k: info.get(k) for k in RYD_FIELDS.keys()}
        }
        if api_data:
            info.update({k: api_data.get(v) for k, v in RYD_FIELDS.items()})

        return [], info

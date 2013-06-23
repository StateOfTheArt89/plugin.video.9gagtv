#!/usr/bin/python
# -*- coding: utf-8 -*-
from gagtv import GagTV, Keys, GagException

class JsonListItemConverter(object):

    def __init__(self, PLUGIN, title_length):
        self.plugin = PLUGIN

    def convertVideoToListItem(self, video):
        name = video[Keys.TITLE].encode('utf-8')
        image = video[Keys.THUMBNAIL].encode('utf-8')
        vid = video[Keys.YOUTUBE_VIDEO_ID].encode('utf-8')
        return {
                'label': name,
                'path': self.plugin.url_for('playVideo', videoId = vid),
                'icon' : image,
                'is_playable': True,
                }


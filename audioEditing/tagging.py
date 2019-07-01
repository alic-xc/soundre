from .audioException import (
                ExtensionException,
                TaggingException
            )

from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3
from mutagen.id3 import ID3


class Tagging:

    def __init__(self, io):
        """  """
        self.fileObj = io
        if not self.fileObj.name.endswith('mp3'):
            raise ExtensionException('Not Expecting file extension')

    def view_tags(self):
        try:
            audio = MP3(self.fileObj)
            print(audio)
        except Exception as err:
            print(err)



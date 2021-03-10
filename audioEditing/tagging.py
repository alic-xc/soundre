from .audioException import (
                ExtensionException,
                TaggingException
            )
from mutagen.easyid3 import EasyID3
from mutagen import File
from mutagen.id3 import APIC, ID3
import mutagen



class Tagging:
    """
    This allows editing of audio tags. It depends on mutagen
    library which makes it easy to worked on
    """
    def __init__(self, io):
        try:
            self.fileObj = io
            if self.fileObj.url.rsplit('.')[-1] != 'mp3':
                raise ExtensionException('Not Expecting file extension')

            self.audio = EasyID3(self.fileObj.path)

        except mutagen.id3.ID3NoHeaderError as err:
            self.audio = File(self.fileObj.path, easy=True)
            self.audio.add_tags()
            self.audio.save(self.fileObj.path, v1=2)

        except (mutagen.MutagenError, ExtensionException) as err:
            self.audio = None

    def add_tag(self, tags, image):
        """
        Method for editing or adding new tags for a mp3 files.
        Also, it add cover image to it an image is provided.
        """
        if tags is not None:
            for key, value in tags.items():
                if value is not None or value != '':
                    if key != 'cover':
                        self.audio[u'{}'.format(key)] = value
            self.audio.save(self.fileObj.path, v1=2)

        if image is not None:
            img = image
            fileObj = image.read()
            img_ext = img.name.rsplit('.')[-1]
            multipart = [('jpg', 'image/jpeg'), ('png', 'image/png'), ('jpeg', 'image/jpeg')]
            img_typ = ''
            for typ in multipart:
                if img_ext in typ:
                    img_typ = typ[1]
                    break

            id3 = ID3(self.fileObj.path)
            id3.add(APIC(3, img_typ, 3, 'Front Cover', fileObj))
            id3.save(v2_version=3)

    def tags(self):
        tags = {}

        if self.audio is not None:

            for key, value in self.audio.items():
                tags[key] = value[0]

        return tags

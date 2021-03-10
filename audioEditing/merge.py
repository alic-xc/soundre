from django.core.files import File
from pydub import AudioSegment
from .audioException import SoundException
from .tagging import Tagging


class Merge:
    """ using composition """

    def __init__(self, file1, file2, position, mergeobj = AudioSegment ):
        self.file1 = file1
        self.file2 = file2
        self.position = position
        self.tags = ''
        self.Obj = mergeobj

    def merge_sound(self, secs):
        """ """
        try:
            main_audio = self.Obj.from_mp3(self.file1.path)
            stamp_audio = self.Obj.from_mp3(File(self.file2))

            if len(stamp_audio) > 10000:
                raise Exception('Audio length greater than 10 secs')

            result = main_audio.overlay(stamp_audio, position=self._milliseconds(main_audio, secs), gain_during_overlay=-6)
            result.export(self.file1.path, format="mp3", bitrate="192k", tags={**self.tags} )

        except FileNotFoundError as err:
            raise err

        except SoundException as err:
            raise err

        return True

    def get_file_tags(self):
        self.tags = Tagging(self.file1).tags()
        return self.tags

    def _milliseconds(self, audio, sub):
        length = audio.duration_seconds
        if length < 1:
            return 0

        if self.position == 'Beginning':
            return sub

        return length - sub

    def run_process(self, secs=5000):
        self.get_file_tags()
        self.merge_sound(secs)





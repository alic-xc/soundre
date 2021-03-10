from pydub import AudioSegment
from .tagging import Tagging


class Crop:
    """ Allow cutting out unwanted path from an audios """

    def __init__(self, file, minute, seconds, length):
        self.minute = (minute * 60) if minute > 0 else 0  # set the minute
        self.starting_point = (self.minute + seconds) * 1000  # Set starting point for cropping
        self.crop_length = self.starting_point + (length * 1000)  #
        self.fileObj = file
        self.tags = ''

    def remove(self):
        """
        This method will remove desired length from the audio.
        It replace the current audio with the newly modified one.
        """

        try:
            temp = AudioSegment.from_mp3(self.fileObj.path)
            duration = len(temp)

            if self.starting_point >= self.crop_length:
                raise Exception('Invalid Length. Check audio length')

            part1 = temp[:self.starting_point]
            part2 = temp[-(duration - self.crop_length):]
            result = part1 + part2
            result.export(self.fileObj.path, format="mp3",
                          bitrate="192k",
                          tags={**self.tags})
            return True
        except Exception as err:
            print(err)
            return False

    def get_file_tags(self):
        """ Get current file tags """
        self.tags = Tagging(self.fileObj).tags()
        return self.tags

    def run_process(self):
        """ Object manager """
        try:
            self.get_file_tags()
            self.remove()
            return True

        except Exception as err:
            print(err)
            return False
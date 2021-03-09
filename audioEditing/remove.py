from pydub import AudioSegment
from .tagging import Tagging


class Crop:
    """ Allow cutting out unwanted path from an audios """

    def __init__(self, file, minute, seconds, length):
        self.minute = (minute * 60) if minute > 0 else 0
        self.duration = (self.minute + seconds) * 1000
        self.length = (length * 1000) + self.duration
        self.fileObj = file
        self.tags = ''

    def remove(self):
        """
        This method will remove desired length from the audio.
        It replace the current audio with the newly modified one.
        """

        try:
            print("YET 1")
            temp = AudioSegment.from_mp3(self.fileObj.path)
            print("YET 3")
            duration = len(temp)

            if self.length >= self.duration:
                raise Exception('Invalid Length. Check audio length')

            part1 = temp[:self.duration]
            part2 = temp[-(duration - self.length):]
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
        self.get_file_tags()
        self.remove()
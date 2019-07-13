from pydub import AudioSegment
from .tagging import Tagging
class Crop:

    def __init__(self, file, minute, seconds, length):
        self.minute = (minute * 60) if minute > 0 else 0
        self.duration = (self.minute + seconds) * 1000
        self.length = (length * 1000) + self.duration
        self.fileObj = file

    def remove(self):
        try:
            temp = AudioSegment.from_mp3(self.fileObj.path)
            duration = len(temp)
            if self.length >= self.duration:
                raise Exception('Invalid Length. Check audio length')

            part1 = temp[:self.duration]
            part2 = temp[-(duration - self.length):]
            result = part1 + part2
            result.export(self.fileObj.path, format="mp3",
                          bitrate="192k",
                          tags={**self.tags},
                          )
            return True

        except Exception as err:
            return False

    def get_file_tags(self):
        self.tags = Tagging(self.fileObj).tags()
        return self.tags

    def run_process(self):
        self.get_file_tags()
        self.remove()
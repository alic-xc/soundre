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
            part1 = temp[:self.duration]
            part2 = temp[-(duration - self.length):]
            result = part1 + part2
            result.export(self.fileObj.path, format="mp3",
                          bitrate="192k",
                          tags={**self.tags},
                          )
        except Exception as err:
            return err

    def get_file_tags(self):
        self.tags = Tagging(self.fileObj).tags()
        for key, value in self.tags:
            self.tags[key] = value[0]
        return self.tags

    def run_process(self):
        self.get_file_tags()
        self.remove()
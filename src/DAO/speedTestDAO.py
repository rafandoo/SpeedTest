from DTO.speedTestDTO import SpeedTestDTO 
import os

class SpeedTestDAO:
    def __init__(self, filename):
        self.filename = filename

    def save(self, speedTestDTO):
        if not os.path.exists(self.filename):
            with open(self.filename, 'w') as file:
                file.write('download;upload;ping;latency;sponsor;date')
        with open(self.filename, 'a') as file:
                file.write('\n' + speedTestDTO.toCSV())

    def delete(self):
        os.remove(self.filename)

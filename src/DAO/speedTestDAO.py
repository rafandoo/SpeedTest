import os
import logging


class SpeedTestDAO:
    def __init__(self, filename):
        self.filename = filename

    def save(self, speedTestDTO):
        try:
            if not os.path.exists(self.filename):
                with open(self.filename, 'w') as file:
                    file.write('download;upload;ping;latency;sponsor;date')
            with open(self.filename, 'a') as file:
                file.write('\n' + speedTestDTO.toCSV())
        except Exception as e:
            logging.error(e)

    def delete(self):
        os.remove(self.filename)

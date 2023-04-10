from DAO.speedTestDAO import SpeedTestDAO


class SpeedTestBO:
    def __init__(self):
        self.speedTestDAO = None

    def save(self, speedTestDTO):
        self.speedTestDAO = SpeedTestDAO('speedTest.csv')
        self.speedTestDAO.save(speedTestDTO)

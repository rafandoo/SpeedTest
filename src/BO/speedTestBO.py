from DAO.speedTestDAO import SpeedTestDAO

class SpeedTestBO:
    def __init__(self):
        pass

    def save(self, speedTestDTO):
        self.speedTestDAO = SpeedTestDAO('speedTest.csv')
        self.speedTestDAO.save(speedTestDTO)

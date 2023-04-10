import os, sys
import logging
import argparse
import time
from configparser import ConfigParser
from service.tester import Tester
from BO.speedTestBO import SpeedTestBO
from DTO.speedTestDTO import SpeedTestDTO

class Main:
    SPEED_TEST_VERSION = 'SPEED TEST 1.0.0'
    INI_FILE = 'config.ini'
    
    def __init__(self):
        self.st = SpeedTestBO()
        self.logger = logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', filename='speedTest.log')
        self.config = ConfigParser()
        self.loadIni()
        self.start()

    def resourcePath(self, relativePath):
        basePath = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
        return os.path.join(basePath, relativePath)

    def loadIni(self):
        try:
            self.config.read(self.resourcePath(self.INI_FILE))
            logging.info('INI file loaded')
        except Exception as e:
            logging.logger.error('Error loading INI file')
            logging.logger.error(e)
            exit(1)

    def test(self):
        self.s = Tester(self.args.timeout, self.args.threads, self.args.secure, self.args.pre_allocate)
        self.result = self.s.test()
        self.speedTestDTO = SpeedTestDTO(self.s.toMbps(self.result['download']), self.s.toMbps(self.result['upload']), self.result['ping'], self.result['server']['latency'], self.result['server']['sponsor'], self.result['timestamp'])
        self.st.save(self.speedTestDTO)
        logging.info(self.speedTestDTO)


    def start(self):
        self.parser = argparse.ArgumentParser(
            prog='Speed Test',
            description='Speed Test',
            epilog='Developed by: Rafael Camargo',
            usage='%(prog)s [options]'
        )
        
        self.parser.version = self.SPEED_TEST_VERSION
        self.parser.add_argument('-v', '--version', action='version', help='Show version')
        
        self.parser.add_argument('-t', '--timeout', type=int, help='Timeout in seconds to run the test', default=10)
        self.parser.add_argument('-l', '--loops', type=int, help='Number of loops to run the test', default=1)
        self.parser.add_argument('-d', '--delay', type=int, help='Delay in seconds between each loop', default=60)
        self.parser.add_argument('-th', '--threads', type=int, help='Number of threads to run the test', default=0)
        self.parser.add_argument('-s', '--secure', type=bool, help='Use HTTPS instead of HTTP when communicating with speedtest.net operated servers', default=False)
        self.parser.add_argument('-p', '--pre-allocate', type=bool, help='Pre-allocate upload data. Pre-allocating upload data prior to testing can increase upload performance. However, some systems may see a performance decrease when pre-allocating upload data.', default=False)
    
        self.args = self.parser.parse_args()
        
        # for printing the arguments
        if self.args.loops >= 1:
            for i in range(self.args.loops):
                self.test()
                time.sleep(self.args.delay)
            exit(0)
        else:
            while True:
                self.test()
                time.sleep(self.args.delay)
        
if __name__ == '__main__':
    Main()
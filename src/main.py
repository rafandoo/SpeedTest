import logging
import argparse
import time
from service.tester import Tester, toMbps
from BO.speedTestBO import SpeedTestBO
from DTO.speedTestDTO import SpeedTestDTO


class Main:
    SPEED_TEST_VERSION = 'SPEED TEST 1.0.0'

    def __init__(self):
        self.args = None
        self.parser = None
        self.st = SpeedTestBO()
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s',
                            filename='speedTest.log')
        self.start()

    def test(self):
        try:
            s = Tester(self.args.timeout, self.args.threads, self.args.secure, self.args.pre_allocate)
            result = s.test()
            speedTestDTO = SpeedTestDTO(toMbps(result['download']), toMbps(result['upload']), result['ping'],
                                        result['server']['latency'], result['server']['sponsor'], result['timestamp'])
            self.st.save(speedTestDTO)
            logging.info(speedTestDTO)
        except Exception as e:
            logging.error(e)

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
        self.parser.add_argument('-s', '--secure', type=bool,
                                 help='Use HTTPS instead of HTTP when communicating with speedtest.net operated servers',
                                 default=False)
        self.parser.add_argument('-p', '--pre-allocate', type=bool,
                                 help='Pre-allocate upload data. Pre-allocating upload data prior to testing can increase upload performance. However, some systems may see a performance decrease when pre-allocating upload data.',
                                 default=False)

        self.args = self.parser.parse_args()

        logging.info('Starting Speed Test, version: ' + self.SPEED_TEST_VERSION)
        logging.info('Arguments: ' + str(self.args))

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

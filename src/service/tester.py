from lib import speedtest_cli as speedtest


def toMbps(bps):
    return round(bps / 1000000, 2)


class Tester:
    def __init__(self, timeout, threads, secure, pre_allocate):
        self.timeout = timeout
        self.threads = threads
        self.secure = secure
        self.pre_allocate = pre_allocate

    def test(self):
        s = speedtest.Speedtest(secure=self.secure, timeout=self.timeout)
        s.get_best_server([])
        s.download(threads=self.threads)
        s.upload(threads=self.threads)
        return s.results.dict()

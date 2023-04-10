class SpeedTestDTO:
    def __init__(self, download, upload, ping, latency, sponsor, date):
        self.download = download
        self.upload = upload
        self.ping = ping
        self.latency = latency
        self.sponsor = sponsor
        self.date = date
        
    def __str__(self):
        return f"Download: {self.download} Mbps | Upload: {self.upload} Mbps | Ping: {self.ping} ms | Latency: {self.latency} ms | Sponsor: {self.sponsor} | Date: {self.date}"
    
    def __repr__(self):
        return f"SpeedTest(download={self.download}, upload={self.upload}, ping={self.ping}, latency={self.latency}, sponsor={self.sponsor}, date={self.date})"

    def toCSV(self):
        return f"{self.download};{self.upload};{self.ping};{self.latency};{self.sponsor};{self.date}"

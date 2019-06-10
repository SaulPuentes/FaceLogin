import time


class Timer:

    start = None
    end = None

    def start(self):
        self.start = time.time()
    
    def seconds(self):
        self.end = time.time()
        return self.end - self.start
    
    def restart(self):
        self.start = self.end
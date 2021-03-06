import time, threading

class Worker(object):
    """Handles a single repetitive entity-action."""
    def __init__(self, actionDelay, World, time=time, threading=threading):
        self.World = World
        self.actionDelay = actionDelay
        self.time = time
        self.threading = threading

    def work(self):
        for Entity in self.World.Entities:
            print("I sure love working with entities.")

    def run(self):
        while not self.endRun:
            self.work()
            self.time.sleep(self.actionDelay)

    def start(self):
        Thread = self.threading.Thread(target=self.run)
        self.endRun = False
        Thread.start()

    def quit(self):
        self.endRun = True





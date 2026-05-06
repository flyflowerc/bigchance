
class LoggerAgent:
    def __init__(self, bus):
        bus.subscribe("task", self.log)

    async def log(self, message):
        print("[LOG]", message)

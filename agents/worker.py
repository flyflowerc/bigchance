
import asyncio

class WorkerAgent:
    def __init__(self, bus, name="worker"):
        self.name = name
        self.bus = bus
        self.bus.subscribe("task", self.handle_task)

    async def handle_task(self, task):
        print(f"[{self.name}] Executing {task['task']}")
        await asyncio.sleep(1)

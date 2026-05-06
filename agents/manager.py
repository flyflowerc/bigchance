
import json
import asyncio

class ManagerAgent:
    def __init__(self, bus, planner):
        self.bus = bus
        self.planner = planner

    async def start(self):
        with open("config.json") as f:
            config = json.load(f)

        goal = config["workflow"]["goal"]
        plan = await self.planner.plan(goal)

        for step in plan:
            await self.bus.publish("task", step)
            await asyncio.sleep(1)

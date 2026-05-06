
import asyncio
from core.bus import MessageBus
from agents.manager import ManagerAgent
from agents.worker import WorkerAgent
from agents.logger import LoggerAgent
from agents.planner import PlannerAgent

async def main():
    bus = MessageBus()

    logger = LoggerAgent(bus)
    planner = PlannerAgent(bus)
    manager = ManagerAgent(bus, planner)

    workers = [WorkerAgent(bus, name=f"worker_{i}") for i in range(2)]

    await manager.start()

if __name__ == "__main__":
    asyncio.run(main())


class PlannerAgent:
    def __init__(self, bus):
        self.bus = bus

    async def plan(self, goal):
        return [
            {"task": "fetch_data"},
            {"task": "analyze_data"},
            {"task": "generate_report"}
        ]

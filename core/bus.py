
import asyncio
from collections import defaultdict

class MessageBus:
    def __init__(self):
        self.subscribers = defaultdict(list)

    def subscribe(self, topic, handler):
        self.subscribers[topic].append(handler)

    async def publish(self, topic, message):
        if topic in self.subscribers:
            await asyncio.gather(*[
                handler(message) for handler in self.subscribers[topic]
            ])

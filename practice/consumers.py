import asyncio
import time
from celery.result import AsyncResult
from celery_progress.backend import ProgressRecorder
from channels.generic.websocket import AsyncJsonWebsocketConsumer

class PracticeConsumer(AsyncJsonWebsocketConsumer):
    id = None
    polling_started = False
    progress = 0

    async def connect(self):
        await self.accept()

    async def receive(self, text_data=None, bytes_data=None, **kwargs):
        if text_data:
            self.id = text_data
            if not self.polling_started:
                self.polling_started = True
                # Start continuous polling when the WebSocket connection is established
                asyncio.create_task(self.poll_data_continuously())

            await self.send('PONG')

    async def poll_data_continuously(self):
        while True:
            if self.id:
                try:
                    # Poll your data source here (e.g., query database, make API request)
                    # Replace this with your actual data polling logic
                    data = "Some new data from the server at " + str(time.time())
                    result = AsyncResult(self.id)
                    if result.state == 'SUCCESS':
                        self.progress = 100
                        await self.send(text_data=str(self.progress))
                    else:
                        self.progress += 5
                        await self.send(text_data=str(self.progress))
                        
                    if self.progress >= 100:  # Check if progress is 100 or more
                        break  # Exit the loop when progress is 100 or more
                except Exception as e:
                    print(f"Error occurred while polling data: {e}")

            # Sleep for a certain interval before polling again
            await asyncio.sleep(1)  # Change the interval as needed

import random
from locust import TaskSet, task
import hlsplayer

SECONDS = 1000  # ms in seconds

class HLSUser(hlsplayer.HLSLocust):
    min_wait = 2 * SECONDS  # 2 seconds
    max_wait = 15 * SECONDS  # 5 seconds

    @task
    def play_lgi_vxpl(self):
        url = "https://stream.touquan.co/live/show/index.m3u8"
        duration = random.randint(60, 600)
        self.client.play(url, duration=duration)

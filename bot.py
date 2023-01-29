import time

from aiohttp import web
from pyrogram import Client
from plugins import web_server
from info import API_ID, API_HASH, BOT_TOKEN

class Bot(Client):


    def __init__(self):
        self.start_time = None
        super().__init__(
            name="ChannelAutoCopy",
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            workers=150,
            plugins={"root": "plugins"},
            sleep_threshold=5,
        )


    async def start(self):
        await super().start()
        me = await self.get_me()
        self.start_time = time.time()
        app = web.AppRunner(await web_server())
        await app.setup()
        bind_address = "0.0.0.0"
        await web.TCPSite(app, bind_address, PORT).start()
        print(f"{me.first_name} Started")
   
    async def stop(self, *args):
        await super().stop()
        print("Bot stopped. Bye.")

app = Bot()
app.run()

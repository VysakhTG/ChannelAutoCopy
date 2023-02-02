from info import FROM, TO
from pyrogram import Client, filters
from pyrogram.errors import FloodWait

@Client.on_message(filters.chat(FROM) & (filters.document | filters.video)) #add more filters if you want.
async def copy(c, m):
    try:
        if m.media and not (m.video_note or m.sticker):
            await m.copy(TO, caption = m.caption if m.caption else None)
        else:
            await m.copy(TO)
    except FloodWait as e:
        await asyncio.sleep(e.x)

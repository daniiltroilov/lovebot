# 7667439532:AAFRPIc5dE2qLEn4jaw2XcOFLDDeqd4ErMQ
import asyncio
import random
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from datetime import datetime
import logging
import pytz
import os
API_TOKEN = os.getenv('API_TOKEN')
ALLOWED_USER_ID = (611327348, 5792327667)  # ← замени на свой user_id
MSK = pytz.timezone('Europe/Moscow')

MORNING_MESSAGES = [
    # ... 30 утренних сообщений (не повторяю здесь ради краткости)
    "Доброе утро, солнышко ☀️",
    "Просыпайся, мир ждёт тебя 🌍",
    "Ты лучшее, что могло случиться с этим утром 💛",
    "С добрым утром, красотуля 😘",
    "Пусть сегодня всё получится 🎯",
    "Ты сияешь даже в пасмурный день 🌦️",
    "Начинай день с улыбки 😄",
    "Ты сильная, умная и очень нужный человек 💪",
    "Вдохни глубже — это запах новых возможностей 🌸",
    "Ты справишься со всем, что приготовил день 🛡️",
    "Пусть этот день будет лёгким ☕",
    "Ты делаешь этот мир добрее 💖",
    "День начинается с тебя — и это круто ✨",
    "Пусть твоё утро будет таким же тёплым, как ты 🌞",
    "Желаю тебе спокойствия и радости сегодня 🕊️",
    "Ты невероятная, и это не обсуждается 💥",
    "Смотри в зеркало — там котик 💫",
    "Улыбнись — ты живёшь! 💃",
    "Ты прекрасна просто потому, что ты есть 🌺",
    "Пусть всё сегодня сложится идеально 🧩",
    "Ты заслуживаешь всего самого лучшего 🎁",
    "Этот день будет твоим! 🔥",
    "Ты не одна — я всегда здесь 🐾",
    "Ты приносишь свет 💡",
    "Пусть кофе будет вкусным, а задачи — лёгкими ☕📋",
    "Ты любима мною зайка 💌",
    "Пусть день будет добрым, как ты ❤️",
    "Ты умеешь радовать других — сегодня побалуй себя 🍰",
    "Ты уже моводец, просто потому что проснувся 🌅",
    "Сегодня отличный день, чтобы быть счастливой 😊",
]

NIGHT_MESSAGES = [
    # ... 30 ночных сообщений
    "Спокойной ночи, ангелочек мой 😴",
    "Пусть тебе приснится что-то крутое 💤",
    "нАдеюсь ты в прекрасном сне 🌙",
    "Мир ждёт тибя завтра — отдохни 🛌",
    "Спи спокойно, я присмотрю 🐾",
    "Пусть ночь обнимет тебя нежно 💖",
    "Ты сегодня молодец. Всё! Точка. 🔚",
    "Пусть тебе снятся звёздочки ✨",
    "Ты в безопасности, спи крепко 🕊️",
    "Пусть каждый сон будет добрым 📚",
    "Ты принесла свет в этот день — теперь отдыхай 🔋",
    "Устала быть лучшей для меня? 💡",
    "Ты сделала всё, что могла — теперь спи 💤",
    "Я горжусь тобой 💛",
    "Ты невероятно ценна, даже когда спишь 🌌",
    "Засыпай с лёгким сердцем 💗",
    "Ты достоинна самого мягкого сна 🛏️",
    "Пусть луна споёт тебе колыбельную 🌕🎶",
    "Ночь — это подарок для восстановления 🎁",
    "Ты принёс добро — оно вернётся 💫",
    "Ты умница. Отдыхай 🌜",
    "Пусть тревоги исчезнут во сне 🌬️",
    "Спокойной ночи, пукалка дня 🌟",
    "Ты нужен этому миру — завтра продолжим 💪",
    "Всё будет хорошо. Спи 🕊️",
    "Ты не один — я рядом 🐻",
    "Спокойного сна и сладких грёз 🍬",
    "Ты — свет даже в темноте 💫",
    "Отпусти мысли, просто отдыхай 🌊",
    "Скоро утро, а пока — отдыхай ☁️",
]

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher()
scheduler = AsyncIOScheduler()

async def send_morning_message():
    try:
        msg = random.choice(MORNING_MESSAGES)
        for user_id in ALLOWED_USER_ID:
            await bot.send_message(user_id, f"☀️ {msg}")
    except Exception as e:
        logging.error(f"Ошибка утреннего сообщения: {e}")

async def send_night_message():
    
    try:
        msg = random.choice(NIGHT_MESSAGES)
        for user_id in ALLOWED_USER_ID:
            await bot.send_message(user_id, f"🌙 {msg}")
    except Exception as e:
        logging.error(f"Ошибка ночного сообщения: {e}")

# Реакция на любые входящие сообщения
@dp.message(F.text)
async def handle_message(message: Message):
    if message.from_user.id in ALLOWED_USER_ID:
        await message.answer("Ты никогда не забудешь такого придурка как я 😊")
    else:
        await message.answer("Ты не мой любимый человек 🤬🤬🤬")

async def main():
    logging.info("Бот запускается...")
    scheduler.add_job(send_morning_message, 'cron', hour=11, minute=0, timezone=MSK)
    scheduler.add_job(send_night_message, 'cron', hour=3, minute=0, timezone=MSK)
    scheduler.add_job(send_night_message, 'cron', hour=8, minute=0, timezone=MSK)
    scheduler.start()
    logging.info("Бот работает...")
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())


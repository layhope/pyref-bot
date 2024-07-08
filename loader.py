from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from config import BOT_TOKEN

bot = Bot(BOT_TOKEN, parse_mode='html')
dp = Dispatcher(bot, storage=MemoryStorage())
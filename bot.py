import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command
from deep_translator import GoogleTranslator

TOKEN = "5925272864:AAHXfzxkCdYHrXUwhcV8Iz6qW6eeWAKz-jQ"

bot = Bot(token=TOKEN)
dp = Dispatcher()

# Tarjima qilinadigan tillar
TARGET_LANGUAGES = {
    "🇺🇿 O‘zbek": "uz",
    "🇷🇺 Rus": "ru",
    "🇬🇧 Ingliz": "en",
    "🇫🇷 Fransuz": "fr",
    "🇩🇪 Nemis": "de",
    "🇹🇷 Turkcha": "tr",
}

@dp.message(Command("start"))
async def start_handler(message: Message):
    await message.answer("👋 Salom! Men tarjimon botman.\n\n📌 Mening yaratuvchim Ahmedov Shuhrat bo'ladilar, @Akhmedov_Shuxrat")
    await message.answer("Menga xoxlagan matningizni yuboring men uni 5 ta tilgan tarjima qilib beraman!")

@dp.message()
async def translate_message(message: Message):
    try:
        original_text = message.text
        translations = []

        for lang_name, lang_code in TARGET_LANGUAGES.items():
            translated_text = GoogleTranslator(source="auto", target=lang_code).translate(original_text)
            translations.append(f"{lang_name}: {translated_text}")

        response = "**Tarjimalar:**\n\n" + "\n".join(translations)
        await message.answer(response)
    
    except Exception as e:
        await message.answer(f"❌ Xatolik yuz berdi: {e}")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

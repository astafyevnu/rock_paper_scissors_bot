from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from keyboards import game_kb, yes_no_kb
from lexicon import LEXICON_RU
from game import get_winner, get_bot_choice

# Инициализируем роутер уровня модуля
router = Router()

# Варианты ходов
CHOICES = [stone := "\U0001FAA8", scissors := "\U00002702", paper := "\U0001F4DC"]


# Этот хэндлер будет срабатывать на команду "/start"
@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(
        text=LEXICON_RU['/start'],
        parse_mode='HTML',
        reply_markup=yes_no_kb
    )


# Этот хэндлер срабатывает на команду /help
@router.message(Command(commands="help"))
async def process_help_command(message: Message):
    await message.answer(
        text=LEXICON_RU["/help"],
        parse_mode='HTML',
        reply_markup=yes_no_kb)


# Этот хэндлер срабатывает на согласие пользователя играть в игру
@router.message(F.text == LEXICON_RU["yes_button"])
async def process_yes_answer(message: Message):
    await message.answer(text=LEXICON_RU["yes"], reply_markup=game_kb)


# Этот хэндлер срабатывает на отказ пользователя играть в игру
@router.message(F.text == LEXICON_RU["no_button"])
async def process_no_answer(message: Message):
    await message.answer(text=LEXICON_RU["no"])


# Этот хэндлер срабатывает на любую из игровых кнопок
@router.message(
    F.text.in_([LEXICON_RU["stone"], LEXICON_RU["paper"], LEXICON_RU["scissors"]])
)
async def process_game_button(message: Message):
    bot_choice = get_bot_choice()
    # Отправка результата
    await message.answer(
        f"Ты выбрал: {message.text}\n"
        f"Бот выбрал: {bot_choice}\n"
    )

    result = get_winner(message.text, bot_choice)

    if result == "victory":
        message_effect_id = "5046509860389126442"
    else:
        message_effect_id = None

    await message.answer(
        text=LEXICON_RU[result],
        message_effect_id=message_effect_id,
        reply_markup=yes_no_kb,
    )


# Хэндлер для сообщений, которые не попали в другие хэндлеры
@router.message()
async def send_answer(message: Message):
    await message.answer(text=LEXICON_RU["other_answer"])

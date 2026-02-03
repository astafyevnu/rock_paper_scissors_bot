from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from lexicon import LEXICON_RU

# Инициализируем билдер
yes_no_kb_builder = ReplyKeyboardBuilder()
game_kb_builder = ReplyKeyboardBuilder()

# Создаём кнопки с ответами согласия и отказа
button_yes = KeyboardButton(text=LEXICON_RU["yes_button"])
button_no = KeyboardButton(text=LEXICON_RU["no_button"])

# Добавляем кнопки в билдер с аргументом width=2
yes_no_kb_builder.row(button_yes, button_no, width=2)

# Создаём клавиатуру с кнопками "✅ Давай!" и "Не хочу!"
yes_no_kb: ReplyKeyboardMarkup = yes_no_kb_builder.as_markup(
    one_time_keyboard=True, resize_keyboard=True
)

# Создаём игровую клавиатуру
buttons = [
    KeyboardButton(text=LEXICON_RU['stone']),
    KeyboardButton(text=LEXICON_RU['scissors']),
    KeyboardButton(text=LEXICON_RU['paper']),
    # KeyboardButton(text=LEXICON_RU['rules'])
]

# Добавляем кнопки в билдер
game_kb_builder.row(*buttons, width=3)
# Создаем объект клавиатуры
game_kb: ReplyKeyboardMarkup = game_kb_builder.as_markup(
    resize_keyboard=True,
    input_field_placeholder=LEXICON_RU['choose_move']
)

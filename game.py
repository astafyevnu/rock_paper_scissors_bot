from lexicon import LEXICON_RU
import random

# Варианты ходов
CHOICES = [
    stone := LEXICON_RU['stone'],
    scissors := LEXICON_RU['scissors'],
    paper := LEXICON_RU['paper']
]


# Функция, возвращающая случайный выбор бота в игре
def get_bot_choice() -> str:
    return random.choice(CHOICES)


# Функция, определяющая победителя
def get_winner(user_choice: str, bot_choice: str) -> str:
    # Определение результата
    if user_choice == bot_choice:
        result = "draw"
    elif (
            (user_choice == stone and bot_choice == scissors) or
            (user_choice == scissors and bot_choice == paper) or
            (user_choice == paper and bot_choice == stone)
    ):
        result = "victory"
    else:
        result = 'loss'

    return result

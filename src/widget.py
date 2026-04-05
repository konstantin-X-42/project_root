from src.masks import get_mask_card_number
from src.masks import get_mask_account


def mask_account_card(card_or_account: str) -> str:
    """ функция маскирует номер карты или счёта """
    if "Счет" in card_or_account:
        mask = get_mask_account(card_or_account[5:])
    else:
        mask = get_mask_card_number(card_or_account[-16:])
        print(card_or_account[-16:].strip(' '))
    return mask


# --------------------------------------------------------------------
# В том же модуле создайте функцию get_date, которая принимает на вход строку с датой в формате
# "2024-03-11T02:26:18.671407"
#  и возвращает строку с датой в формате "ДД.ММ.ГГГГ" ("11.03.2024")
def get_date():
    pass

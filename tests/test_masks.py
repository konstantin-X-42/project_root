from src.masks import get_mask_account, get_mask_card_number
from src.widget import get_date, mask_account_card

print(get_mask_card_number("7000792289606361"))
print(get_mask_card_number(7000792289606361))
print(get_mask_card_number("700079228960636"))
print(get_mask_card_number(700079228960636))
print(get_mask_card_number(70007922 + 9606361))
print(get_mask_card_number("70007922889606361"))
print(get_mask_card_number(70007922889606361))
print(get_mask_card_number("h000792289606361"))
print(get_mask_card_number("-700079228960636"))
print(get_mask_card_number(-700079228960636))
print(get_mask_card_number("70007922+9606361"))
print(get_mask_card_number(["7000792289606361"]))
print(get_mask_card_number([7000792289606361]))
print(get_mask_card_number({"7000792289606361"}))
print(get_mask_card_number({7000792289606361}))
print(get_mask_card_number())

# ----------------------------------------------

print(get_mask_account("73654108430135874305"))
print(get_mask_account(73654108430135874305))
print(get_mask_account("7365410843013587430"))
print(get_mask_account(7365410843013587430))
print(get_mask_account(73654108401 + 35874305))
print(get_mask_account("736541084301358874305"))
print(get_mask_account(736541084301358874305))
print(get_mask_account("736g54108430135874305"))
print(get_mask_account("s3654108430135874305"))
print(get_mask_account("-3654108430135874305"))
print(get_mask_account(-73654108430135874305))
print(get_mask_account("736541084/0135874305"))
print(get_mask_account(["73654108430135874305"]))
print(get_mask_account([73654108430135874305]))
print(get_mask_account({"73654108430135874305"}))
print(get_mask_account({73654108430135874305}))
print(get_mask_account())

# ----------------------------------------------

print(mask_account_card("Maestro 1596837868705199"))
print(mask_account_card("Счет 64686473678894779589"))
print(mask_account_card("MasterCard 7158300734726758"))
print(mask_account_card("Счет 35383033474447895560"))
print(mask_account_card("Visa Classic 6831982476737658"))
print(mask_account_card("Visa Platinum 8990922113665229"))
print(mask_account_card("Visa Gold 5999414228426353"))
print(mask_account_card("Счет 73654108430135874305"))

# ----------------------------------------------

print(get_date("2024-03-11T02:26:18.671407"))
print(get_date("2024-g3-11T02:26:18.671407"))
print(get_date("2024-33-11T02:26:18.671407"))
print(get_date("1024-03-11T02:26:18.671407"))
print(get_date("2024-03-32T02:26:18.671407"))
print(get_date(20240311022618671407))
print(get_date())

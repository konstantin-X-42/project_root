from crc.masks import get_mask_card_number

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
print(get_mask_card_number())


from crc.masks import get_mask_account

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
print(get_mask_account())

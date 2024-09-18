# Домашняя работа по уроку "Способы вызова функции"

def is_address_good(address: str):
    if address.find(" ") >= 0 or address.find("..") >= 0:
        return False
    split_address = address.split("@")
    if len(split_address) != 2 or split_address[0] == "":
        return False
    split_address = split_address[-1].split(".")
    if len(split_address) < 2 or split_address[0] == "":
        return False
    split_address_end = split_address[-1]
    if split_address_end == "com" or split_address_end == "ru" or split_address_end == "net":
        return True
    return False


def send_email(message, recipient, *, sender="university.help@gmail.com"):
    if not is_address_good(recipient) or not is_address_good(sender):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
    elif recipient == sender:
        print(f"Нельзя отправить письмо самому себе!")
    elif sender == "university.help@gmail.com":
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
    else:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")


# send_email('Это сообщение для проверки связи', 'vasyok1337@.com')
# send_email('Это сообщение для проверки связи', '@someplace.com')
# send_email('Это сообщение для проверки связи', 'vasyok1337@some place.com')
send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')

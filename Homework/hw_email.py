import math
from datetime import date

# словарь email
email = {
    "subject": "Conference",
    "from": "Veronika@sberbank.ru",
    "to": "Kate@sberbank.ru",
    "body": "Hello, Kate! Conference at 12:00 online!",
}

# переменная с текущей датой
send_data = date.today().strftime("%Y-%m-%d")

# добавление даты в словарь
email["date"] = send_data
print(email)

# привести к нижнему регистру и уберать пробелы по краям e-mail адрес отправителя и получателя
email["from"] = email["from"].strip().lower()
email["to"] = email["to"].strip().lower()
print(email)

# извлечь логин и домен отправителя в две переменные login и domain
login = email["from"].split("@")[0]
domain = email["from"].split("@")[1]

# сокращённая версия текста с помощью срезов
email["short_body"] = email["body"][:10] + "..."
print(email["short_body"])

# список личных доменов
personal_domains = [
    'gmail.com', 'list.ru', 'yahoo.com', 'outlook.com', 'hotmail.com',
    'icloud.com', 'yandex.ru', 'mail.ru', 'list.ru', 'bk.ru', 'inbox.ru',
]

# список корпоративных доменов
corporate_domains = [
    'company.ru', 'corporation.com', 'university.edu',
    'organization.org', 'company.ru', 'business.net'
]

# проверка, что между доменами нет пересечений
# альтернативная запись
# intersection = set(personal_domains).intersection(corporate_domains)
intersection = set(personal_domains) & set(corporate_domains)
print(intersection)

# проверьте «корпоративность» отправителя, создав булево
sender_domain = email["from"].split("@")[1]
is_corporate = sender_domain in corporate_domains
print(f"is corporate sender: {is_corporate}")

# cобрать «чистый» текст сообщения
email["clean_body"] = email["body"]. replace("\n", " ").replace("\t", " ")
print(email["clean_body"])

# многострочный текст
email["sent_text"] = f"""Кому: {email["to"]}, от {email["from"]}
Тема: {email["subject"]}, дата {email["date"]}
{email["clean_body"]}"""
print(email["sent_text"])

# рассчитать количество страниц печати для email
pages = math.ceil(len(email["sent_text"]) / 500)
print("Количество страниц:", pages)

# проверка пустоты темы и тела письма c помощью булева
is_subject_empty = not email["subject"]
is_body_empty = not email["body"]

print("Пустая тема письма", is_subject_empty)
print("Пустое тело письма", is_body_empty)

# cоздать «маску» e-mail отправителя
sender = email["from"]
logins, domains = sender.split("@")
email["masked_form"] = login[:2] + "***@" + domain

print("Маска отправителя", email["masked_form"])

# удалить из списка личных доменов значения "list.ru" и "bk.ru".
if "list.ru" in personal_domains:
    personal_domains.remove("list.ru")

if "bk.ru" in personal_domains:
    personal_domains.remove("bk.ru")

print(email)
print(is_corporate, is_subject_empty, is_body_empty, pages)


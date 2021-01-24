# IMAP query builder example
from imap_tools import Q, AND, OR, NOT
import datetime

# AND
Q(text='hello', new=True)  # '(TEXT "hello" NEW)'
# OR
OR(text='hello', date=datetime.date(2000, 3, 15))
# NOT
NOT(text='hello', new=True)  # 'NOT (TEXT "hello" NEW)'
# complex
Q(OR(from_='from@ya.ru', text='"the text"'), NOT(OR(Q(answered=False), Q(new=True))), to='to@ya.ru')


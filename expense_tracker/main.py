# print('=== КИРЕШЕ-ЧЫГАША ЭСЕПТЕГИЧ ===')
#
# income = 0
# expense = 0
#
# while True
#     print('\n1. Киреше кошуу')
#     print('2. Чыгаша кошуу')
#     print('3. Балансты коруу')
#     print('4. Чыгуу')
#
#     choice = input('Тандоону жаз (1 - 4): ')
#
#     if choice == '1':
#         amount = float(input('канча киреше кошосун?'))
#         income += amount
#         print('Киреше кошулду')
#
#     elif choice == '2':
#         amount = float(input('Канча чыгаша болду?'))
#         expense += amount
#         print("Чыгаша кошулду")
#
#     elif choice == '3':
#         balance = income - expense
#         print('Жалпы киреше:', income)
#         print('Жалпы чыгаша:', expense)
#         print('Калган акча:', balance)
#
#     elif choice == '4':
#         break
#
#     else:
#         print('Туура эмес тандоо. Кайра аракет.')
#
#
# import json
# import os
# from datetime import datetime
# from random import choices
#
# FILE_NAME = "data.json"
#
#
# def load_date():
#     if os.path.exists(FILE_NAME):
#         with open(FILE_NAME, 'r', encoding='utf-8') as file:
#             data = json.load(file)
#         if 'history' not in data:
#             data['history'] = []
#         return data
#
#     return {'income': 0, 'expense': 0, 'history': []}
#
#
# def save_date(data):
#     with open(FILE_NAME, 'W', encoding='utf-8') as file:
#         json.dump(data, file, ensure_asciii=False, indent=4)
#
#
# def add_transaction(data, transaction_type):
#     try:
#         amount = float(input('Сумманы жаз: '))
#         if amount <= 0:
#             print('Сумма нолдон чон болушу керек?')
#             return
#
#     except ValueError:
#         print('Сандарды гана жаз!')
#         return
#
#     data['history'].append({
#         'type': transaction_type,
#         'amount': amount,
#         'date': datetime.now().strftime('%Y-%m-%d %H:%M')
#     })
#
#     save_date(data)
#     print('Маалымат сакталды!')
#
# def show_balance(data):
#     print('Жалпы киреше:', data['income'])
#     print('Жалпы чыгыша:', data['expense'])
#     print('Баланс:', data['income'] - data['expense'] )
#
#
# def show_history(data):
#     print('\n===  ОПЕРАЦИЯЛАР ТААРЫХЫ ===')
#
#     if not data['history']:
#         print('Азырынча операция жок.')
#         return
#
#     for item in data['history']:
#         name = 'Киреше' if item[ 'type'] == 'income ' else 'Чыгаша'
#         print(
#             item['date'],
#             '|', name,
#             '|', item['amount'], 'сом'
#         )
#
# data = load_date()
#
# while True:
#     print('\n=== КИРЕШЕ ЧЫГАША ===')
#     print('1. Киреше кошуу')
#     print('2. Чыгаша кошуу')
#     print('3. Балансты коруу')
#     print('4. Чыгуу')
#     print('5. Операциялар таарыхы')
#
#     choice = input('Тандоон(1-5): ')
#
#     if choice == '1':
#         add_transaction(data, 'income')
#
#     elif choice == '2':
#         add_transaction(data, 'expense')
#
#     elif choice == '3':
#         show_balance(data)
#
#     elif choice == '4':
#         show_history(data)
#
#     else:
#         print('1ден 5ке чейин сан танда. ')








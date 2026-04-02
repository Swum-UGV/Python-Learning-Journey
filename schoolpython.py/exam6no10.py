transaction_data='Purchase:Online Python Course:199.90'
exchange_rate_usd_to_eur = 0.92
parts=transaction_data.split(':')
transaction_type=parts[0]
description=parts[1]
amount_of_usd=parts[2]
amount_usd=float(amount_of_usd)
amount_eur=amount_usd*exchange_rate_usd_to_eur 
print('Transaction details:')
print(description)
print(f'amount of usd:{amount_usd:.2f}')
print(amount_eur)

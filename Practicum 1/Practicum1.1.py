balance = 0
transactions = 0
interest = 0
debt = 0

add_balance1 = int(input())
while add_balance1 != 0:
    balance = balance + add_balance1
    add_balance1 = int(input())
    transactions += 1
    if balance >= 0 and transactions % 3 == 0:
        interest = interest + balance * 0.1
        balance *= 1.1
    if balance < 0 and transactions % 3 == 0:
        debt = debt + balance * 0.2
        balance *= 1.2
print(round(balance, 2), round((debt + interest), 2), round(interest, 2), round(debt, 2))
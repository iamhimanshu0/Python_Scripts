x = input().split(' ')
amount_withdraw = int(x[0])
balance = float(x[1])

if (amount_withdraw % 5 == 0 and balance >= amount_withdraw + 0.5):
    balance = balance - amount_withdraw - 0.5
    print('{0:.2f}'.format(balance))
else:
    print('{0:.2f}'.format(balance))

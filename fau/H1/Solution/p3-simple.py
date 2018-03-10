# Homework 1
# Problem 3 solution
#
#  Do not distribute.
#

while True:
    amount = float(input('Enter amount:'))

    if amount < 0:
        print("Invalid input.")
    else:
        # convert to pennies:
        amount_cents = int(amount * 100)

        coins_total_amount = 0
        coins_total_count = 0
        cents_left = amount_cents

        quarters = cents_left // 25
        cents_left -= quarters * 25
        coins_total_count += quarters
        coins_total_amount += quarters * 25

        dimes = cents_left // 10
        cents_left -= dimes * 10
        coins_total_count += dimes
        coins_total_amount += dimes * 10

        pennies = cents_left
        cents_left -= pennies
        coins_total_count += pennies
        coins_total_amount += pennies

        msg = "$" + str(amount) + " makes " + str(quarters) + " quarters, " + \
            str(dimes) + " dimes, and " + str(pennies) + " pennies (" + \
            str(coins_total_count) + " coins), total amount in coins: $" + \
            str(coins_total_amount / 100) + "."
        print(msg)

        

        

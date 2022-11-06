# Indentation is very important in if else statements

is_hot = ''

if is_hot:
    print("It's a hot day")

else:
    print("Its cool day")

buyer_good_credit = False
buyer_bad_credit = False
if buyer_good_credit:
    print('they need to put down 10%')

elif buyer_bad_credit:
    print('they need to put down 20%')

else:
    print('print the down payment')

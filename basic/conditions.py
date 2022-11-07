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

                        #COMPARISION OPERATORS
temp = 5

if temp > 30:
    print("it's a hot day")

elif temp < 10:
    print("It's a cold day")

else:
    print("It's neither hot nor cold")

                        #lOGICAL OPERATOR

has_credit = False
has_money = False

if has_credit and has_money:
    print('You are eligible')

elif has_credit and not has_money:
    print('you are Poor')

elif not has_credit and has_money:
    print('you are rich')

elif has_credit or has_money:
    print('You need support')

else:
    print('you are eliminated')




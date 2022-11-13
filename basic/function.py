                            #   PYTHONF FUNCTION DEFINITION
def myNum():
    yourName = "My name is 'Hello World'"
    print(yourName)
    # return yourName # by default python return None, if we don't print anythin

print(myNum())

                            # Parameter Definition
def myParam(Name, age):
    print(f"{Name} is {age} Years Old")

myParam('Asif', 28)

                            # Argument Keyword
def myParam2(product, cost):
    details = f"{product} is {cost} Tk"
    print(details)

myParam2(cost=50, product="medicine")




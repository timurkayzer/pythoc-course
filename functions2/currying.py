from functools import partial

MILK = 10
MILK_TAX = 0.1
BEEF = 30
BEEF_TAX = 0.15

def tax_for_purchases(product,amount,tax):
    return product*amount*tax

tax_to_milk = partial(tax_for_purchases, tax=MILK_TAX, product=MILK)
tax_to_beef = partial(tax_for_purchases, tax=BEEF_TAX, product=BEEF)


print(tax_to_beef(amount=100))
print(tax_to_milk(amount=100))


my_print = partial(print,sep="^",end="\n")

my_print("a","A","b")
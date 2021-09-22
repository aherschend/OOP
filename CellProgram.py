import CellClass

def main():

    man = input("Who is your phone's manufacturer?  ")
    mod = input('Enter the model number:  ')
    retail = float(input('Enter the retail price:  '))

    phone = CellClass.cellclass(man, mod, retail)

    print('Here is the data you entered:')
    print('Manufactur:', phone.getmanufact())
    print('Model Number:', phone.get_model())
    print('Retail Price: $', format(phone.get_retail_price(), ',.2f', sep = ''))


main()

    
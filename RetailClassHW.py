import RetailItem as ri

def main():

    item1 = ri.RetailItem('Jacket', 12 ,59.95)
    item2 = ri.RetailItem('Designer Jeans', 40, 34.95)
    item3 = ri.RetailItem('Shirt', 20 ,24.95)

    item1.get_description()
    item1.get_unitsininventory()
    item1.get_price()

    item2.get_description()
    item2.get_unitsininventory()
    item2.get_price()

    item3.get_description()
    item3.get_unitsininventory()
    item3.get_price()

main()









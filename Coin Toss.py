import CoinClass as c
# c is just an alias, importing the file to use in the code

# The main function.
def main():
       # Create an object from the Coin(came from other file) class.
       my_coin = c.Coin()   # this creates an instance called 'my_coin' of the class 'Coin()'

       # Display the side of the coin that is facing up.
       # We initialized heads so that is what side it will say is up
       print('This side is up:', my_coin.get_sideup())    # notice you do not have to supply the argument/parameter

       # Toss the coin.
       print('I am going to toss the coin ten times:')
       for count in range(10):
           my_coin.toss()
           
           #user could have control over this code, so we need to make our attributes private
           #because it's hidden, he can't access it
           my_coin.sideup = 'Heads'

           # Display the side of the coin that is facing up.
           print('This side is up:', my_coin.get_sideup())

           


       

# Call the main function.

main()

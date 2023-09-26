from numpy import random
import time
MIN_NUMBER = 0
MAX_NUMBER = 150

def game():
    ''' The game in itself    
    '''
    
    # The random number to guess
    r = random.randint(MIN_NUMBER,MAX_NUMBER)
    found = False
    
    # (Eternal) loop
    while not found:
        
        entry = input("\nEnter a number between "+str(MIN_NUMBER)+" and "+str(MAX_NUMBER)+": ")
        while not entry.isdigit():
            print("please input a number")
            entry = input("\nEnter a number between "+str(MIN_NUMBER)+" and "+str(MAX_NUMBER)+": ")

        entry = int(entry)
        # Condition on what to do
        if entry == r:
            print("\n\nGood job, it was "+str(r)+"!!!")
            found=True
        elif entry>150 or entry<0:
            print("You didn't enter a valid number. 10 seconds to think about it.")
            time.sleep(10)
        elif entry>=(r+20):
            print("You're too high!")
        elif entry>r:
            print("You're high but not that far!")
        elif (entry+20)>=r:
            print("A bit more?")
        else:
            print("You are too low!")
    	
 
# Start the game only if you wish
game()
player = input("Do you wanna start the game again? (y/n): ")
while player == "y":
    game()
	
print("Thanks for playing!")
time.sleep(1)



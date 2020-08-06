# Collatz Sequence
def collatz(number):
	if number % 2 == 0:
		return number // 2
	else:
		return 3 * number + 1
	# function checks if number is even, if not multiplies the number by 3 and adds 1

print('Hey wanna see somthing cool :), \n Type any number:')
try: # Use try and except block to catch errors
    collatz_calc = '' 
    while collatz_calc != 1: # keep getting input from user till the program hits one
	    user_input = int(input('')) # Gets an integer value from the user
	    collatz_calc = collatz(user_input)
	    print(collatz_calc)
except:
	print('ValueError("Non int type value passed :(")')

print('This is a little something called the collatz sequence :)', end='')
print("No matter what integer you use you'll inevitably end up at 1")

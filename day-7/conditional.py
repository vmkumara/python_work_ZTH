###  if condition1 
        # Code to execute if condition1 is True
###  elif condition2:
        # Code to execute if condition2 is True
###  elif condition3:
        # Code to execute if condition3 is True
# ...
###  else:
        # Code to execute if none of the conditions are True.

import sys  ##[[user is passing input(import), i can read the CommandLineArgument(sys) that user is passing]]

type = sys.argv[1] ##[[defing a variable called type, am taking the value using the sys.argv[1] from commandlineargument]]

if type == "t2.micro":
    print("This will has no charge")
elif type == "t2.medium":
    print("This will charge you $2 per day")
elif type == "t3.medium":
    print("This will charge you $4 per day")
elif type == "t5.xlarge":
    print("This will charge you $10 per day")

else:
    print("Invalid_output")

"""
Elmos_Cheez-its: Amanda Tan, Ethan Sie, Aidan Wong
SoftDev
K14 - User Input with Flask
2024-10-07
time spent: 0.7
"""

def goo():
    return "this is return string from goo() in test module"

# Print statements appear regardless of which python file is run using flask, Only appears on first run (dosen't repeat upon page refresh)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("this print statement came from test module")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

# Printed when this python file is run using flask (through python testmod0.py)
if __name__ == "__main__": #false if this file imported as module
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("this CONDITIONAL print statement came from test module")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

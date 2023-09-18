"""main script of project"""

import grade_compute as gc

print("Hello. Welcome to the main assignment.\nHere to assist with grading. ")
cont = 0
#checks to make sure that user wants to continue program 
while cont == 0:
    cont = gc.main()

print("It seems like you have quit. Thank you for using this program.")
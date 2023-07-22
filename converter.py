print("How many kilometers do you ran today")
kms = input()
miles = float(kms)/1.60934
miles = round(miles, 2)
print(f"Your {kms}km was {miles}mi ")


# Explanation of this code;
# print--> is used to print out either a variable or text to be displayed 
# input--> it is use for inputing text or numbers, anything, just as the use of textbox in MS-Word
# float--> is a number without decimal or a int without decimal 
# round--> it is used to round up int also known as numbers to the given nearest number, i.e to round up the int/number to 2 decimal places 
# f--> f-string is used for concatinating words with variable and adding calling braces bracket when using the f-strings
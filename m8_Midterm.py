# ====================================
# Attached: Midterm
# ====================================
# File: Project #1
# ====================================
# Name: Calories from Fat and Carbohydrates
# ====================================
# Programmer: Jacqueline Ceballos
# Class: CMPR 114
# ====================================

def main():
    # asking the members for the number of fat grams and carbohydrates grams that they consumed in a day
    fat_grams = float(input("What is the number of fat grams that you consume in a day? "))
    carbohydrates_gram = float(input("What is the number of carbohydrates grams that you consume in a day? "))
    # calling the two functions
    show_calories_from_fat(fat_grams)
    show_calories_from_carbohydrates(carbohydrates_gram)


# the show_calories_from_fat function accepts the fat gram as an argument
# and displays the total calories for the amount consumed.
def show_calories_from_fat(fat_grams):
    # calculating the number of calories that results from the fat
    calories = fat_grams * 9
    print(f"\nThe total calories consumed from fat grams is {calories}.")


# the show_calories_from_carbohydrates function accepts the carbohydrates' gram as an argument
# and displays the total calories for the amount consumed.
def show_calories_from_carbohydrates(carbohydrates_gram):
    # calculating the number of calories from the carbohydrates
    calories = carbohydrates_gram * 4
    print(f"The total calories consumed from carbohydrates grams is {calories}.")


# calling the main function
main()

''''
=================== Output ===========================
What is the number of fat grams that you consume in a day? 32
What is the number of carbohydrates grams that you consume in a day? 12

The total calories consumed from fat grams is 288.0.
The total calories consumed from carbohydrates grams is 48.0.

Process finished with exit code 0


'''

# ====================================
# Attached: Midterm
# ====================================
# File: Project #2
# ====================================
# Name: Coffee
# ====================================
# Programmer: Jacqueline Ceballos
# Class: CMPR 114
# ====================================

# this program will read from the file
def read():
    infile = open("Coffee.txt", "r")

    fileContents = infile.read()

    infile.close()
    
    # display what is in the file
    print(fileContents)


# calling the read function
read()

''''
=================== Output ===========================
Description,ProdNum,Price
Bolivian Dark,14-001,8.95
Bolivian Medium,14-002,8.95
Brazilian Dark,15-001,7.95
Brazilian Medium,15-002,7.95
Brazilian Decaf,15-003,8.55
Central American Dark,16-001,9.95
Central American Medium,16-002,9.95
Sumatra Dark,17-001,7.95
Sumatra Decaf,17-002,8.95
Sumatra Medium,17-003,7.95
Sumatra Organic Dark,17-004,11.95
Kona Medium,18-001,18.45
Kona Dark,18-002,18.45
French Roast Dark,19-001,9.65
Galapagos Medium,20-001,6.85
Guatemalan Dark,21-001,9.95
Guatemalan Decaf,21-002,10.45
Guatemalan Medium,21-003,9.95

Process finished with exit code 0


'''

# ====================================
# Attached: Midterm
# ====================================
# File: Project #3
# ====================================
# Name: Coffee (Part 2)
# ====================================
# Programmer: Jacqueline Ceballos
# Class: CMPR 114
# ====================================

# this function will allow the user to write the input
def writeCoffee():
    # writing to the default directory
    outfile = open("coffee.txt", "a")

    # asking the user the following
    num1 = input("Enter your favorite coffee brand: ")
    num2 = input("Enter the prod number: ")
    num3 = input("Enter the price: $")

    # writing the contents to a file
    outfile.write("\n" + str(num1) + ",")
    outfile.write(str(num2) + ",")
    outfile.write(str(num3))

    # displaying that the information has been recorded
    print("Data Recorded!\n")


# calling the write function
writeCoffee()


# this function will read from the file
def readCoffee():
    infile = open("coffee.txt", "r")

    fileContents = infile.read()

    infile.close()

    # display what is in the file
    print(fileContents)


# calling the read function
readCoffee()

''''
=================== Output ===========================
Enter your favorite coffee brand: Nescafe
Enter the prod number: 99-8888
Enter the price: $9.88
Data Recorded!

Description,ProdNum,Price
Bolivian Dark,14-001,8.95
Bolivian Medium,14-002,8.95
Brazilian Dark,15-001,7.95
Brazilian Medium,15-002,7.95
Brazilian Decaf,15-003,8.55
Central American Dark,16-001,9.95
Central American Medium,16-002,9.95
Sumatra Dark,17-001,7.95
Sumatra Decaf,17-002,8.95
Sumatra Medium,17-003,7.95
Sumatra Organic Dark,17-004,11.95
Kona Medium,18-001,18.45
Kona Dark,18-002,18.45
French Roast Dark,19-001,9.65
Galapagos Medium,20-001,6.85
Guatemalan Dark,21-001,9.95
Guatemalan Decaf,21-002,10.45
Guatemalan Medium,21-003,9.95
Nescafe,99-8888,9.88

Process finished with exit code 0


'''

# ====================================
# Attached: Midterm
# ====================================
# File: Project #4
# ====================================
# Name: Expenses
# ====================================
# Programmer: Jacqueline Ceballos
# Class: CMPR 114
# ====================================

# this function will allow the user to write the input
def write():
    # writing to the default directory
    expenses = open("expenses.txt", "a")

    # asking the user the following
    rent = input("Enter your rent for this month: $")
    gas = input("Enter how much money you wasted on gas this month: $")
    food = input("Enter how much money you wasted on food this month: $")
    clothing = input("Enter how much money you wasted on clothing this month: $")
    car_payment = input("Enter your car payment for this month: $")

    # writing and formatting the contents to a file
    expenses.write("----Monthly Expenses----")
    expenses.write("\nRent: $" + str(rent) + "\n")
    expenses.write("Gas: $" + str(gas) + "\n")
    expenses.write("Food: $" + str(food) + "\n")
    expenses.write("Clothing:$ " + str(clothing) + "\n")
    expenses.write("Car payment: $" + str(car_payment) + "\n")

    # closing the file
    expenses.close()

    # displaying that the information has been recorded
    print("\n Expenses recorded! \n")


# calling the write function
write()


# this function will read from the file
def read():
    infile = open("expenses.txt", "r")

    fileContents = infile.read()

    infile.close()

    # display what is in the file
    print(fileContents)


# calling the read function
read()

''''
=================== Output ===========================
Enter your rent for this month: $1200
Enter how much money you wasted on gas this month: $140
Enter how much money you wasted on food this month: $200
Enter how much money you wasted on clothing this month: $0
Enter your car payment for this month: $305

 Expenses recorded! 

----Monthly Expenses----
Rent: $1200
Gas: $140
Food: $200
Clothing:$ 0
Car payment: $305


Process finished with exit code 0



'''

# ====================================
# Attached: Midterm
# ====================================
# File: Project #5
# ====================================
# Name: List
# ====================================
# Programmer: Jacqueline Ceballos
# Class: CMPR 114
# ====================================

def main():
    # creating a 1-D list with the numbers 20-30
    numbers = [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]

    # creating a variable
    total = 0

    for value in numbers:
        # total the number in the list
        total += value

    # the lens function returns the number of items in the list
    # calculating the average
    average = total / len(numbers)

    # displaying the total and average
    print("The total is", total)
    print("The average is", average)

# calling the main function
main()

''''
=================== Output ===========================
The total is 275
The average is 25.0

Process finished with exit code 0

'''


# ====================================
# Attached: Midterm
# ====================================
# File: Project #6
# ====================================
# Name: List (Part 2)
# ====================================
# Programmer: Jacqueline Ceballos
# Class: CMPR 114
# ====================================

def main():
    # creating a 1-D list with the numbers 20-30
    numbers = ["20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30"]

    # using index function to access an item and displaying it
    print("Lucky number:", numbers[7])


# calling the main function
main()

''''
=================== Output ===========================
Lucky number: 27

Process finished with exit code 0

'''


# ====================================
# Attached: Midterm
# ====================================
# File: Project #7
# ====================================
# Name: 2-D List
# ====================================
# Programmer: Jacqueline Ceballos
# Class: CMPR 114
# ====================================

def main():
    # creating a 2-D list with the number 1-10
    values = [1, 2, 3, 4, 5], [6, 7, 8, 9, 10]

    # using index function to access an item and displaying it
    print("Lucky number:", values[1][1])


# calling the main function
main()

''''
=================== Output ===========================
Lucky number: 7

Process finished with exit code 0

'''

# ====================================
# Attached: Midterm
# ====================================
# File: Project #8
# ====================================
# Name: Randomizing
# ====================================
# Programmer: Jacqueline Ceballos
# Class: CMPR 114
# ====================================
import random


def main():
    # creating a list of 5 random names
    names = ["Ashely", "Nick", "Jonas", "Rob", "Jazmine"]

    # using a for loop to randomly choose and print the names
    for i in names:
        choice = random.choice(names)

        print(choice)


# calling the main function
main()

''''
=================== Output ===========================
Jonas
Rob
Ashely
Jonas
Jazmine

Process finished with exit code 0

'''

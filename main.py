# CEASER CIPHER
# alphabet = [' ','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# def encode(text, shift):
#   new_text = ""
#   for x in text:
#     position = alphabet.index(x) + shift
#     new_text += alphabet[position]
#   print(new_text)

# def decode(text, shift):
#   new_text = ""
#   for x in text:
#     position = alphabet.index(x) - shift
#     new_text += alphabet[position]
#   print(new_text)

# proceed = False
# while proceed == False:
#   direction = input(f"Type 'encode' to encode a text or 'decode' to decode a text. \n")
#   print(direction)
#   if direction == "encode" or direction == "decode":
#     input_text = input("Type your text: \n").lower()
#     shift = int(input("Type your shift: \n"))
#     if direction == "encode":
#       encode(text=input_text, shift=shift)
#     elif direction == "decode":
#       decode(text=input_text, shift=shift)
#     proceed = True
#   else:
#     print("Please type the correct direction.")
#     proceed = False

# def is_leap(year):
#   if year % 4 == 0:
#     if year % 100 == 0:
#       if year % 400 == 0:
#         return True
#       else:
#         return False
#     else:
#       return True
#   else:
#     return False

# def days_in_month(year, month):
#   month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
#   if is_leap(year):
#     month_days[1] = 29 
#   selected_month = month_days[month-1]
#   return f"In year {year} month {month} is {selected_month} days."
  
# print(days_in_month(int(input("Enter year: ")), int(input("Enter month: "))))

# logo = """
#  _____________________
# |  _________________  |
# | | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
# | |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
# |  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
# | | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
# | |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
# | | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
# | |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
# | | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
# | |___|___|___| |___| | | |              | || |              | || |              | || |              | |
# | | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
# | |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
# |_____________________|
# """
# print(logo)

# def addition(a,b):
#   return a+b
# def substraction(a,b):
#   return a-b
# def multiplication(a,b):
#   return a*b
# def dividation(a,b):
#   return a/b
# def modulas(a,b):
#   return a%b

# operation_val = {"+": addition, "-":substraction, "*":multiplication, "/":dividation, "%":modulas}

# f_num = int(input("Enter your first number: "))
# for x in operation_val:
#   print(x)
# operation = operation_val[input("Enter your operation: ")]
# l_num = int(input("Enter your last number: "))
# print(f"The result of your calculation is: {operation(f_num,l_num)}")

from turtle import Turtle, Screen
import random

colours = ["red", "orange", "yellow", "green", "blue", "purple"]

screen = Screen()
screen.setup(width=600, height=400)
screen.bgcolor("lightgray")

turtles = []
for x in range(6):
    turtle_x = Turtle(shape="turtle")
    turtle_x.penup()
    turtle_x.color(colours[x])
    turtle_x.goto(x=-280, y=(-130 + (x*50)))
    turtles.append(turtle_x)

is_race_on = False
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win? Enter a colour: ")

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in turtles:
        if turtle.xcor() >= 280:
            is_race_on = False
            winning_colour = turtle.pencolor()
            if winning_colour == user_bet:
                print(f"You've won! The {winning_colour} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_colour} turtle is the winner!")
        turtle.forward(random.randint(0,10))



# screen.exitonclick()
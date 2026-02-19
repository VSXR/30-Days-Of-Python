# ## 💻 Exercises - Day 2

# ### Exercises: Level 1
# 1. Inside 30DaysOfPython create a folder called day_2. Inside this folder create a file named variables.py
# 2. Write a python comment saying 'Day 2: 30 Days of python programming'
# Day 2: 30 Days of python programming

# 3. Declare a first name variable and assign a value to it
first_name= "Victor "

# 4. Declare a last name variable and assign a value to it
last_name= "Sanz"

# 5. Declare a full name variable and assign a value to it
full_name= first_name + last_name

# 6. Declare a country variable and assign a value to it
conuntry_variable= "Spain"

# 7. Declare a city variable and assign a value to it
city_variable="Madrid"

# 8. Declare an age variable and assign a value to it
age= 21

# 9. Declare a year variable and assign a value to it
year= 2026

# 10. Declare a variable is_married and assign a value to it
is_married= True

# 11. Declare a variable is_true and assign a value to it
is_True= True

# 12. Declare a variable is_light_on and assign a value to it
is_light_on= False

# 13. Declare multiple variable on one line
first_name, last_name, country, age, is_married = "Victor ", "Sanz", "Spain", 21, True


# ### Exercises: Level 2
# 1. Check the data type of all your variables using type() built-in function
print(type(first_name))
print(type(last_name))
print(type(country))
print(type(age))
print(type(is_married))

# 2. Using the _len()_ built-in function, find the length of your first name
print(f"La longitud de mi nombre es de {len(first_name)} letras")

# 3. Compare the length of your first name and your last name
if len(first_name) > len(last_name):
    print("Mi NOMBRE es mas largo que mi apellido")
else:
    print("Mi APELLIDO es mas largo que mi nombre")

# 4. Declare 5 as num_one and 4 as num_two
num_one= 5
num_two= 4

# 5. Add num_one and num_two and assign the value to a variable total
total= num_one + num_two

# 6. Subtract num_two from num_one and assign the value to a variable diff
diff= num_two - num_one

# 7. Multiply num_two and num_one and assign the value to a variable product
product= num_two * num_one

# 8. Divide num_one by num_two and assign the value to a variable division
division= num_one / num_two

# 9. Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
remainder= num_two % num_one

# 10. Calculate num_one to the power of num_two and assign the value to a variable exp
exp= num_one ** num_two

# 11. Find floor division of num_one by num_two and assign the value to a variable floor_division
floor_division= num_one // num_two

# 12. The radius of a circle is 30 meters.
#     1. Calculate the area of a circle and assign the value to a variable name of _area_of_circle_
#     2. Calculate the circumference of a circle and assign the value to a variable name of _circum_of_circle_
#     3. Take radius as user input and calculate the area.
radius= 30
pi= 3.14
_area_of_circle_= pi * radius**2
_circum_of_circle_= 2 * pi * radius
print(_area_of_circle_)
print(_circum_of_circle_)

new_radius= input("Introduce el valor del radio que desees: ")
print(f"El area respecto al radio dado es: {pi * float(new_radius)**2} metros")

# 13. Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
first_name= input("Nombre: ")
last_name= input("Apellido: ")
country= input("Pais: ")
age= int(input("Edad: "))
print(first_name, last_name, country, age)

# 14. Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords
help("keywords")
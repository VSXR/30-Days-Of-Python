# ## 💻 Exercises - Day 3
import math

# 1. Declare your age as integer variable
age= 21

# 2. Declare your height as a float variable
height= 1.78

# 3. Declare a variable that store a complex number
complex_number= 1j

# 4. Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
# ```py
#     Enter base: 20
#     Enter height: 10
#     The area of the triangle is 100
# ```
base= int(input("Introduce la medida de la base: "))
height= int(input("Introduce la medida de la altura: "))
area= 0.5 * base * height
print(f"El area del triangulo es: {area}")

# 5. Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
# ```py
# Enter side a: 5
# Enter side b: 4
# Enter side c: 3
# The perimeter of the triangle is 12
# ```
side_a= int(input("Introduce el lado A del triangulo: "))
side_b= int(input("Introduce el lado B del triangulo: "))
side_c= int(input("Introduce el lado C del triangulo: "))
perimeter= side_a + side_b + side_c
print(f"El perimetro del triangulo es: {perimeter}")

# 6. Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
length= int(input("Introduce el largo del rectangulo: "))
width= int(input("Introduce el ancho del rectangulo: "))
area= length * width
perimeter= 2 * (length * width)
print(f"El area del rectangulo es: {area} y su permietro es: {perimeter}")

# 7. Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
pi= 3.14
radius= int(input("Introduce el radio de la circunferencia: "))
area= pi * radius * radius
circumference= 2 * pi * radius
print(f"El area de la cirunferencia es: {area} y su circunferencia es: {circumference}")

# 8. Calculate the slope, x-intercept and y-intercept of y = 2x -2
# y= mx + b
# m es el slope
# b es el y-intercept
m= 2
b= -2

# Pendiente
slope_1= m

# Intersección en Y (cuando x = 0)
y_intercept= (0, b)

# Intersección en X (cuando y = 0, despejamos: x = -b / m)
x_val= -b / m
x_intercept= (x_val, 0)

print(f"Pendiente (m): {slope_1}")
print(f"Intersección en Y: {y_intercept}")
print(f"Intersección en X: {x_intercept}")

# 9. Slope is (m = y2-y1/x2-x1). Find the slope and [Euclidean distance](https://en.wikipedia.org/wiki/Euclidean_distance#:~:text=In%20mathematics%2C%20the%20Euclidean%20distance,being%20called%20the%20Pythagorean%20distance.) between point (2, 2) and point (6,10) 
x1, y1= 2, 2
x2, y2= 6, 10

slope_2= int((y2 - y1) / (x2 - x1))
euclidean_distance= int(math.sqrt((x1 - y1)**2 + (x2 - y2)**2))
print(f"La pendiente es: {slope_2} y la distnacia euclidea es: {euclidean_distance}")

# 10. Compare the slopes in tasks 8 and 9.
print(slope_1 == slope_2)

# 11. Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
x= int(input("Introduce el valor de X: "))
y= x**2 + 6*x + 9
print(f"Para x = {x}, el valor de y es {y}")

# 12. Find the length of 'python' and 'dragon' and make a falsy (!=) comparison statement.
len_python= "python"
len_dragon= "dragon"
falsy_comparison= len(len_python) != len(len_dragon)
print(f"El valor de la longitud de '{len_python}' es de {len(len_python)} y '{len_dragon}' es de {len(len_dragon)} --> Cmparacion: {falsy_comparison}")

# 13. Use _and_ operator to check if 'on' is found in both 'python' and 'dragon'
word_python= "python"
word_dragon= "dragon"
check= ("on" in word_python) and ("on" in word_dragon)
print(f"ESTAN las letras 'on' en las palabras '{word_python}' y '{word_dragon}'? --> {check}")

# 14. _I hope this course is not full of jargon_. Use _in_ operator to check if _jargon_ is in the sentence.
jargon_phrase= "I hope this course is not full of jargon"
check= ("jargon" in jargon_phrase)
print(f"¿Esta la palabra 'jargon' en la frase '{jargon_phrase}'? --> {check}")

# 15. There is no 'on' in both dragon and python
check= ("on" not in word_python) and ("on" not in word_dragon)
print(f"¿Las letras 'on' NO ESTAN en las palabras '{word_python}' y '{word_dragon}'? --> {check}")

# 16. Find the length of the text _python_ and convert the value to float and convert it to string
resultado= str(float(len(word_python)))
print(f"El valor de la longitud de la palabra '{word_python}' casteada de INT a FLOAT y de FLOAT a STR es de {resultado}")

# 17. Even numbers (Numeros Pares) are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
numbers= [8, 9, 10]
for i in range(0, len(numbers)):
    number= numbers[i]
    if(i % 2 == 0):
        print(f"El numero {number} es PAR")
    else:
        print(f"El numero {number} es IMPAR")

# 18. Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
converted_value= int(2.7)
7 // 3 == converted_value

# 19. Check if type of '10' is equal to type of 10
'10' == type(10)

# 20. Check if int('9.8') is equal to 10
int('9.8') == 10

# 21. Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
# ```py
# Enter hours: 40
# Enter rate per hour: 28
# Your weekly earning is 1120
# ```
hours= int(input("Introduce las horas trabajadas durante la semana: "))
rate_per_hour= int(input("Introduce lo que ganas cada hora trabajada: "))
print(f"Ganas un total de: {hours * rate_per_hour} euros por cada semana trabajada")

# 22. Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
# ```py
# Enter number of years you have lived: 100
# You have lived for 3153600000 seconds.
# ```
age= int(input("Enter number of years you have lived: "))
seconds_in_a_year= 86400 * 365  # 1 dia == 86400 segundos
print(f"You have lived for {age * seconds_in_a_year} seconds")

# 23. Write a Python script that displays the following table
# ```py
# 1 1 1 1 1
# 2 1 2 4 8
# 3 1 3 9 27
# 4 1 4 16 64
# 5 1 5 25 125
# ```
# OJO: el primer numero de cada fila es el i, el segundo la potencia de i elevado a 0, y asi sucesivamente!
for i in range(1, 6):
    print(f"{i} {i**0} {i**1} {i**2} {i**3}")

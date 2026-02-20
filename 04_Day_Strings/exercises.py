# 💻 Exercises - Day 4

# Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
str1= "Thirty "
str2= "Days "
str3= "Of "
str4= "Python"
full_string= str1 + str2 + str3 + str4
print(full_string)

# Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
string_list= ["Coding", "For", "All"]
full_string= " ".join(string_list)
print(full_string)

# Declare a variable named company and assign it to an initial value "Coding For All".
company= "Coding For All"

# Print the variable company using print().
print(company)

# Print the length of the company string using len() method and print().
print(len(company))

# Change all the characters to uppercase letters using upper() method.
print(company.upper())

# Change all the characters to lowercase letters using lower() method.
print(company.lower())

# Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
print(company.capitalize())
print(company.title())
print(company.swapcase())

# Cut(slice) out the first word of Coding For All string.
company_sliced= company[:6]
print(company_sliced)

# Check if Coding For All string contains a word Coding using the method index, find or other methods.
print(company.index("Coding"))  # 0 es correcto     -1 es incorrecto
print(company.find("Coding"))
print(company.rindex("Coding"))
print(company.rfind("Coding"))

# Replace the word coding in the string 'Coding For All' to Python.
company_python = company.replace("Coding", "Python")
print(company_python)

# Change "Python for Everyone" to "Python for All" using the replace method or other methods.
company= "Python for Everyone"
company_python= company.replace("Everyone", "All")

# Split the string 'Coding For All' using space as the separator (split()) .
company= "Coding For All"
company_split= company.split()
print(company_split)

# "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
companies_split= companies.split()
print(companies_split)

# What is the character at index 0 in the string Coding For All.
print(company[0])

# What is the last index of the string Coding For All.
print(company[-1])

# What character is at index 10 in "Coding For All" string.
print(company[10])

# Create an acronym or an abbreviation for the name 'Python For Everyone'.
company = "Python for Everyone"
words = company.split()  # ['Python', 'for', 'Everyone']
acronym= ""

for word in words:
    acronym += word[0].upper()
print(acronym)

# Create an acronym or an abbreviation for the name 'Coding For All'.
company = "Coding For All"
words = company.split()  # ['Python', 'for', 'All']
acronym= ""

for word in words:
    acronym += word[0].upper()
print(acronym)

# Use index to determine the position of the first occurrence of C in Coding For All.
print(company.index("C"))

# Use index to determine the position of the first occurrence of F in Coding For All.
print(company.index("F"))

# Use rfind to determine the position of the last occurrence of l in Coding For All People.
company = "Coding For All People"
print(company.rfind("l"))

# Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
sentence = "You cannot end a sentence with because because because is a conjunction"
print(sentence.find("because"))

# Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print(sentence.rindex("because"))

# Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print(sentence[sentence.find("because") : sentence.rfind("because") + len("because")])  # sentence[31:54] --> Sliceamos la b de because buscando primero por la izquierda y luego por el final de la derecha. A la b de la derecha le sumamos la longitud de la palabra because para coger 'ecause'

# Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print(sentence.index("because"))    # Si ponemos "Because" con mayuscula como no esta en la frase devuelve ValueError y EXPLOTA!
print(sentence.find("because"))     # Si ponemos "Because" con mayuscula como no esta en la frase devuelve -1

# Does 'Coding For All' start with a substring Coding?
sentence= "Coding For All"
print(sentence.startswith("Coding"))

# Does 'Coding For All' end with a substring coding?
print(sentence.endswith("Coding"))

# '   Coding For All      '  , remove the left and right trailing spaces in the given string.
sentence= "   Coding For All      "
print(sentence[sentence.find("Coding") : sentence.rfind("All") + len("All")].strip())
print(sentence.strip())

# Which one of the following variables return True when we use the method isidentifier():
# 30DaysOfPython
# thirty_days_of_python
variable1= "30DaysOfPython"
variable2= "thirty_days_of_python"
print(variable1.isidentifier())
print(variable2.isidentifier())

# The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
libraries_list= ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
resultado = " # ".join(libraries_list)
print(resultado)

# Use the new line escape sequence to separate the following sentences.
# I am enjoying this challenge.
# I just wonder what is next.
print("I am enjoying this challenge.\nI just wonder what is next.")

# Use a tab escape sequence to write the following lines.
# Name      Age     Country   City
# Asabeneh  250     Finland   Helsinki
# Definimos anchos fijos para que todo encaje como una cuadrícula
n, a, co, ci = 15, 8, 15, 10
print(f"{'Name':<{n}}{'Age':<{a}}{'Country':<{co}}{'City':<{ci}}")
print(f"{'Asabeneh':<{n}}{'250':<{a}}{'Finland':<{co}}{'Helsinki':<{ci}}")

# Use the string formatting method to display the following:
# radius = 10
# area = 3.14 * radius ** 2
# The area of a circle with radius 10 is 314 meters square.
radius = 10
area = 3.14 * radius ** 2
print("radius = {}".format(radius))
print("area = 3.14 * {}**2".format(radius))
print("The area of a circle with radius {} is {} meters square.".format(radius, area))

# Make the following using string formatting methods:
# 8 + 6 = 14
# 8 - 6 = 2
# 8 * 6 = 48
# 8 / 6 = 1.33
# 8 % 6 = 2
# 8 // 6 = 1
# 8 ** 6 = 262144
a, b = 8, 6

print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b:.2f}")  # :.2f para los decimales
print(f"{a} % {b} = {a % b}")
print(f"{a} // {b} = {a // b}")
print(f"{a} ** {b} = {a ** b}")

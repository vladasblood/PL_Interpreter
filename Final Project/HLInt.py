import re
import sys
from tkinter import filedialog
import tkinter as tk

file_path = filedialog.askopenfilename(filetypes=[("HL", "*.HL")])
variable_types = {}
variables = {}

#Functions
#Before closing
def finalProcess():
    newLinesForAppend = ""
    with open(file_path, 'r') as file:
        # Read the entire contents of the file into a string
        file_contents = file.read()

    # Split the file contents into lines using semicolon as the delimiter
    lines = file_contents.split(';')
    for line in lines:
        newLinesForAppend = newLinesForAppend + re.sub(r'\s', '', line)

    with open('NOSPACES.txt', 'w') as file:
        file.write(newLinesForAppend + "\n")


    # Append reserved words and symbols to RES_SYM.TXT
    appendForRes = ""
    if "integer" in newLinesForAppend:
        appendForRes += "integer "
    if "double" in newLinesForAppend:
        appendForRes += "double "
    if "if" in newLinesForAppend:
        appendForRes += "if "
    if "output" in newLinesForAppend:
        appendForRes += "output "
    if "+" in newLinesForAppend:
        appendForRes += "+ "
    if "-" in newLinesForAppend:
        appendForRes += "- "

    with open('RES_SYM.txt', 'w') as file:
        file.write(appendForRes)

#Declare Variable Type
def variableDeclaration(newline):
    line = re.sub(r'\s', '', newline)
    variable_name, variable_type = line.split(":")
    if variable_type != "integer" and variable_type != "double":
        print("ERROR")
        finalProcess()
        input("Press Enter to exit...")
        sys.exit()
    else:
        variable_types[variable_name.replace(" ", "")] = variable_type.replace(" ", "")

#Assign Variables
def assignment(newline):
    line = re.sub(r'\s', '', newline)
    variable_name, value = line.split(":=")
    if variable_types[variable_name] == "integer":
        variables[variable_name] = int(value)
    elif variable_types[variable_name] == "double":
        variables[variable_name] = float(value)
    else:
        print("ERROR")
        finalProcess()
        input("Press Enter to exit...")
        sys.exit()


#Mathematical Operations
def mathematicalOperations(newline):
    line = re.sub(r'\s', '', newline)
    if "=" in line:
        if "+" in line:
            leftside, rightside = line.replace(" ", "").split("=")
            variableToUpdate = leftside
            numbers = rightside.replace(" ", "").split("+")
            for i, number in enumerate(numbers):
                if type(number) is not float:
                    if number in variables:
                        numbers[i] = float(variables[number])
            output = 0.0
            for number in numbers[1:]:
                if type(number) is not float:
                    if number in variables:
                        number = float(variables[number])
                output += float(number)
            if output.is_integer():
                print(int(output))
                print("NO ERROR(S) FOUND")
                finalProcess()
            else:
                print(output)
                print("NO ERROR(S) FOUND")
                finalProcess()
        elif "-" in line:
            leftside, rightside = line.replace(" ", "").split("=")
            variableToUpdate = leftside
            numbers = rightside.replace(" ", "").split("-")
            for i, number in enumerate(numbers):
                if type(number) is not float:
                    if number in variables:
                        numbers[i] = float(variables[number])
            output = float(numbers[0])
            for number in numbers[1:]:
                if type(number) is not float:
                    if number in variables:
                        number = float(variables[number])
                output -= float(number)
            if output.is_integer():
                print(int(output))
                print("NO ERROR(S) FOUND")
                finalProcess()
            else:
                print(output)
                print("NO ERROR(S) FOUND")
                finalProcess()
    else:
        if "+" in line:
            numbers = line.replace(" ", "").split("+")
            for i, number in enumerate(numbers):
                if type(number) is not float:
                    if number in variables:
                        numbers[i] = float(variables[number])
            output = 0.0
            for number in numbers:
                if type(number) is not float:
                    if number in variables:
                        number = float(variables[number])
                output += float(number)
            if output.is_integer():
                print(int(output))
                print("NO ERROR(S) FOUND")
                finalProcess()
            else:
                print(output)
                print("NO ERROR(S) FOUND")
                finalProcess()
        elif "-" in line:
            numbers = line.replace(" ", "").split("-")
            for i, number in enumerate(numbers):
                if type(number) is not float:
                    if number in variables:
                        numbers[i] = float(variables[number])
            output = float(numbers[0])
            for number in numbers[1:]:
                if type(number) is not float:
                    if number in variables:
                        number = float(variables[number])
                output -= float(number)
            if output.is_integer():
                print(int(output))
                print("NO ERROR(S) FOUND")
                finalProcess()
            else:
                print(output)
                print("NO ERROR(S) FOUND")
                finalProcess()

#Print output
def printOutput(line):
    if "output << " in line:
        text_after_output = line.split("output << ")[1].replace(" ", "")
    elif "output <<" in line:
        text_after_output = line.split("output <<")[1].replace(" ", "")
    elif "output<< " in line:
        text_after_output = line.split("output<< ")[1].replace(" ", "")
    elif "output<<" in line:
        text_after_output = line.split("output<<")[1].replace(" ", "")
    else:
        print("ERROR")
        finalProcess()
        input("Press Enter to exit...")
        sys.exit()

    if text_after_output.strip().startswith("<"):
        print("ERROR")
        finalProcess()
        input("Press Enter to exit...")
        sys.exit()

    if text_after_output.startswith('"') and text_after_output.endswith('"'):
        # Remove the double quotes and add to the output_text list
        extracted_text = text_after_output[1:-1]
        print(extracted_text)
        print("NO ERROR(S) FOUND")
        finalProcess()
    else:
        if text_after_output in variables:
            if variable_types[text_after_output] == "integer":
                print(int(variables[text_after_output]))
                print("NO ERROR(S) FOUND")
                finalProcess()
            else:
                print(float(variables[text_after_output]))
                print("NO ERROR(S) FOUND")
                finalProcess()
        elif "+" or "-" in text_after_output:
            mathematicalOperations(text_after_output)
        else:
            print("ERROR")
            finalProcess()
            input("Press Enter to exit...")
            sys.exit()


#Condition
def execute_condition(main):
    if "==" in main:
        line = re.sub(r'\s', '', main)
        matches = re.search(r'\(([^=]+)==([\d.]+)\)', line)
        partsWithoutSpace = line.split(')')
        partsWithSpace = main.split(')')
        toExecute = partsWithoutSpace[1]
        finalLine = partsWithSpace[1]
        variable = matches.group(1)
        comparison = matches.group(2)
        if variable in variables:
            if float(variables[variable]) == float(comparison):
                if ":" in toExecute:
                    if ":=" in toExecute:
                        assignment(toExecute)
                    else:
                        variableDeclaration(toExecute)
                elif "if" in toExecute:
                    execute_condition(toExecute)
                elif "output<<" in toExecute:
                    printOutput(finalLine)
                elif "=" in toExecute:
                    if "+" and "-" in toExecute:
                        mathematicalOperations(toExecute)
                    else:
                        print("ERROR")
                        finalProcess()
                        input("Press Enter to exit...")
                        sys.exit()
                elif toExecute.strip() == "":
                    toExecute.strip()
                else:
                    print("ERROR")
                    finalProcess()
                    input("Press Enter to exit...")
                    sys.exit()
    elif "!=" in main:
        line = re.sub(r'\s', '', main)
        matches = re.search(r'\(([^=]+)!=([\d.]+)\)', line)
        partsWithoutSpace = line.split(')')
        partsWithSpace = main.split(')')
        toExecute = partsWithoutSpace[1]
        finalLine = partsWithSpace[1]
        variable = matches.group(1)
        comparison = matches.group(2)
        if variable in variables:
            if float(variables[variable]) != float(comparison):
                if ":" in toExecute:
                    if ":=" in toExecute:
                        assignment(toExecute)
                    else:
                        variableDeclaration(toExecute)
                elif "if" in toExecute:
                    execute_condition(toExecute)
                elif "output<<" in toExecute:
                    printOutput(finalLine)
                elif "=" in toExecute:
                    if "+" and "-" in toExecute:
                        mathematicalOperations(toExecute)
                    else:
                        print("ERROR")
                        finalProcess()
                        input("Press Enter to exit...")
                        sys.exit()
                elif toExecute.strip() == "":
                    toExecute.strip()
                else:
                    print("ERROR")
                    finalProcess()
                    input("Press Enter to exit...")
                    sys.exit()
    elif ">" in main:
        line = re.sub(r'\s', '', main)
        matches = re.search(r'\(([^=]+)>([\d.]+)\)', line)
        partsWithoutSpace = line.split(')')
        partsWithSpace = main.split(')')
        toExecute = partsWithoutSpace[1]
        finalLine = partsWithSpace[1]
        variable = matches.group(1)
        comparison = matches.group(2)
        if variable in variables:
            if float(variables[variable]) > float(comparison):
                if ":" in toExecute:
                    if ":=" in toExecute:
                        assignment(toExecute)
                    else:
                        variableDeclaration(toExecute)
                elif "if" in toExecute:
                    execute_condition(toExecute)
                elif "output<<" in toExecute:
                    printOutput(finalLine)
                elif "=" in toExecute:
                    if "+" and "-" in toExecute:
                        mathematicalOperations(toExecute)
                    else:
                        print("ERROR")
                        finalProcess()
                        input("Press Enter to exit...")
                        sys.exit()
                elif toExecute.strip() == "":
                    toExecute.strip()
                else:
                    print("ERROR")
                    finalProcess()
                    input("Press Enter to exit...")
                    sys.exit()
    elif "<" in main:
        line = re.sub(r'\s', '', main)
        matches = re.search(r'\(([^=]+)<([\d.]+)\)', line)
        partsWithoutSpace = line.split(')')
        partsWithSpace = main.split(')')
        toExecute = partsWithoutSpace[1]
        finalLine = partsWithSpace[1]
        variable = matches.group(1)
        comparison = matches.group(2)
        if variable in variables:
            if float(variables[variable]) < float(comparison):
                if ":" in toExecute:
                    if ":=" in toExecute:
                        assignment(toExecute)
                    else:
                        variableDeclaration(toExecute)
                elif "if" in toExecute:
                    execute_condition(toExecute)
                elif "output<<" in toExecute:
                    printOutput(finalLine)
                elif "=" in toExecute:
                    if "+" and "-" in toExecute:
                        mathematicalOperations(toExecute)
                    else:
                        print("ERROR")
                        finalProcess()
                        input("Press Enter to exit...")
                        sys.exit()
                elif toExecute.strip() == "":
                    toExecute.strip()
                else:
                    print("ERROR")
                    finalProcess()
                    input("Press Enter to exit...")
                    sys.exit()

# Main
# Read a text file with the code
root = tk.Tk()
root.withdraw()  # Hide the main window

if file_path:
    with open(file_path, 'r') as file:
        file_contents = file.read()
else:
    print("No file selected.")

# Open the file for reading
with open(file_path, 'r') as file:
    # Read the entire contents of the file into a string
    file_contents = file.read()

# Split the file contents into lines using semicolon as the delimiter
lines = file_contents.split(';')

# Check for unique tokens
for line in lines:
    newLine = line.replace("\n", "")
    stripped = newLine.strip()
    if ":" in newLine:
        if ":=" in newLine:
            assignment(newLine)
        else:
            variableDeclaration(newLine)
    elif "if" in newLine:
        execute_condition(newLine)
    elif "output<<" in newLine.strip():
        printOutput(newLine)
    elif "=" in newLine:
        if "+" and "-" in newLine:
            mathematicalOperations(newLine)
        else:
            print("ERROR")
            finalProcess()
            input("Press Enter to exit...")
            sys.exit()
    elif newLine.strip() == "":
        newLine.strip()
    else:
        print("ERROR")
        finalProcess()
        input("Press Enter to exit...")
        sys.exit()

input("Press Enter to exit...")

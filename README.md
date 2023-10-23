# CS145-8L Principles of Programming Language Laboratory

## Create a Simple Interpreter Project

**Description**: We created a simple interpreter using Python to translate various reserve words, data types, and other lexical symbols that can be prompted.

### Requirements
1. Variable Declaration
```python
x: integer;
y: double;
```

integer, double - data types

2. Assignment Statements
```python
x:=5;
y:=2.35;
```
3. Mathematical Operations
```python
x = 3 + 2;
y = 4 + 2.56;
```
*Addition and subtraction of single digit integers and double values with precision of 2*

4. Sending Output to Screen
```python
output<<"<string>">;
output<<value;
```

For Example: `output<<"hello"`;
   
5. Conditional Statement
*One-way if*
```python
if(<condition>)
  <statement>
```

Use this comparison operators: `>,<,==,!=`

```python
x:=6;
if(x<5)
  output<<x;
```
### The Process
When `HLInt.py` runs, it opens a source code, then it removes all spaces in the program and sends the contents "without spaces" to an output file named `NOSPACES.TXT` Then, it sends reserved words and symbols found in the program to `RES_SYM.TXT` Finally, it prints on the screen `ERROR` if it finds any syntax error in the program or `NO ERROR(S) FOUND` if there are no errors.
# How to Run?
## Fork the Repository
Fork the root directory folder, then proceed to "Final Project">>"dist">>"HLInt">>"HLInt.exe". 

Run the executable application window, and then it will prompt a selection of files from which you will redirect to any file with an ending of `.HL` file extensions.

## Run Test Case
Proceed to "Test_Files">>"Test Files">>"[PROG1.HL]" or "[PROG2.HL]" or "[PROG3.HL]"


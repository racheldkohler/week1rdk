Python 3.4.2 (v3.4.2:ab2c023a9432, Oct  5 2014, 20:42:22) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> WARNING: The version of Tcl/Tk (8.5.7) in use may be unstable.
Visit http://www.python.org/download/mac/tcltk/ for current information.

>>> # convert.py
>>> 	A program to convert Fahrenheit temps to Celsius
	
SyntaxError: unexpected indent
>>> # convert.py
>>> #	A program to convert Fehrenheit temps to Celsius
>>> #by: Rachel Kohler
>>> def main():
	farenheit = eval(input("What is the Fahrenheit temperature? "))
	celsius = 5/9 * (farenheit - 32)
	print("The temperature is ", celsius, "degrees Celsius.")

	
>>> main()
What is the Fahrenheit temperature? 32
The temperature is  0.0 degrees Celsius.
>>> 
>>> main()
What is the Fahrenheit temperature? 212
The temperature is  100.0 degrees Celsius.
>>> 

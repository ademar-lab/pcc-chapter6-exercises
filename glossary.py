# Store the meaning of the programming words
words = {
    "break": 
    "The break statement stops the while loop it is running in"
    " whenever it is reached",
        
    "try-except-else": 
    "The try-except-else block is used to keep your"
    " program from crashing whenever it reaches an error",
        
    "pass": 
    "The pass statement tells python to do nothing in a block",
        
    "JSON":
    "The JSON format stores different data structures fed directly"
    " by your program",
        
    "ZeroDivisionError":
    "The ZeroDivisionError is an exception object",

    "exceptions":
    "Python uses special objects that arise during a program's execution",

    "import":
    "The import statement lets you use code from another file in your"
    " program",

    "method":
    "A function that is part of a class",

    "attribute":
    "Attributes are variables available through instances of a class",
        
    "with":
    "The with keyword closes the file you are reading from when access"
    " to it is no longer needed",
    }

for key, value in words.items():
    print(f"\n{key}:\n{value}")
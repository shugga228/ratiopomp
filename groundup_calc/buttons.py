BUTTONS = [
    "0","1","2","3","4","5","6","7","8","9",
    ".","-","+","*","/","^","(",")",
    "sin(","cos(","tan(","log(","ln(",
    "pi","e","ANS",
    "BACK","CLEAR","ENTER",
    "UP","DOWN","LEFT","RIGHT","ALT"
]

BUTTON_LAYOUT = [
    ["7", "8", "9", "/", "sin("],
    ["4", "5", "6", "*", "cos("],
    ["1", "2", "3", "-", "tan("],
    ["0", "+/-", ".", "+", "log("],
    ["(", ")", "^", "ln(", "ANS"],
    ["e", "BACK", "CLEAR", "ENTER"],
    ["UP", "DOWN", "LEFT", "RIGHT"]  # NEW
]

ALT_MAP = {
    "sin(": "asin(",
    "cos(": "acos(",
    "tan(": "atan(",
    "0": "RESET",          # special reset function
    "/": "mod",            # modulus operation
    "*": "fact(",          # factorial
    ".": "TOGGLE_SCI"      # toggle scientific mode
}



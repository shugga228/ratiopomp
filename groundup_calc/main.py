from calculator import Calculator
from buttons import BUTTONS

def main():
    calc = Calculator()
    print("Ground-Up Calculator Prototype")
    print("Type button names or symbols, 'ENTER' to evaluate, 'QUIT' to exit.")

    while True:
        print("Display:", calc.get_display())
        key = input("Button> ").strip().upper()

        if key == "QUIT":
            print("<3")
            break
        elif key not in [b.upper() for b in BUTTONS]:
            print("Invalid button.")
            continue

        calc.press(key)
        print()

if __name__ == "__main__":
    main()

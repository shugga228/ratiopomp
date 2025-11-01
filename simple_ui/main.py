from calc_app import ScientificCalculator
#from graph_app import GraphApp
from textgraph import TextGraph


def home_screen():
    options = ["Scientific Calculator", "Graphing Function", "Exit"]
    current = 0

    while True:
        print("\n=== HOME MENU ===")
        for i, opt in enumerate(options):
            prefix = "→ " if i == current else "  "
            print(prefix + opt)

        choice = input("\nUse ↑ ↓ to navigate, Enter to select: ").strip().lower()

        if choice == "s":
            current = (current + 1) % len(options)
        elif choice == "w":
            current = (current - 1) % len(options)
        elif choice == "":
            selected = options[current]
            if selected == "Scientific Calculator":
                calc = ScientificCalculator()
                calc.run()
            elif selected == "Graphing Function":
        
                g = TextGraph()
                g.run()
            elif selected == "Exit":
                print("Goodbye!")
                break
        else:
            print("Invalid input. Use ↑ ↓ or press Enter.")

if __name__ == "__main__":
    home_screen()

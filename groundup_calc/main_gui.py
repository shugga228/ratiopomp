import tkinter as tk
from calculator import Calculator
from buttons import BUTTON_LAYOUT, ALT_MAP

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Ground-Up Calculator")
        self.calc = Calculator()
        self.alt_mode = False

        # --- Display ---
        self.display = tk.Entry(
            root, font=("Consolas", 18), justify="right", bd=10, relief=tk.RIDGE
        )
        self.display.grid(row=0, column=0, columnspan=6, ipadx=10, ipady=10, sticky="nsew")

        # --- Buttons ---
        self.buttons = []
        for r, row in enumerate(BUTTON_LAYOUT, start=1):
            for c, label in enumerate(row):
                b = tk.Button(
                    root,
                    text=label,
                    font=("Consolas", 16),
                    width=6,
                    height=2,
                    command=lambda l=label: self.on_press(l),
                )
                b.grid(row=r, column=c, sticky="nsew", padx=2, pady=2)
                self.buttons.append(b)

        # Add ALT button in its own column at the bottom
        alt_button = tk.Button(
            root,
            text="ALT",
            font=("Consolas", 16, "bold"),
            bg="#f0f0f0",
            width=6,
            height=2,
            command=lambda: self.on_press("ALT"),
        )
        alt_button.grid(row=len(BUTTON_LAYOUT) + 1, column=0, columnspan=6, sticky="nsew", padx=2, pady=2)
        self.buttons.append(alt_button)

        # --- Grid resizing ---
        total_rows = len(BUTTON_LAYOUT) + 2  # + display + alt row
        for i in range(total_rows):
            root.grid_rowconfigure(i, weight=1)
        for i in range(6):  # 6 columns now
            root.grid_columnconfigure(i, weight=1)

    def toggle_alt_mode(self):
        self.alt_mode = not self.alt_mode
        color = "#f0a500" if self.alt_mode else "#f0f0f0"
        # Change color of ALT button only
        for b in self.buttons:
            if b["text"] == "ALT":
                b.configure(bg=color)

    def on_press(self, label):
        # ALT button pressed
        if label == "ALT":
            self.toggle_alt_mode()
            return

        # ALT mode logic
        if self.alt_mode and label in ALT_MAP:
            alt_action = ALT_MAP[label]
            self.calc.press(alt_action)
            self.toggle_alt_mode()  # exit ALT mode
        else:
            self.calc.press(label.upper() if label in ["BACK", "CLEAR", "ENTER"] else label)

        # Update display
        self.display.delete(0, tk.END)
        self.display.insert(0, self.calc.get_display())

def main():
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()

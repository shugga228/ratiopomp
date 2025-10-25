import math
import re

class Calculator:
    def __init__(self):
        self.display = ""
        self.cursor_pos = 0
        self.last_answer = 0
        self.scientific_mode = False
        self.env = {
            "pi": math.pi,
            "e": math.e,
            "sin": math.sin,
            "cos": math.cos,
            "tan": math.tan,
            "asin": math.asin,
            "acos": math.acos,
            "atan": math.atan,
            "log": math.log10,
            "ln": math.log,
            "Ans": lambda: self.last_answer,
            "fact": math.factorial,
            "mod": lambda a, b: a % b,
        }

        # --- NEW ---
        self.history = []
        self.history_index = None  # None means not browsing history

    # ------------------------
    # --- INPUT PROCESSING ---
    # ------------------------
    def press(self, key):
        if key == "CLEAR":
            self.display = ""
            self.cursor_pos = 0
        elif key == "BACK":
            self.backspace()
        elif key == "ENTER":
            self.evaluate()
        elif key == "ANS":
            self.insert_text(str(self.last_answer))
        elif key == "+/-":
            self.toggle_sign()
        elif key == "RESET":
            self.display = ""
            self.last_answer = 0
            self.cursor_pos = 0
        elif key == "TOGGLE_SCI":
            self.scientific_mode = not self.scientific_mode
        elif key == "LEFT":
            self.move_cursor(-1)
        elif key == "RIGHT":
            self.move_cursor(1)
        elif key == "UP":
            self.prev_history()
        elif key == "DOWN":
            self.next_history()
        else:
            self.insert_text(key)

    # ------------------------
    # --- TEXT OPERATIONS ---
    # ------------------------
    def insert_text(self, text):
        """Insert text at cursor position."""
        self.display = self.display[:self.cursor_pos] + text + self.display[self.cursor_pos:]
        self.cursor_pos += len(text)

    def backspace(self):
        if self.cursor_pos > 0:
            self.display = self.display[:self.cursor_pos - 1] + self.display[self.cursor_pos:]
            self.cursor_pos -= 1

    def move_cursor(self, direction):
        """Move cursor left (-1) or right (+1)"""
        self.cursor_pos = max(0, min(len(self.display), self.cursor_pos + direction))

    # ------------------------
    # --- HISTORY HANDLING ---
    # ------------------------
    def prev_history(self):
        """Scroll up through previous inputs."""
        if not self.history:
            return
        if self.history_index is None:
            self.history_index = len(self.history) - 1
        elif self.history_index > 0:
            self.history_index -= 1
        self.display = self.history[self.history_index]
        self.cursor_pos = len(self.display)

    def next_history(self):
        """Scroll down through history."""
        if self.history_index is None:
            return
        elif self.history_index < len(self.history) - 1:
            self.history_index += 1
            self.display = self.history[self.history_index]
        else:
            self.history_index = None
            self.display = ""
        self.cursor_pos = len(self.display)

    # ------------------------
    # --- MATH OPERATIONS ---
    # ------------------------
    def toggle_sign(self):
        """Toggle the sign of the current or last entered number."""
        if not self.display:
            self.insert_text("-")
            return

        match = re.search(r"(-?\d+\.?\d*)$", self.display[:self.cursor_pos])
        if match:
            num_str = match.group(1)
            start = match.start()
            if num_str.startswith("-"):
                # remove negative
                self.display = self.display[:start] + num_str[1:] + self.display[self.cursor_pos:]
                self.cursor_pos -= 1
            else:
                # add negative
                self.display = self.display[:start] + "-" + num_str + self.display[self.cursor_pos:]
                self.cursor_pos += 1
        else:
            self.insert_text("-")

    def evaluate(self):
        expr = self.display.replace("^", "**")
        try:
            result = eval(expr, {"__builtins__": None}, self.env)
            self.last_answer = result
            self.history.append(self.display)
            self.history_index = None
            if self.scientific_mode and isinstance(result, (float, int)):
                self.display = f"{result:.6e}"
            else:
                self.display = str(result)
            self.cursor_pos = len(self.display)
        except Exception:
            self.display = "Error"
            self.cursor_pos = len(self.display)

    # ------------------------
    # --- DISPLAY HELPER ---
    # ------------------------
    def get_display(self):
        """Return display text with visible cursor marker."""
        # Insert a vertical bar to show cursor
        return self.display[:self.cursor_pos] + "|" + self.display[self.cursor_pos:]

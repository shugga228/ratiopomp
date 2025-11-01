import math
import re

class TextGraph:
    def __init__(self, width=60, height=20, x_min=-10, x_max=10):
        self.width = width
        self.height = height
        self.x_min = x_min
        self.x_max = x_max

    def safe_eval(self, expr, x):
        # Replace ^ with ** and implicit multiplications (e.g., 2x -> 2*x)
        expr = expr.replace("^", "**")
        expr = re.sub(r"(\d)([a-zA-Z(])", r"\1*\2", expr)
        expr = re.sub(r"([a-zA-Z)])(\d)", r"\1*\2", expr)

        # Safe math environment
        allowed = {k: getattr(math, k) for k in dir(math) if not k.startswith("_")}
        allowed["x"] = x

        try:
            return eval(expr, {"__builtins__": {}}, allowed)
        except Exception:
            return None

    def plot_function(self, func_str):
        print(f"\nPlotting f(x) = {func_str}")
        xs = [self.x_min + (i / (self.width - 1)) * (self.x_max - self.x_min) for i in range(self.width)]
        ys = [self.safe_eval(func_str, x) for x in xs]

        valid_ys = [y for y in ys if y is not None and math.isfinite(y)]
        if not valid_ys:
            print("No valid data points.")
            return

        y_min, y_max = min(valid_ys), max(valid_ys)
        if y_min == y_max:
            y_min -= 1
            y_max += 1

        grid = [[" " for _ in range(self.width)] for _ in range(self.height)]
        try:
            x_axis = int((0 - y_min) / (y_max - y_min) * (self.height - 1))
        except ZeroDivisionError:
            x_axis = self.height // 2
        y_axis = int((0 - self.x_min) / (self.x_max - self.x_min) * (self.width - 1))

        for x in range(self.width):
            if 0 <= x_axis < self.height:
                grid[x_axis][x] = "-"
        for y in range(self.height):
            if 0 <= y_axis < self.width:
                grid[y][y_axis] = "|"
        if 0 <= x_axis < self.height and 0 <= y_axis < self.width:
            grid[x_axis][y_axis] = "+"

        for i, y in enumerate(ys):
            if y is None:
                continue
            py = int((1 - (y - y_min) / (y_max - y_min)) * (self.height - 1))
            if 0 <= py < self.height:
                grid[py][i] = "*"

        for row in grid:
            print("".join(row))

    def run(self):
        print("\n=== GRAPHING MODE ===")
        print("Type a function of x (e.g. sin(x), 2x, x^2, exp(x))")
        print("Type 'home' to return to main menu.\n")

        while True:
            func_str = input("f(x) = ").strip()
            if func_str.lower() == "home":
                break
            elif func_str == "":
                continue
            else:
                self.plot_function(func_str)

import math

class TextGraph:
    def __init__(self, width=60, height=20, x_min=-10, x_max=10):
        self.width = width
        self.height = height
        self.x_min = x_min
        self.x_max = x_max
        self.y_min = -10
        self.y_max = 10

    def plot_function(self, func_str):
        """Plot f(x) = ... using ASCII graphics."""
        print(f"Plotting f(x) = {func_str}")
        func = None
        try:
            func = lambda x: eval(func_str, {"x": x, "math": math, "__builtins__": {}})
        except Exception as e:
            print("Error parsing function:", e)
            return

        # Create empty grid
        grid = [[" " for _ in range(self.width)] for _ in range(self.height)]

        # Axes positions
        x_axis = int((0 - self.y_min) / (self.y_max - self.y_min) * (self.height - 1))
        y_axis = int((0 - self.x_min) / (self.x_max - self.x_min) * (self.width - 1))

        # Draw axes
        for x in range(self.width):
            if 0 <= x_axis < self.height:
                grid[x_axis][x] = "-"
        for y in range(self.height):
            if 0 <= y_axis < self.width:
                grid[y][y_axis] = "|"
        if 0 <= x_axis < self.height and 0 <= y_axis < self.width:
            grid[x_axis][y_axis] = "+"

        # Compute and plot points
        for px in range(self.width):
            # Map screen x to graph x
            x = self.x_min + (px / (self.width - 1)) * (self.x_max - self.x_min)
            try:
                y = func(x)
                # Map y to screen y
                py = int((1 - (y - self.y_min) / (self.y_max - self.y_min)) * (self.height - 1))
                if 0 <= py < self.height:
                    grid[py][px] = "*"
            except Exception:
                continue

        # Print the grid
        for row in grid:
            print("".join(row))

    def run(self):
        print("\n=== GRAPHING MODE ===")
        print("Type a function of x (example: sin(x), x**2, exp(x), etc.)")
        print("Type 'home' to return to the main menu.\n")

        while True:
            func_str = input("f(x) = ").strip()
            if func_str.lower() == "home":
                break
            elif func_str == "":
                continue
            else:
                self.plot_function(func_str)

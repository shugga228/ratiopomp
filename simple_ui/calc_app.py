import math

class ScientificCalculator:
    def __init__(self):
        self.memory = 0
        self.last_answer = 0
        self.mode_deg = False
        self.alt_mode = False
        self.sci_notation = False
        self.running = True

    def run(self):
        print("\n=== SCIENTIFIC CALCULATOR ===")
        print("Type expressions directly (e.g. sin(pi/2) + 3)")
        print("Commands: alt | deg | sci | m+ | m- | mr | mc | ans | clr | home")

        while self.running:
            expr = input("> ").strip().lower()

            if not expr:
                continue

            if expr == "home":
                print("Returning home...")
                break
            elif expr == "clr":
                self.last_answer = 0
                print("Cleared.")
            elif expr == "alt":
                self.alt_mode = not self.alt_mode
                print("[ALT MODE]" if self.alt_mode else "[NORMAL MODE]")
            elif expr == "deg":
                self.mode_deg = not self.mode_deg
                print("[DEG MODE]" if self.mode_deg else "[RAD MODE]")
            elif expr == "sci":
                self.sci_notation = not self.sci_notation
                print("[SCIENTIFIC ON]" if self.sci_notation else "[NORMAL NOTATION]")
            elif expr == "m+":
                self.memory += self.last_answer
                print(f"Memory = {self.memory}")
            elif expr == "m-":
                self.memory -= self.last_answer
                print(f"Memory = {self.memory}")
            elif expr == "mr":
                print(f"Recalled memory: {self.memory}")
                expr = str(self.memory)
            elif expr == "mc":
                self.memory = 0
                print("Memory cleared.")
                continue
            else:
                expr = expr.replace("^", "**")
                expr = expr.replace("ans", str(self.last_answer))
                expr = expr.replace("π", "math.pi").replace("pi", "math.pi")
                expr = expr.replace("e", "math.e")

                # ALT trig/log
                if self.alt_mode:
                    expr = expr.replace("sin", "math.asin")
                    expr = expr.replace("cos", "math.acos")
                    expr = expr.replace("tan", "math.atan")
                    expr = expr.replace("log", "math.log10")
                else:
                    expr = expr.replace("sin", "math.sin")
                    expr = expr.replace("cos", "math.cos")
                    expr = expr.replace("tan", "math.tan")
                    expr = expr.replace("log", "math.log10")

                # Always allow these
                expr = expr.replace("ln", "math.log")
                expr = expr.replace("sqrt", "math.sqrt")
                expr = expr.replace("abs", "abs")
                expr = expr.replace("exp", "math.exp")
                expr = expr.replace("fact", "math.factorial")

                try:
                    result = eval(expr, {"math": math, "__builtins__": {}})
                    if self.mode_deg and not self.alt_mode:
                        # Convert trig inputs to radians in deg mode
                        result = math.degrees(result) if "asin" in expr or "acos" in expr or "atan" in expr else result
                    if self.sci_notation:
                        print(f"= {result:.6e}")
                    else:
                        print(f"= {result}")
                    self.last_answer = result
                except Exception as e:
                    print("Error:", e)

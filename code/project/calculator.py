import tkinter
import math

button_values = [
    ["AC", "+/-", "%", "÷"],
    ["7", "8", "9", "×"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "√", "="]
]

right_symbols = ["÷", "×", "-", "+", "="]
top_symbols = ["AC", "+/-", "%"]

row_count = len(button_values)
column_count = len(button_values[0])

# Colors
column_light_gray = "#D4D4D2"
column_black = "#1C1C1C"
column_dark_gray = "#505050"
column_orange = "#FF9500"
column_white = "white"

# -----------------------------
# Calculator Variables
# -----------------------------
current_input = "0"

# -----------------------------
# Window
# -----------------------------
window = tkinter.Tk()
window.title("Calculator")
window.resizable(False, False)

frame = tkinter.Frame(window, bg=column_black)

label = tkinter.Label(
    frame,
    text=current_input,
    font=("Arial", 40),
    bg=column_black,
    fg=column_white,
    width=15,
    anchor="e",
    padx=10,
    pady=20,
)

label.grid(row=0, column=0, columnspan=column_count, sticky="we")


# -----------------------------
# Update Display
# -----------------------------
def update_display():
    label.config(text=current_input)


# -----------------------------
# Button Function
# -----------------------------
def button_clicked(value):
    global current_input

    if value == "AC":
        current_input = "0"

    elif value == "+/-":
        try:
            current_input = str(-float(current_input))
            if current_input.endswith(".0"):
                current_input = current_input[:-2]
        except:
            current_input = "Error"

    elif value == "%":
        try:
            current_input = str(float(current_input) / 100)
        except:
            current_input = "Error"

    elif value == "√":
        try:
            number = float(current_input)
            if number < 0:
                current_input = "Error"
            else:
                current_input = str(math.sqrt(number))
        except:
            current_input = "Error"

    elif value == "=":
        try:
            expression = (
                current_input.replace("×", "*")
                .replace("÷", "/")
            )
            result = eval(expression)
            current_input = str(result)

            if current_input.endswith(".0"):
                current_input = current_input[:-2]

        except:
            current_input = "Error"

    elif value in ["+", "-", "×", "÷"]:

        if current_input[-1] in "+-×÷":
            current_input = current_input[:-1] + value
        else:
            current_input += value

    elif value == ".":

        last_number = ""

        for ch in reversed(current_input):
            if ch in "+-×÷":
                break
            last_number = ch + last_number

        if "." not in last_number:
            current_input += "."

    else:
        if current_input == "0" or current_input == "Error":
            current_input = value
        else:
            current_input += value

    update_display()


# -----------------------------
# Buttons
# -----------------------------
for row in range(row_count):
    for column in range(column_count):

        value = button_values[row][column]

        if value in top_symbols:
            bg_color = column_light_gray
            fg_color = "black"

        elif value in right_symbols:
            bg_color = column_orange
            fg_color = "white"

        else:
            bg_color = column_dark_gray
            fg_color = "white"

        button = tkinter.Button(
            frame,
            text=value,
            font=("Arial", 20),
            width=4,
            height=2,
            bg=bg_color,
            fg=fg_color,
            bd=0,
            command=lambda value=value: button_clicked(value),
        )

        button.grid(row=row + 1, column=column, padx=2, pady=2)

frame.pack()
window.mainloop()
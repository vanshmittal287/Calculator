import tkinter

button_values = [
    ["AC","+/-","%","÷"],
    ["7","8","9","×"],
    ["4","5","6","+"],
    ["1","2","3","-"],
    ["0",".","√","="]
]

button_right = ["÷", "×", "+", "-", "="]
button_top = ["AC", "+/-", "%",]

light_gray = "#D4D4D2"
black="#1C1C1C"
dark_gray = "#505050"
orange="#FF9500"
white = "white"

number_row = len(button_values)
number_col = len(button_values[0])

window = tkinter.Tk()
window.title("Calculator")
window.resizable(False, False)
FRAME = tkinter.Frame(window,)
FRAME.pack()
LABEL = tkinter.Label(FRAME, text="0", bg=black, fg=white, font=("Arial", 45), anchor = "e", width=number_col)
LABEL.grid(row=0, column=0, columnspan=number_col,sticky="we")

for row in range(number_row):
    for col in range(number_col):
        value = button_values[row][col]
        button = tkinter.Button(FRAME, text=value, font=("Arial", 30), width=3, height=1,
        command = lambda value=value: button_click(value))
        button.grid(row=row+1, column=col)

        if value in button_top:
            button.config(bg=light_gray,fg=black)
        elif value in button_right:
            button.config(bg=orange,fg=white)
        else:
            button.config(bg=dark_gray,fg=white)
A = "0"
operator = None
B = None

def clear():
    global A, B, operator
    A = "0"
    B = None
    operator = None
   

def zero_decimal(num):
    if num%1 == 0:
        num = int(num)
    return str(round(num, 7))
    
def button_click(value): 
    global button_right, LABEL , A, B, operator
    if value in button_right:
        if value == "=":
            if A!=None and operator!=None:
                B = LABEL["text"]
                num1 = float(A)
                num2 = float(B)
                if operator == "+":
                    LABEL["text"] = zero_decimal(num1 + num2)
                elif operator == "-":
                    LABEL["text"] = zero_decimal(num1 - num2)
                elif operator == "×":
                    LABEL["text"] = zero_decimal(num1 * num2)
                elif operator == "÷":
                    if num2 == 0:
                        LABEL["text"] = "Error"
                    else:
                        LABEL["text"] = zero_decimal(num1 / num2)

                clear()
        elif value in "+-×÷":
            if operator is None:
                A = LABEL["text"]
                LABEL["text"] = "0"
                B = "0"
            operator = value

    elif value in button_top:
        if value == "AC":
            clear()
            LABEL["text"] = "0"

        elif value == "+/-":
            result = float(LABEL["text"]) * -1
            LABEL["text"] = zero_decimal(result)
        else:
            if LABEL["text"] == "0":
                pass
            else:
             result = float(LABEL["text"]) / 100
             LABEL["text"] = zero_decimal(result)
    elif value == ".": 
            if value not in LABEL["text"]:
                LABEL["text"] += value
            else:
                pass
    elif value in "0123456789":
            if LABEL["text"] == "0":
                LABEL["text"] = value
            else:
             LABEL["text"] += value
    elif value == "√":
        if float(LABEL["text"]) < 0:
            LABEL["text"] = "Error"
        else:
         result = float(LABEL["text"]) ** 0.5
         LABEL["text"] = zero_decimal(result)
         

def keyboard_press(event):
    key = event.char

    if key and key in "0123456789.":
        button_click(key)

    elif key == "+":
        button_click("+")

    elif key == "-":
        button_click("-")

    elif key == "*":
        button_click("×")

    elif key == "/":
        button_click("÷")

    elif key == "%":
        button_click("%")

    elif key == "\r":  # Enter
        button_click("=")

    elif event.keysym == "BackSpace":
     if LABEL["text"] != "Error":
        text = LABEL["text"][:-1]
        LABEL["text"] = text if text and text != "-" else "0"

    elif event.keysym == "Escape":
        button_click("AC")

window.bind_all("<Key>", keyboard_press)

window.mainloop()
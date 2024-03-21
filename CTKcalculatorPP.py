import customtkinter as ctk
import re

ctk.set_appearance_mode("system")

#create window
app = ctk.CTk()
app.title("Calculator")
app.geometry("400x250")

#create label
text = ""
label = ctk.CTkLabel(app, text = "", font = ("Arial", 50))
label.grid(row= 0, column = 0, rowspan = 1, columnspan = 3)

#commands for each button
def btn1_command():
    label.configure(text = "")

def btn2_command():
    current_text = label.cget("text")
    txt = current_text + "^"
    label.configure(text = txt)

def btn3_command():
    current_text = label.cget("text")
    txt = current_text + "%"
    label.configure(text = txt)

def btn4_command():
    current_text = label.cget("text")
    txt = current_text + "/"
    label.configure(text = txt)

def btn5_command():
    current_text = label.cget("text")
    txt = current_text + "7"
    label.configure(text = txt)

def btn6_command():
    current_text = label.cget("text")
    txt = current_text + "8"
    label.configure(text = txt)

def btn7_command():
    current_text = label.cget("text")
    txt = current_text + "9"
    label.configure(text = txt)

def btn8_command():
    current_text = label.cget("text")
    txt = current_text + "x"
    label.configure(text = txt)

def btn9_command():
    current_text = label.cget("text")
    txt = current_text + "4"
    label.configure(text = txt)

def btn10_command():
    current_text = label.cget("text")
    txt = current_text + "5"
    label.configure(text = txt)

def btn11_command():
    current_text = label.cget("text")
    txt = current_text + "6"
    label.configure(text = txt)

def btn12_command():
    current_text = label.cget("text")
    txt = current_text + "-"
    label.configure(text = txt)

def btn13_command():
    current_text = label.cget("text")

    txt = current_text + "1"
    label.configure(text = txt)

def btn14_command():
    current_text = label.cget("text")
    txt = current_text + "2"
    label.configure(text = txt)

def btn15_command():
    current_text = label.cget("text")
    txt = current_text + "3"
    label.configure(text = txt)

def btn16_command():
    current_text = label.cget("text")
    txt = current_text + "+"
    label.configure(text = txt)

def btn17_command():
    current_text = label.cget("text")
    txt = current_text + "0"
    label.configure(text = txt)

def btn19_command():
    current_text = label.cget("text")
    txt = current_text + "."
    label.configure(text = txt)

def btn20_command():
    #display result
    #[[num1], symbol, [num2]]

    current_str = label.cget("text")

    lst = re.split(r'(\+|-|x|/|\^|%)', current_str)
    lst = [elem for elem in lst if elem.strip()]

    a = lst[0]
    b = lst[2]
    opperator = lst[1]

    def calculate(num1, num2, opp):
        if opp == "+":
            result = float(num1) + float(num2)
            return str(result)
        
        elif opp == "-":
            result = float(num1) - float(num2)
            return str(result)
        
        elif opp == "x":
            result = float(num1) * float(num2)
            return str(result)
        
        elif opp == "/":
            if num2 == 0:
                return "Error"
            else:
                result = float(num1) / float(num2)
                return str(result)
        
        elif opp == "^":
            result = float(num1) ** float(num2)
            return str(result)
        
        elif opp == "%":
            if num2 == 0:
                return "Error"
            else:
                result = float(num1) % float(num2)
                return str(result)
        

    label.configure(text = calculate(a, b, opperator)) #updates the label with the result from the calculation function


#create 4x5 grid
app.grid_columnconfigure(0, weight=1)
app.grid_columnconfigure(1, weight=1)
app.grid_columnconfigure(2, weight=1)
app.grid_columnconfigure(3, weight=1)


btn1 = ctk.CTkButton(app, text = "Clear", command = btn1_command)
btn1.grid(row=1, column = 0, padx=5, pady=5, sticky = "ew")

btn2 = ctk.CTkButton(app, text = "^", command = btn2_command)
btn2.grid(row=1, column = 1, padx=5, pady=5, sticky = "ew")

btn3 = ctk.CTkButton(app, text = "%", command = btn3_command)
btn3.grid(row=1, column = 2, padx=5, pady=5, sticky = "ew")

btn4 = ctk.CTkButton(app, text = "/", command = btn4_command)
btn4.grid(row=1, column = 3, padx=5, pady=5, sticky = "ew")

btn5 = ctk.CTkButton(app, text = "7", command = btn5_command)
btn5.grid(row=2, column = 0, padx=5, pady=5, sticky = "ew")

btn6 = ctk.CTkButton(app, text = "8", command = btn6_command)
btn6.grid(row=2, column = 1, padx=5, pady=5, sticky = "ew")

btn7 = ctk.CTkButton(app, text = "9", command = btn7_command)
btn7.grid(row=2, column = 2, padx=5, pady=5, sticky = "ew")

btn8 = ctk.CTkButton(app, text = "x", command = btn8_command)
btn8.grid(row=2, column = 3, padx=5, pady=5, sticky = "ew")

btn9 = ctk.CTkButton(app, text = "4", command = btn9_command)
btn9.grid(row=3, column = 0, padx=5, pady=5, sticky = "ew")

btn10 = ctk.CTkButton(app, text = "5", command = btn10_command)
btn10.grid(row=3, column = 1, padx=5, pady=5, sticky = "ew")

btn11 = ctk.CTkButton(app, text = "6", command = btn11_command)
btn11.grid(row=3, column = 2, padx=5, pady=5, sticky = "ew")

btn12 = ctk.CTkButton(app, text = "-", command = btn12_command)
btn12.grid(row=3, column = 3, padx=5, pady=5, sticky = "ew")

btn13 = ctk.CTkButton(app, text = "1", command = btn13_command)
btn13.grid(row=4, column = 0, padx=5, pady=5, sticky = "ew")

btn14 = ctk.CTkButton(app, text = "2", command = btn14_command)
btn14.grid(row=4, column = 1, padx=5, pady=5, sticky = "ew")

btn15 = ctk.CTkButton(app, text = "3", command = btn15_command)
btn15.grid(row=4, column = 2, padx=5, pady=5, sticky = "ew")

btn16 = ctk.CTkButton(app, text = "+", command = btn16_command)
btn16.grid(row=4, column = 3, padx=5, pady=5, sticky = "ew")

btn17 = ctk.CTkButton(app, text = "0", command = btn17_command)
btn17.grid(row=5, column = 0, columnspan = 2, padx=5, pady=5, sticky = "ew")

btn19 = ctk.CTkButton(app, text = ".", command = btn19_command)
btn19.grid(row=5, column = 2, padx=5, pady=5, sticky = "ew")

btn20 = ctk.CTkButton(app, text = "=", command = btn20_command)
btn20.grid(row=5, column = 3, padx=5, pady=5, sticky = "ew")



app.mainloop()
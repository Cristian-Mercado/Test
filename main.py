import tkinter as tk

root = tk.Tk()

root.geometry("900x600")
root.title("Home page")

label = tk.Label(root, text='How can I help you?', font =('Arial', 20))
label.pack(padx=10, pady=10)

buttonframe = tk.Frame(root)
buttonframe.pack(expand=True, fill="both", padx=10,pady=10)

for i in range(5):
  buttonframe.rowconfigure(i, weight=1)
for j in range(5):
  buttonframe.columnconfigure(j, weight=1)

btn1 = tk.Button(buttonframe, text = "Academic Programs", font = ("Arial", 18))
btn1.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

btn2 = tk.Button(buttonframe, text = "Academic Calendar", font = ("Arial", 18))
btn2.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

btn3 = tk.Button(buttonframe, text = "Locations", font = ("Arial", 18))
btn3.grid(row=0, column=2, sticky="nsew", padx=10, pady=10)

btn4 = tk.Button(buttonframe, text = "General UNTD Info", font = ("Arial", 18))
btn4.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)

btn5 = tk.Button(buttonframe, text = "Events", font = ("Arial", 18))
btn5.grid(row=1, column=1, sticky="nsew", padx=10, pady=10)


buttonframe.pack(fill="x")

root.mainloop()
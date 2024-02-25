import tkinter as tk

def decimal_to_binary(n):
    return bin(n)[2:]

def display_lights(result):
    if result < 0:
        error_label = tk.Label(lights_frame, text="Отрицательные числа не поддерживаются!", fg="red")
        error_label.pack()
    else:
        binary_result = decimal_to_binary(result)

        for widget in lights_frame.winfo_children():
            widget.destroy()

        row_frame = tk.Frame(lights_frame)
        row_frame.pack()

        for index, bit in enumerate(binary_result):
            if index % 12 == 0:
                row_frame = tk.Frame(lights_frame)
                row_frame.pack()

            if bit == '1':
                light_color = "yellow"  # Лампочка включена
            else:
                light_color = "gray"  # Лампочка выключена

            light_label = tk.Label(row_frame, bg=light_color, width=2, height=1, padx=5, pady=5, relief="ridge")
            light_label.pack(side=tk.LEFT, anchor=tk.W)

        result_label.config(text=f"Результат: {result}\nРезультат в двоичной системе: {binary_result}")

def add():
    num1 = int(entry1.get())
    num2 = int(entry2.get())
    res = num1 + num2
    display_lights(res)

root = tk.Tk()
root.title("Сложение двоичных чисел")
root.geometry("400x300")

label1 = tk.Label(root, text="Первое число:")
label1.pack()
entry1 = tk.Entry(root)
entry1.pack()

label2 = tk.Label(root, text="Второе число:")
label2.pack()
entry2 = tk.Entry(root)
entry2.pack()

add_button = tk.Button(root, text="Сложить", command=add)
add_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

lights_frame = tk.Frame(root)
lights_frame.pack()

root.mainloop()


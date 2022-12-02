from tkinter import *
from tkinter import messagebox


def calculate_bmi():
    kg = int(weight_tf.get())
    m = int(height_tf.get()) / 100
    bmi = kg / (m * m)
    bmi = round(bmi, 1)

    if bmi < 18.5:
        messagebox.showinfo('ИМТ', f'ИМТ = {bmi} соответствует недостаточному весу')
    elif (bmi > 18.5) and (bmi < 24.9):
        messagebox.showinfo('ИМТ', f'ИМТ = {bmi} соответствует нормальному весу')
    elif (bmi > 24.9) and (bmi < 29.9):
        messagebox.showinfo('ИМТ', f'ИМТ = {bmi} соответствует избыточному весу')
    elif (bmi > 29.9) and (bmi < 34.9):
        messagebox.showinfo('ИМТ', f'ИМТ = {bmi} соответствует ожирению 1-й степени')
    elif (bmi > 34.9) and (bmi < 39.9):
        messagebox.showinfo('ИМТ', f'ИМТ = {bmi} соответствует ожирению 2-й степени')
    else:
        messagebox.showinfo('ИМТ', f'ИМТ = {bmi} соответствует ожирению 3-й степени')
def clear():
    height_tf.delete("0", "end")
    weight_tf.delete("0", "end")

window = Tk()
window.title('Калькулятор индекса массы тела (ИМТ)')
window.geometry('700x300')
window["bg"] = "pink"

frame = Frame(window, bg="pink")
frame.pack(expand=True)

name = Label(frame, text="Рассчитать индекс массы тела", bg="pink", fg="black", width=27, font=('helvetica', 15, 'bold'))
name.grid(row=0, column=2)

height_lb = Label(frame, text="Введите свой рост (в см)", bg="pink", fg="black", font=6)
height_lb.grid(row=2, column=1)

weight_lb = Label(frame, text="Введите свой вес (в кг)", bg="pink", fg="black", font=6)
weight_lb.grid(row=3, column=1)

height_tf = Entry(frame, width=28, font=6, bg="white", bd=5)
height_tf.grid(row=2, column=2, pady=5, padx=5)

weight_tf = Entry(frame, width=28, font=6, bg="white", bd=5)
weight_tf.grid(row=3, column=2, pady=5, padx=5)

cal_btn = Button(frame, text='Рассчитать ИМТ', bg="white", command=calculate_bmi, bd=5, width=15, font=6)
cal_btn.grid(row=2, column=3, pady=5)
clear_btn = Button(frame, fg="black", text="Очистить", bg="white", command=clear, bd=5,  width=15, font=6)
clear_btn.grid(row=3, column=3)

window.mainloop()

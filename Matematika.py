# pip install tk

import turtle
a = float (input ('Upišite duljinu veće katete A: '))
b = float (input ('Upišite duljinu manje katete B: '))
c = float (input ('Upišite duljinu hipotenuze C: '))
x = int (input ("Upišite '0' za Kalkulator ili '1' za Konstukciju: "))
#---------------------------------------------------------------
if x == 1:
    print ("Upišite 'START' za početak'")
    trokut = turtle.Turtle()
    trokut.forward (200)
    trokut.backward (200)
    trokut.left(90)
    trokut.forward(250)
    trokut.backward(125)
    trokut.left(90)
    trokut.penup()
    trokut.forward(50)
    trokut.write(a, font=('Calibri',25,'normal'))
    trokut.backward(50)
    trokut.left(90)
    trokut.forward(125)
    trokut.left(90)
    trokut.forward(100)
    trokut.right(90)
    trokut.forward(50)
    trokut.write(b, font=('Calibri',25,'normal'))
    trokut.backward(50)
    trokut.left(90)
    trokut.forward(100)
    trokut.pendown()
    trokut.left(129)
    trokut.forward(320)
    trokut.backward(160)
    trokut.penup()
    trokut.right(90)
    trokut.forward(50)
    trokut.write(c, font=('Calibri',25,'normal'))

#---------------------------------------------------------------

if x == 0:
    from tkinter import *
    import math
    expression = ""
     
     
    def press(num):

        global expression
     

        expression = expression + str(num)
     

        equation.set(expression)
     
     

    def equalpress():

        try:
     
            global expression
     

            total = str(eval(expression))
     
            equation.set(total)
     

            expression = ""
     

        except:
     
            equation.set(" error ")
            expression = ""
     
    def sin():
        global expression
        expression = float(expression)
        expression = round(math.sin(math.radians(expression)), 5)
        equation.set(float(expression))
        expression = str(expression)


    def cos():
        global expression
        expression = float(expression)
        expression = round(math.cos(math.radians(expression)), 5)
        equation.set(float(expression))
        expression = str(expression)


    def tan():
        global expression
        expression = float(expression)
        expression = round(math.tan(math.radians(expression)), 5)
        equation.set(float(expression))
        expression = str(expression)
     
    def clear():
        global expression
        expression = ""
        equation.set("")
     
     

    if __name__ == "__main__":

        gui = Tk()
     

        gui.configure(background="blue")
     

        gui.title("Simple Calculator")
     

        gui.geometry("265x175")
     

        equation = StringVar()
     

        expression_field = Entry(gui, textvariable=equation)
     

        expression_field.grid(columnspan=4, ipadx=70)

        button1 = Button(gui, text=' 1 ', fg='black', bg='red',
                        command=lambda: press(1), height=1, width=7)
        button1.grid(row=2, column=0)
     
        button2 = Button(gui, text=' 2 ', fg='black', bg='red',
                        command=lambda: press(2), height=1, width=7)
        button2.grid(row=2, column=1)
     
        button3 = Button(gui, text=' 3 ', fg='black', bg='red',
                        command=lambda: press(3), height=1, width=7)
        button3.grid(row=2, column=2)
     
        button4 = Button(gui, text=' 4 ', fg='black', bg='red',
                        command=lambda: press(4), height=1, width=7)
        button4.grid(row=3, column=0)
     
        button5 = Button(gui, text=' 5 ', fg='black', bg='red',
                        command=lambda: press(5), height=1, width=7)
        button5.grid(row=3, column=1)
     
        button6 = Button(gui, text=' 6 ', fg='black', bg='red',
                        command=lambda: press(6), height=1, width=7)
        button6.grid(row=3, column=2)
     
        button7 = Button(gui, text=' 7 ', fg='black', bg='red',
                        command=lambda: press(7), height=1, width=7)
        button7.grid(row=4, column=0)
     
        button8 = Button(gui, text=' 8 ', fg='black', bg='red',
                        command=lambda: press(8), height=1, width=7)
        button8.grid(row=4, column=1)
     
        button9 = Button(gui, text=' 9 ', fg='black', bg='red',
                        command=lambda: press(9), height=1, width=7)
        button9.grid(row=4, column=2)
     
        button0 = Button(gui, text=' 0 ', fg='black', bg='red',
                        command=lambda: press(0), height=1, width=7)
        button0.grid(row=5, column=1)

        buttonA = Button(gui, text=' A ', fg='black', bg='light green',
                        command=lambda: press(a), height=1, width=7)
        buttonA.grid(row=6, column=0)

        buttonB = Button(gui, text=' B ', fg='black', bg='light green',
                        command=lambda: press(b), height=1, width=7)
        buttonB.grid(row=6, column=1)

        buttonC = Button(gui, text=' C ', fg='black', bg='light green',
                        command=lambda: press(c), height=1, width=7)
        buttonC.grid(row=6, column=2)
     
        plus = Button(gui, text=' + ', fg='black', bg='red',
                    command=lambda: press("+"), height=1, width=7)
        plus.grid(row=2, column=3)
     
        minus = Button(gui, text=' - ', fg='black', bg='red',
                    command=lambda: press("-"), height=1, width=7)
        minus.grid(row=3, column=3)
     
        multiply = Button(gui, text=' * ', fg='black', bg='red',
                        command=lambda: press("*"), height=1, width=7)
        multiply.grid(row=4, column=3)
     
        divide = Button(gui, text=' / ', fg='black', bg='red',
                        command=lambda: press("/"), height=1, width=7)
        divide.grid(row=5, column=3)
     
        equal = Button(gui, text=' = ', fg='black', bg='red',
                    command=equalpress, height=1, width=7)
        equal.grid(row=6, column=3)
     
        clear = Button(gui, text='Clear', fg='black', bg='red',
                    command=clear, height=1, width=7)
        clear.grid(row=5, column='2')
     
        Decimal= Button(gui, text='.', fg='black', bg='red',
                        command=lambda: press('.'), height=1, width=7)
        Decimal.grid(row=5, column=0)

        sin = Button(gui, text='SIN', fg='black', bg='light green',
        command=sin, height=1, width=7)
        sin.grid(row=7, column=0)

        cos = Button(gui, text='COS', fg='black', bg='light green',
        command=cos, height=1, width=7)
        cos.grid(row=7, column=1)

        tan = Button(gui, text='TAN', fg='black', bg='light green',
        command=tan, height=1, width=7)
        tan.grid(row=7, column=2)



        buttonupitnik = Button(gui, text='?', fg='black', bg='light green',
                command=lambda: press('Za Trigonometriju - Prvo broj, pa onda radnju'), height=1, width=7)
        buttonupitnik.grid(row=7, column=3)

        gui.mainloop()

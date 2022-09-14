import turtle as f 

colors = ['indigo', 'dark violet', 'purple',
          'magenta', 'violet', 'pink']

p = f.Pen()

f.bgcolor('black')

def FibonacciSpiral():
    for i in range(360):
        p.pencolor(colors[i%6])
        p.width(i//100+1)
        p.forward(i)
        p.left(59)

FibonacciSpiral()
f.mainloop()


#Run Command: python FibonacciSpiral.py

import turtle as f 

colors = ['magenta', 'pink']

p = f.Pen()
f.bgcolor('black')
def flower():
    for i in range(360):
        p.pencolor(colors[i%2])
        p.circle(190-i,90)
        p.left(90)
        p.circle(190-i,90)
        p.left(18)

flower()
f.mainloop()


#Run Command: python SymmetryFlower.py

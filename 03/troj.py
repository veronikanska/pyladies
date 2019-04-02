from turtle import forward, left, exitonclick, bgcolor, pencolor, pensize, speed, hideturtle

# Nejprve zadani poctu stran - nepusti dal, pokud uzivatel nezada velikost v tomto rozmezi
n = 0             
while n < 2 or n > 8:
    n = int(input('Zadej pocet stran spiraly (2-8): '))     

# Pocatecni nastaveni vzhledu
hideturtle()
speed(0)
bgcolor('black')
colors = ('red', 'yellow', 'orange', 'green', 'blue', 'violet', 'pink', 'white')

for strana in range(int(200/n),int(1000/n + 100)):         # v range je korekce velikosti spiraly: Cim vetsi n, tim mensi pocatecni delka strany a mensi pocet 'otoceni'
    pencolor(colors[strana%n])                             # barva stopy se meni s kazdou novou stranou / vybira y mnoyiny barvy definovane vyse
    if strana > 100:                                       # tloustka stopy roste s delkou strany
        pensize(2)
    elif strana > 150:
        pensize(3)    
    elif strana > 200:
        pensize(4)
    forward(strana)
    left(360 / n + 1)

exitonclick()
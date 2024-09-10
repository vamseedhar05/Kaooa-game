import turtle as t
from turtle import Screen
from shapely.geometry import LineString
import time

def find_intersection(line1, line2):
    line1 = LineString([(line1[0], line1[1]), (line1[2], line1[3])])
    line2 = LineString([(line2[0], line2[1]), (line2[2], line2[3])])
    
    intersection = line1.intersection(line2)
    
    if intersection.is_empty:
        return None
    else:
        return intersection

def draw_star(star):
    star.penup()
    star.goto(-250, 0)
    lines = {}
    line = []
    line.extend(star.position())
    star.pendown()
    star.forward(500)
    line.extend(star.position())

    lines[0] = line
    for r in range(1, 5):
        line = []
        line.extend(star.position())
        star.rt(144)
        star.forward(500)
        line.extend(star.position())
        lines[r] = line
        
    return lines

def draw_circle(xco, yco, circle_turtle):
    circle_turtle.penup()
    circle_turtle.goto(xco, yco)
    circle_turtle.dot(60, "white")    

turn=0
crow_count=0
vulture_count=0
kills_count=0

class Circle :
    def __init__(self,xco,yco):
        self.x=xco
        self.y=yco
        self.color="white"
        self.neighbours=[]
        self.nxt_neighbours=[]

def fill_color(circle_turtle, inst, color):
    global turn,crow_count,vulture_count,kills_count
    circle_turtle.penup()       
    circle_turtle.goto(inst.x , inst.y)
    circle_turtle.pd()
    
    if inst.color == "white" : 
        if color=="yellow":
            turn+=1
            crow_count+=1
        elif color=="red":
            turn+=1
            vulture_count+=1 
    if color == "white" : 
        if inst.color=="yellow":
            kills_count+=1
    
    inst.color = color
    circle_turtle.dot(60, color)

def win_condition(winner,turtle,star):
    text = winner + " won the Game !"
    turtle.clear()
    star.clear()
    font = ("Arial", 25, "normal")
    x, y = -250, 0
    for letter in text:
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.write(letter, font=font)
        x += 20

    time.sleep(3)
    turtle.screen.bye()
    
    
    
def crows_move(x, y, circle_turtle, circles):
    global turn,crow_count,vulture_count
    if crow_count <= 7 :
        for inst in circles:
            if inst.color == "white":
                if ((x - inst.x)**2 + (y - inst.y)**2) ** 0.5 <= 60:
                    fill_color(circle_turtle,inst,"yellow")
                    break              
        if crow_count == 7 :
            crow_count = 100
    else:
        for inst in circles:
            if ((x - inst.x)**2 + (y - inst.y)**2) ** 0.5 <= 60:
                    found = inst
                    break
        if found.color=="yellow":
            flag = True
            while flag :
                flag=circle_turtle.screen.onclick(lambda x, y, turtle=circle_turtle, circles=circles, prev_click=found: crow_move_2(x, y, circle_turtle, circles, prev_click))
                    

def crow_move_2(x, y, circle_turtle, circles, prev_click):
    for i in range(len(circles)):
        if ((x - circles[i].x) ** 2 + (y - circles[i].y) ** 2) ** 0.5 <= 60:
            index = i
            break
        
    for neighbour in prev_click.neighbours:
        if index == neighbour["neigh"] and circles[index].color == "white":
                fill_color(circle_turtle, circles[neighbour["neigh"]], "yellow")
                fill_color(circle_turtle, prev_click, "white")
                circle_turtle.screen.onclick(lambda x, y, turtle=circle_turtle, star=star, circles=circles: click_function(x, y, circle_turtle, star, circles))
                return False
    return True
        


def check_for_kill(found):
    kill_options=[]
    for neighbour in found.neighbours:
        if circles[neighbour["neigh"]].color == "yellow" and neighbour["nxt_neigh"] != -1 and circles[neighbour["nxt_neigh"]].color == "white":
            kill_options.append(neighbour)
    return kill_options


def vulture_move(x, y, circle_turtle, circles, star):
    global turn, crow_count, vulture_count
    if vulture_count <= 1:
        for inst in circles:
            if inst.color == "white":
                if ((x - inst.x) ** 2 + (y - inst.y) ** 2) ** 0.5 <= 60:
                    fill_color(circle_turtle, inst, "red")
                    break
        if vulture_count == 1:
            vulture_count = 100
    else:
        for inst in circles:
            if inst.color == "red":
                found = inst
                break
        valid_set=check_for_kill(found)
        for i in range(len(circles)):
            if ((x - circles[i].x) ** 2 + (y - circles[i].y) ** 2) ** 0.5 <= 60:
                index = i
                break
        if len(valid_set) > 0:
            for neighbour in valid_set:
                if index == neighbour["nxt_neigh"] :
                    fill_color(circle_turtle, found, "white")
                    fill_color(circle_turtle, circles[neighbour["nxt_neigh"]], "red")
                    fill_color(circle_turtle, circles[neighbour["neigh"]], "white")
                    break
        else :
            if circles[index].color == "white":
                for neighbour in found.neighbours:
                    if index == neighbour["neigh"]:
                        fill_color(circle_turtle, found, "white")
                        fill_color(circle_turtle, circles[neighbour["neigh"]], "red")
            else:
                flag=0
                for neighbour in found.neighbours:
                    if circles[neighbour["neigh"]].color == "white":
                        flag=1
                if flag==0:
                    win_condition("Crow",circle_turtle,star)
            


def click_function(x, y, circle_turtle, star, circles):
    global turn,crow_count,vulture_count,kills_count
    if turn%2==0:
        if kills_count >= 4:
            win_condition("Vulture",circle_turtle,star)
        else:
            crows_move(x,y,circle_turtle, circles)
    else :
        vulture_move(x,y,circle_turtle, circles,star)
    

def assign_neighbours(circles):
    circles[0].neighbours.extend([
        {"neigh": 5, "nxt_neigh": 8},
        {"neigh": 7, "nxt_neigh": 9}
    ])
    circles[1].neighbours.extend([
        {"neigh": 8, "nxt_neigh": 5},
        {"neigh": 6, "nxt_neigh": 9}
    ])
    circles[2].neighbours.extend([
        {"neigh": 7, "nxt_neigh": 5},
        {"neigh": 9, "nxt_neigh": 6}
    ])
    circles[3].neighbours.extend([
        {"neigh": 5, "nxt_neigh": 7},
        {"neigh": 8, "nxt_neigh": 6}
    ])
    circles[4].neighbours.extend([
        {"neigh": 6, "nxt_neigh": 8},
        {"neigh": 9, "nxt_neigh": 7}
    ])
    circles[5].neighbours.extend([
        {"neigh": 0, "nxt_neigh": -1},
        {"neigh": 3, "nxt_neigh": -1},
        {"neigh": 7, "nxt_neigh": 2},
        {"neigh": 8, "nxt_neigh": 1}
    ])
    circles[6].neighbours.extend([
        {"neigh": 1, "nxt_neigh": -1},
        {"neigh": 4, "nxt_neigh": -1},
        {"neigh": 8, "nxt_neigh": 3},
        {"neigh": 9, "nxt_neigh": 2}
    ])
    circles[7].neighbours.extend([
        {"neigh": 0, "nxt_neigh": -1},
        {"neigh": 2, "nxt_neigh": -1},
        {"neigh": 5, "nxt_neigh": 3},
        {"neigh": 9, "nxt_neigh": 4}
    ])
    circles[8].neighbours.extend([
        {"neigh": 1, "nxt_neigh": -1},
        {"neigh": 3, "nxt_neigh": -1},
        {"neigh": 5, "nxt_neigh": 0},
        {"neigh": 6, "nxt_neigh": 4}
    ])
    circles[9].neighbours.extend([
        {"neigh": 2, "nxt_neigh": -1},
        {"neigh": 4, "nxt_neigh": -1},
        {"neigh": 6, "nxt_neigh": 1},
        {"neigh": 7, "nxt_neigh": 0}
    ])



screen = Screen()
screen.bgcolor("peachpuff")

star = t.Turtle()
star.hideturtle()
star.pensize(4)
star.speed(0)
Lines = draw_star(star)

intersections = {}
for r in range(0, 5):
    intersections[r] = find_intersection(Lines[r], Lines[(r+2) % 5])

circle_turtle = t.Turtle()
circle_turtle.hideturtle()
circle_turtle.speed(0)

circles = []
for r in range(0, 5):
    draw_circle(Lines[r][0], Lines[r][1], circle_turtle)
    circles.append(Circle(Lines[r][0], Lines[r][1]))

for r in range(0, 5):
    draw_circle(intersections[r].x, intersections[r].y, circle_turtle)
    circles.append(Circle(intersections[r].x, intersections[r].y))


assign_neighbours(circles)


circle_turtle.screen.onclick(lambda x, y, turtle=circle_turtle, star=star, circles=circles: click_function(x, y, circle_turtle, star, circles))

screen.mainloop()

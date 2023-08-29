import pygame as pg
import numpy as np



def handle_vertex_args(args):
    method, x, y, z = args


vertices = []

def parse_model(model):
    #model_arguments = []
    with open(model, "r") as object_file:
        for line in object_file:
            #model_arguments.append(line.replace("\n", "").split())
            arguments = line.replace("\n", "").split()
            if len(arguments) > 0:
                if arguments[0] == "v":
                    vertex = arguments
                    vertex.remove("v")
                
                    vertices.append([float(vertex[0]), float(vertex[1]), float(vertex[2])])
                
                    #handle_vertex_args(arguments)
            

    
    
    

parse_model("fish.obj")
print(vertices)

pg.init()
screen = pg.display.set_mode((1280, 720))
clock = pg.time.Clock()
running = True

while running:
    # poll for events
    # pg.QUIT event means the user clicked X to close your window
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    for vertex in vertices:
        #print(vertices)
        #print(vertex)
        pg.draw.circle(screen, (255, 255, 255), ((vertex[0]) * 400 + 200, 720 - ((vertex[1]) * 400 + 200)), 3)

    # flip() the display to put your work on screen
    pg.display.flip()

    clock.tick(60)  # limits FPS to 60

pg.quit()


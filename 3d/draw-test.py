import pygame as pg
import numpy as np
import tkinter as tk
from tkinter import filedialog


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
            

    
    
    
root = tk.Tk()
root.withdraw()
file_path = filedialog.askopenfilename()
parse_model(file_path)
print(vertices)

pg.init()
screen = pg.display.set_mode((1280, 720), pg.RESIZABLE)
width, height = pg.display.get_window_size()
clock = pg.time.Clock()
running = True
model_size = 400
dot_size = 3
location = [200, 200]

while running:
    # poll for events
    # pg.QUIT event means the user clicked X to close your window
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_UP:
                model_size += 10
            if event.key == pg.K_DOWN:
                model_size -= 10
            if event.key == pg.K_w:
                dot_size += 1
            if event.key == pg.K_s:
                dot_size -= 1
            if event.key == pg.K_d:
                location[0] += 20
            if event.key == pg.K_a:
                location[1] -= 20
    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    for vertex in vertices:
        #print(vertices)
        #print(vertex)
        pg.draw.circle(screen, (255, 255, 255), ((vertex[0]) * model_size + location[0], height - ((vertex[1]) * model_size + location[1])), dot_size)


    # flip() the display to put your work on screen
    pg.display.flip()

    clock.tick(60)  # limits FPS to 60

pg.quit()


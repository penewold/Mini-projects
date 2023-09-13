import pygame as pg
import numpy as np
import tkinter as tk
from tkinter import filedialog
import math

a1, a2, a3 = 0, 0, 0
vertices = []
aplied_vertices = []
running = True
model_size = 400
location = [200, 200]

def handle_vertex_args(args):
    method, x, y, z = args

def sin(angle):
    ra = math.sin(math.radians(angle))
    return ra

def cos(angle):
    ra = math.cos(math.radians(angle))
    return ra


xrot = np.array([[1, 0, 0],
        [0, cos(a1), sin(a1) * -1],
        [0, sin(a1), cos(a1)]])

yrot = np.array([[cos(a2), 0, sin(a2)],
        [0, 1, 0],
        [sin(a2) * -1, 0, cos(a2)]])

zrot = np.array([[cos(a3), sin(a3) * -1, 0],
        [sin(a3), cos(a3), 0],
        [0, 0, 1]])

def applyRotation(pos):
    a = np.dot(xrot, pos)
    a = np.dot(yrot, a)
    a = np.dot(zrot, a)
    return a


def parse_model(model):
    
    with open(model, "r") as object_file:
        for line in object_file:
            
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
#print(vertices)

pg.init()
font = pg.font.SysFont(None, 36)
text = font.render('hello', True, (255, 255, 0))
screen = pg.display.set_mode((1280, 720), pg.RESIZABLE)
width, height = [1280, 720]
clock = pg.time.Clock()





while running:
    width, height = pg.display.get_window_size()
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
            
            if event.key == pg.K_d:
                location[0] += 20
            if event.key == pg.K_a:
                location[0] -= 20
            if event.key == pg.K_w:
                location[1] += 20
            if event.key == pg.K_s:
                location[1] -= 20
    # fill the screen with a color to wipe away anything from last frame
    xrot = np.array([[1, 0, 0],
        [0, cos(a1), sin(a1) * -1],
        [0, sin(a1), cos(a1)]])
    
    yrot = np.array([[cos(a2), 0, sin(a2)],
        [0, 1, 0],
        [sin(a2) * -1, 0, cos(a2)]])

    zrot = np.array([[cos(a3), sin(a3) * -1, 0],
        [sin(a3), cos(a3), 0],
        [0, 0, 1]])
    
    
    for vertex in vertices:
        aplied_vertices.append(applyRotation(vertex))

    screen.fill("black")
    for vertex in aplied_vertices:
        pg.draw.circle(screen, "white", ((vertex[0]) * model_size + location[0], height - ((vertex[1]) * model_size + location[1])), 1)


    fps = font.render(str(round(clock.get_fps())), True, (255, 255, 0))
    
    screen.blit(fps, (20, 20))
    # flip() the display to put your work on screen
    pg.display.flip()

    a1 += 1
    a2 += 1
    a3 += 1
    aplied_vertices = []
    clock.tick(60)  # limits FPS to 60
    


pg.quit()


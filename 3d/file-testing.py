import pygame as pg
import numpy as np



args = []
def parse_model(model):
    with open("test_file.obj", "r") as object_file:
        for line in object_file:
            args.append(line.replace("\n", "").split())

    
    

print(args)
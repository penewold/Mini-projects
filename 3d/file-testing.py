import pygame as pg
import numpy as np

with open("test_file.obj", "r") as object_file:
    args = []
    for line in object_file:
        args.append(line.replace("\n", "").split())
    
    

print(args)
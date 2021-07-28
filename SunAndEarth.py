from OpenGL.GLU import *
from OpenGL.GL import *
import pygame
from pygame.locals import *
import random
import numpy as np
def Sphere(x,y,z,radius):
    
    vertices=[]
    i=float(z-radius)
    while(z-radius<=i and i<=z+radius):
        temp=[]
        theta=0
        while(0<=theta and theta<=2*np.pi):
  
            temp.append([x+(np.sqrt(radius**2-(i-z)**2))*np.cos(theta),y+(np.sqrt(radius**2-(i-z)**2))*np.sin(theta),i])
            theta+=np.pi/10
        vertices.append(temp)
        i+=radius/20
    
    glBegin(GL_LINES)
    for i in range(len(vertices)-1):
        for j in range(len(vertices[0])-1):
            glVertex3fv(vertices[i][j])
            glVertex3fv(vertices[i][j+1])
            glVertex3fv(vertices[i][j])
            glVertex3fv(vertices[i+1][j])

    try:
        for i in range(len(Center)-1):
            glVertex3fv(Center[i])
            glVertex3fv(Center[i+1])
    except:
        pass
    glEnd()

    '''glBegin(GL_QUADS)
    for Surface in Surfaces:
        glColor3fv((1,0.5,0))
        for vertex in Surface:
            glVertex3fv(Vertices[vertex])
    glEnd()'''

   


def Main():
    pygame.init()
    display = (900,800)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    glEnable(GL_DEPTH_TEST) 
    gluPerspective(45, (display[0]/display[1]), 0.1, 100000.0)
    glTranslatef(1,1, -100)
    global Center
    Center=[]
    distance=5000
    theta=0
    while(0<=theta and theta<=2*np.pi):
        Center.append([distance*np.cos(theta),0,-distance*np.sin(theta)])
        theta+=np.pi/500
    pos=0
    while(True):
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    glTranslatef(-2,0,0)
                elif event.key==pygame.K_RIGHT:
                    glTranslatef(2,0,0)
                elif event.key==pygame.K_UP:
                    glTranslatef(0,2,0)
                elif event.key==pygame.K_DOWN:
                    glTranslatef(0,-2,0)
                elif event.key==pygame.K_2:
                    glTranslatef(0,0,1)
                elif event.key==pygame.K_1:
                    glTranslatef(0,0,-2)
        
        if pygame.mouse.get_pressed()[0]==0:
            (X_pos,Y_pos)=pygame.mouse.get_pos()
        elif pygame.mouse.get_pressed()[0]==1:
            glTranslatef(0,0,0)
            glRotatef((pygame.mouse.get_pos()[0]-X_pos), 0, 1,0)
            glRotatef((pygame.mouse.get_pos()[1]-Y_pos), 1, 0,0)
            glTranslatef(0,0,0)
            (X_pos,Y_pos)=pygame.mouse.get_pos()
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        if pos>=len(Center):
            pos=0
        
        Sphere(0,0,-100,5)
        Sphere(Center[pos][0],Center[pos][1],Center[pos][2],1)
        pos+=1
        pygame.display.flip()
        pygame.time.wait(10)


Main()




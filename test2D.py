
#Alumno: Alejandro Cruz Alvarez Carranza
#No.Control: 18390043
#Grupo i5u
#Maestro: May Canché Isaias
#Materia: Graficación

import matplotlib.pyplot as plt
import numpy as np

#Creación de la tabla y establecimiento del tamaño del lienzo
plt.axis([-30,30,-30,30])
plt.axis('on')
plt.grid(True)

#Función para Rotar el rectangulo 
def rotRz(xp,yp,rz):
    Crz11 = np.cos(rz)
    Crz12 = -np.sin(rz)
    Crz21 = np.sin(rz)
    Crz22 = np.cos(rz)
    xpp = xp*Crz11+yp*Crz12
    ypp = xp*Crz21+yp-Crz22
    xg = xc + xpp
    yg = yc + ypp
    return (xg,yg)

#Valores para el escalado
sx=3/5
sy= 4/5

#Valor para el color
color=(.0,.4,.3)

#------------------------------Primer Rectangulo-------------------------------

#Poner Centro Primer Rectangulo
xc=0
yc=0

#Tamaño en el eje X del primer Rectangulo aplicando el escalado(sx)
xp1= 0*sx
xp2= 30*sx
xp3= 30*sx
xp4= 0*sx

#Tamaño en el eje Y del primer rectangulo aplicando el escalado(sy)
yp1= -20*sy
yp2= -20*sy
yp3= 0*sy
yp4= 0*sy

#Establecimiento de las posiciones del Primer Rectangulo con el escalado ya aplicado
xg1 = xc + xp1
yg1 = yc + yp1
xg2 = xc + xp2
yg2 = yc + yp2
xg3 = xc + xp3
yg3 = yc + yp3
xg4 = xc + xp4
yg4 = yc + yp4

#Guardado en una matriz de las posiciones del primer rectangulo para aplicar la rotación e impresion
xg = [xg1,xg2,xg3,xg4,xg1]
yg = [yg1,yg2,yg3,yg4,yg1]

#Grados de rotación que se le aplicará al primer rectangulo
rz=(4*6)*np.pi/180
#--------rotar el punto 1
xp=xp1
yp=yp1
[xg1,yg1]=rotRz(xp,yp,rz)
#--------rotar el punto 2
xp=xp2
yp=yp2
[xg2,yg2]=rotRz(xp,yp,rz)
#--------rotar el punto 3
xp=xp3
yp=yp3
[xg3,yg3]=rotRz(xp,yp,rz)
#--------rotar el punto 4
xp=xp4
yp=yp4
[xg4,yg4]=rotRz(xp,yp,rz)

#Guardado de las posiciones ya rotadas del primer rectangulo en una matriz para su dibujado
xg=[xg1,xg2,xg3,xg4,xg1]
yg=[yg1,yg2,yg3,yg4,yg1]

#Dibujado del primer rectangulo, habiendole aplicado escalado y posteriormente rotación
plt.plot(xg,yg,color=color)

#---------------------------------Segundo Rectangulo-------------------------------------

#establecer el centro del segundo rectangulo
xc=15
yc=-10

#Tamaño en el eje X del segundo rectangulo
xp1= 0
xp2= -30
xp3= -30
xp4= 0
#Tamaño en el eje Y del segundo rectangulo
yp1= 20
yp2= 20
yp3= 0
yp4= 0

#Establecimiento de las posiciones del segundo rectangulo
xg1 = xc + xp1
yg1 = yc + yp1
xg2 = xc + xp2
yg2 = yc + yp2
xg3 = xc + xp3
yg3 = yc + yp3
xg4 = xc + xp4
yg4 = yc + yp4

#Guardado de las posiciones del segundo rectangulo en una matriz para su dibujado
xg = [xg1,xg2,xg3,xg4,xg1]
yg = [yg1,yg2,yg3,yg4,yg1]
#Dibujado del segundo rectangulo
plt.plot(xg,yg,color=color)


#----------------------------Circulo----------------------
#Valores para dibujar un circulo
p1=0*np.pi/180
p2=360*np.pi/180
dp=(p2-p1)/100

#Establecimiento del centro del circulo
xc = 0
yc = 0
#radio del circulo
r=15

#Posiciones finales del circulo
xlast=xc+r*np.cos(p1)
ylast=yc+r*np.sin(p1)

#Dibujado del circulo
for p in np.arange(p1,p2+dp,dp):
    xp=xc+r*np.cos(p)
    yp=xc+r*np.sin(p)
    plt.plot([xlast,xp],[ylast,yp],color=color, linewidth=1)
    xlast=xp
    ylast=yp


#Impresion de todos los resultados
plt.show()
#Resolución de ecuaciones de segundo grado ax^2+bx+c=0

from math import sqrt       #IMportamos una función del módulo math

a=float(input('a='))
b=float(input('b='))
c=float(input('c='))

if a!=0 and((b**2)-(4*a*c))>=0 :          #Soluciones reales
    x1=(-b+sqrt((b**2)-4*a*c))/(2*a)
    x2=(-b-sqrt((b**2)-4*a*c))/(2*a)
    print('x1=',x1,'\n')
    print('x2=',x2,'\n')
elif a!=0 and ((b**2)-(4*a*c))<0:         #Soluciones complejas
    print('soluciones complejas\n')
    print('x1=',-b/(2*a),'+',sqrt(-((b**2)-4*a*c))/(2*a),'j\n')
    print('x2=',-b/(2*a),'-',sqrt(-((b**2)-4*a*c))/(2*a),'j\n')
elif a==0 and b==0 and c==0:
    print('La ecuación tiene infinitas soluciones\n')
elif a==0 and b==0:
    print('La ecuación no tiene solución\n') 
else:                                     #Solución como ecuación de primer orden           
    x=-c/b
    print('x=',x,'\n')


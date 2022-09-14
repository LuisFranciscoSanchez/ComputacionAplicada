import numpy as np

#Entradas del Usuario

n1 = list(map(float,input("Introduce los coeficientes de la primera ecuación como arreglo de la matriz ampliada: ").split()))
n1 = np.asarray(n1)
n2 = list(map(float,input("Introduce los coeficientes de la segunda ecuación como arreglo de la matriz ampliada: ").split()))
n2 = np.asarray(n2)
n3 = list(map(float,input("Introduce los coeficientes de la tercera ecuación como arreglo de la matriz ampliada: ").split()))
n3 = np.asarray(n3)

m = np.matrix([[n1[0], n1[1], n1[2], n1[3]], [n2[0], n2[1], n2[2], n2[3]], [n3[0], n3[1], n3[2], n3[3]]])
det = np.matrix([[n1[0], n1[1], n1[2]], [n2[0], n2[1], n2[2]], [n3[0], n3[1], n3[2]]])
print("\n Matriz ampliada: \n",m )

#Calculo de determinantes

detM = np.linalg.det(det) 

detX = m[:, [3, 1, 2]]
detX = np.linalg.det(detX)

detY = m[:, [0, 3, 2]]
detY = np.linalg.det(detY)

detZ = m[:, [0, 1, 3]]
detZ = np.linalg.det(detZ)

#Calculo de variables

print("\n Las toneladas diarias necesarias de cada ingrediente son: \n")
x = detX/detM
print("K: ",x)
y = detY/detM
print("NO3: ",y)
z = detZ/detM
print("PO4: ",z)

#Solución del sistema de ecuaciones con función predeterminada Numpy

sol = np.linalg.solve(det,[n1[3], n2[3], n3[3]])
print("\n Con la función predeterminada de la librería Numpy, las cantidades de cada ingrediente son: \n"
      ,"\n K: ",sol[0],"\n NO3: ",sol[1],"\n PO4: ",sol[2])

#Error porcentual entre ambos métodos

e1 = abs(((sol[0]-x)/sol[0])*100)
e2 = abs(((sol[1]-y)/sol[1])*100)
e3 = abs(((sol[2]-z)/sol[2])*100)

print("\n El error porcentual entre ambos métodos es: \n",
      "\n K:",e1,"%","\n NO3: ",e2,"%","\n PO4: ",e3,"%")

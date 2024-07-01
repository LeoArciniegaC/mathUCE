#Operadores en Python
#(También se puede comentar con 3 comillas)
"""Operadores aritméticos"""
#Operadores aritméticos
a=2
b=3
suma=a+b #esto es una suma
print("La suma de ", a, " más ", b, " es ", suma)
resta=a-b #esto es una resta
print("La resta de ", a, " menos ", b, " es ", resta)
multipl=a*b #esto es una multiplicación
print("La multiplicación de ", a, " por ", b, " es ", multipl)
div=a/b #esto es una división normal
print("La división de ", a, " para ", b, " es ", div)
div_ent=a//b
print("La división entera de ", a, " entre ", b, " es ", div_ent)
modulo=a%b #esto es un módulo
print("El módulo de la división entre ", a, " y ", b, " es ", modulo)
exponent=a**b #esto es una potencia
print("La potencia de base ", a, " y exponente ", b, " es ", exponent)

#Operadores Relacionales
print("Operaciones relacionales")
c=6
d=7
e=2
f=1
mayor=c>d #esto es mayor que
print("¿", c, " es mayor que ", d, "? ", mayor)
menor=c<d #esto es menor que
print("¿", c, " es menor que ", d, "? ", menor)
menor_igual=e<=d #esto es menor o igual que
print("¿", e, " es menor o igual que ", d, "? ", menor_igual)
mayor_igual=d>=c #esto es mayor o igual que
print("¿", d, " es mayor o igual que ", c, "? ", mayor_igual)
dif=c!=d #esto es diferente
print("¿", c, " es diferente que ", d, "? ", dif)
igual=e==f #esto es igual
print("¿", e, " es igual que ", f, "? ", igual)

#Operadores Lógicos
p=5>2
q=2<1
p or q #esto significa o
p and q #esto significa y
not p #Esto significa la negación
print("P es 5>2, P es ", p)
print("Q es 2<1, Q es ", q)
print("La proposición P o Q es: ", p or q)
print("La proposición P y Q es: ", p and q)
print("La negación de p es: ", not p)
print("La negación de q es: ", not q)
#para poner "p entonces q", hay que usar su equivalencia:
not p or q #Esto es "entonces"
print("La proposición P entonces Q es: ", not p or q)
print("La proposición Q entonces P es: ", not q or p)

#Tipos de divisiones
#Entera: (con doble barra "//")
div_ent2=27//14
print(div_ent2)
#Decimal: (con una sola barra "/")
div2=27/14
print(div2)
#Módulo: (con el símbolo de porcentaje "%")
modulo2=27%14
print(modulo2)

#Conversión de expresiones
a=1
b=5
c=6
x1=(-b+(b**2-4*a*c)**(1/2))/(2*a)
x2=(-b-(b**2-4*a*c)**(1/2))/(2*a)
print(x1)
print(x2)
A=(x**(2-n))/((y*x+z)/z**(2+x))
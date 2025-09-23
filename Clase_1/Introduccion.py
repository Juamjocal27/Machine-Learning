## mensajes de bienvenida
print("Bienvenido a la clase de Introduccion")

## variables
nombre = "UNIVALLE"
estudiante= "Rudy Manzaneda"

print(nombre+" "+estudiante)

###
edad = 25
mensaje = f"Hola, mi nombre es {estudiante} y tengo {edad} años"
print(mensaje)

### reemplazar Cadenas
frase =  "Python es un lenguaje de programación muy popular"
print("Mayusculas: "+frase.upper())
print("Minusculas: "+frase.lower())

print("Reemplazar", frase.replace("Python", "Java"))

## Dedclaracion de variables con diferentes tipos de Datos
numero_entero = 10
numero_decimal = 3.14
texto = "UNIVALLE"
booleano = True

# Imprimir valores y tipos de datos
print(f"Numero entero: {numero_entero} Tipo: {type(numero_entero)}")
print(f"Numero decimal: {numero_decimal} Tipo: {type(numero_decimal)}")
print(f"Texto: {texto} Tipo: {type(texto)}")
print(f"Booleano: {booleano} Tipo {type(booleano)}")


## operadores aritmeticos
a = 10
b = 5

# Suma
c = a + b
print(f"Suma: {c}")

# Resta
d = a - b
print(f"Resta: {d}")

# Multiplicacion
e = a * b
print(f"Multiplicacion: {e}")

# Division
f = a / b   ##3 f=a//b
print(f"Division: {f}")

# Modulo
g = a % b
print(f"Modulo: {g}")

### Operadores de comparacion
h = 10
i = 5

# Mayor que
j = h > i
print(f"Mayor que: {j}")

# Mayor o igual que
k = h >= i
print(f"Mayor o igual que: {k}")

# Menor que
l = h < i
print(f"Menor que: {l}")

# Menor o igual que
m = h <= i
print(f"Menor o igual que: {m}")

# Igual que
n = h == i
print(f"Igual que: {n}")

##5=5  ## asigancion
##5==5  ## comparacion
##5==='5'  ## comparacion de tipos o exacta
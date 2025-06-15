nombre = input("¡Bienvenido! Por favor ingrese su nombre: ")
edad = int(input("¿Cuál es su edad? "))
pais = input("Ingrese su país de residencia. ").strip().lower()
if pais in {"chile", "argentina", "colombia"} and edad >= 18:
    beneficio = "si"
else:
    beneficio = "no"

print(f"De acuerdo a los datos ingresado, {nombre}, usted {beneficio} puede acceder al beneficio.")
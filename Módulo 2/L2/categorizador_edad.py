nombre = input("Por favor, ingrese su nombre: ")
edad = int(input("¿Qué edad tienes? "))
if edad < 18:
    categoria = "menor de edad"
elif edad < 65:
    categoria = "adulto"
else:
    categoria = "adulto mayor"
print(f"¡Hola, {nombre}! Eres {categoria}.")

decision = input("¿Desa ver el resumen de categorías? (s|n): ").strip().lower()
if decision == "s":
    print("\n-------Categorías de Edad-------")
    print("Menor de edad: menos de 18 años.")
    print("Adulto: entre 18 y 64 años")
    print("Adulto mayor: 65 años o más.")
# Objetivos de la actividad

La actividad busca reforzar los conocimientos sobre implementación y manejo de excepciones, usando la calculadora simple implementada en dos ejercicios anteriores.

# Descripción de la actividad

Se solicita mejorar la calculadora básica diseñada en ejercicios anteriores agregando el manejo de excepciones. En particular, se deben manejar y capturar excepciones para:
- División por cero.
- Entrada no válida (cuando el usuario ingresa texto en vez de números cuando se le solicitan estos).
- Operador no válido (cuando el usuario ingresa una selección distinta a las operaciones disponibles).


# Resultados

En el módulo excepciones.py se implementan las excepciones DivisionPorCero y OperacionNoValida para manejar dos de las excepciones mencionadas para la actividad. Por otro lado, en el módulo
operaciones.py se implementan las operaciones básicas de la calculadora y, finalmente, se implementa la calculadora en el script calculadora.py, específicamente la función calcular.

Al ejecutar calculadora.py, inicialmente la función calcular solicita al usuario que ingrese la operación que desea ejecutar. Si el valor ingresado no está dentro de las opciones disponibles,
lanza una excepción de OperacionNoValida, mostrando el mensaje de error en consola y saliendo de la función con normalidad.

Si el usuario ingresa una operación válida, el programa solicitará los números sobre los que desea operar. Si el usuario ingresa un valor que no se pueda convertir a número en cualquiera de los dos casos,
lanza una excepción ValueError. Por otro lado, si la operación corresponde a división y el segundo número ingresado es 0, la función lanza una excepción de DivisionPorCero. En cualquiera de los caso mencionados,
se imprime el mensaje en pantalla y se sale de la función con normalidad.

Finalmente, si todos los datos ingresados son válidos, se imprimirá en pantalla el resultado obtenido.

![image](https://github.com/user-attachments/assets/a6828d69-0cff-4de3-9749-fdfcbc1e4bb1)

![image](https://github.com/user-attachments/assets/1d0296fc-0190-4f11-a779-cb84ac70be79)

![image](https://github.com/user-attachments/assets/4f0090ed-1522-4786-80bc-6264e46266fe)

![image](https://github.com/user-attachments/assets/c7239319-8b98-405f-bd8b-28d90b638f3b)

![image](https://github.com/user-attachments/assets/c85aa1c0-3054-4bbb-afec-33e3d39a73d5)

Las imágenes anteriores muestran que el programa funciona según lo esperado, y que las excepciones han sido manejadas de forma decuada.

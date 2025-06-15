# Objetivos de la actividad

Esta actividad busca reforzar los conocimientos sobre programación orientada a objetos (POO) y la construcción de clases a partir de la construcción de una clase persona.

# Descripción de la actividad

La actividad consiste en implementar la clase Persona, la cual está diseñada para contener datos básicos de una persona del mundo real y realizar algunas operaciones sobre estos. En particular, se solicita que
la clase contenga los atributos/propiedades nombre, edad y correo_electronico. Esta clase debe implementar métodos que permitan validar que el correo electrónico de la persona está ingresado en un formato adecuado,
permita actualizar la información de la persona y permita comprobar si esta es mayor de edad. Además, se solicita que, al imprimir una instancia de la clase Persona, esta se muestre de una forma amigable
para el usuario.

# Resultados

La clase Persona se implementa en un módulo llamado persona.py, y se pone a prueba en el script test.py.

Para implementar la validación de correo electrónico, se optó por implementarlo como una propiedad de la clase, con métodos getter y setter, de forma que la información se valide desde el momento en que se instancia a la clase.
El método setter usa la librería [re](https://docs.python.org/3/library/re.html) de Python para verificar el formato del correo: este debe tener al menos un carácter del alfabeto antes de un símbolo @,
posteriormente al menos una letra, seguido de un punto y una o más letras.

Para probar el funcionamiento de la clase Persona, primero se intenta instanciar la clase con un correo inválido (en el ejemplo, "abc"). La excepción se maneja en un bloque try-except, de forma, que se imprima
el mensaje de error en el caso que la clase funcione de manera adecuada.

Después de esto, se crea otra instancia de la clase Persona, esta vez con un correo electrónico valida, y se imprime dicha instancia. Posteriormente, se actualizan los datos de la instancia, modificando nombre, edad, y
correo electrónico. Se vuelve a imprimir la instancia y se procede finalmente a verificar si esta es mayor de edad, imprimiendo el resultado.

![image](https://github.com/user-attachments/assets/10d6b851-e89d-404a-b035-5aff9da514f2)

La imágen anterior muestra los resultados obtenidos, los cuales son los esperados.

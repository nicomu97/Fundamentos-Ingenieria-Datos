# Objetivos de la actividad

Reforzar los conocimientos sobre creación y manejo de excepciones a través de la creación de un administrador simple de biblioteca.

# Descripción de la actividad

Se solicita desarrollar una parte básica de un sistema de biblioteca. Esta debe permitir al usuario pedir prestado un libro, validar que el libro esté en stock y actualizar el estado del libro. Para ello, se debe crear
una clase Libro con los atributos titulo, autor y stock, y una clase Biblioteca que reciba un catálogo (diccionario) de libros e implemente un método prestar_libro(titulo) que:
- Verifique que el libro está en el catálogo de la biblioteca.
- Verifique si hay stock del libro.
- Reduzca el stock si hay ejemplares disponibles.
- Lance una excepción LibroNoDisponibleError si no hay stock.

# Desarrollo

Se desarrolla lo solicitado en el módulo biblioteca.py. Adicionalmente, aunque no es solicitado en la actividad:
- Se modifica el método __str__ en las clases Libro y Biblioteca para que, al imprimirlos en pantalla, sus atributos se impriman de forma legible.
- Se agregan los atributos como propiedades para ejecutar validación de los datos ingresados.

Para probar que el módulo funciona correctamente, se crea el script test.py, donde se crean dos instancias distintas de libro, se añaden a un catálogo de libros que se usa para
instanciar la clase Biblioteca y se procede a probar el método prestar libro en diferentes circunstancias.

Al ejecutar el script test.py, se obtienen los siguientes resultados.

![image](https://github.com/user-attachments/assets/89bdd3ed-23c0-4d04-988a-727ce30408f2)

![image](https://github.com/user-attachments/assets/8d05f8b4-6af0-48a0-b320-367c93deb147)

Lo anterior muestra que el módulo funciona correctamente y que las excepciones han sido manejadas de manera adecuada.

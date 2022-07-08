# Guardar la puntuación en un archivo de texto

import pickle

def obtener_puntuacion_mas_alta():
    # Puntuación más alta por defecto
    puntuacion_mas_alta = 0
 
    # Intentemos leer la puntuación más alta desde un archivo
    try:
        archivo_puntuacion_mas_alta = open("high_score.txt", "r")
        puntuacion_mas_alta = int(archivo_puntuacion_mas_alta.read())
        archivo_puntuacion_mas_alta.close()
        print("La puntuación más alta es", puntuacion_mas_alta)
    except IOError:
        # Error al leer el archivo, no existe una puntuación más alta
        print("Aún no existe una puntuación más alta.")
    except ValueError:
        # Hay un archivo allí, pero no entiendo los números.
        print("Estoy confundido. Empezamos sin una puntuación alta.")
 
    return puntuacion_mas_alta
 
def guardar_puntuacion_mas_alta(nueva_puntuacion_mas_alta):
    try:
        # Escribimos el archivo en disco
        archivo_puntuacion_mas_alta = open("high_score.txt", "w")
        archivo_puntuacion_mas_alta.write(str(nueva_puntuacion_mas_alta))
        archivo_puntuacion_mas_alta.close()
    except IOError:
        # Um, no puedo escribirlo.
        print("No soy capaz de guardar la puntuación alta.")
     
def main():
    """ Aquí va el programa principal. """
    # Obtenemos la puntuación más alta.
    puntuacion_mas_alta = obtener_puntuacion_mas_alta()
     
# Obtenemos la puntuación del juego en curso
    puntuacion_actual = 0
    try:
        # Pregúntale al usuario/a por su puntuación
        puntuacion_actual = int(input ("¿Cuál es tu puntuación? "))
    except ValueError:
        # Error, no puedo convertir lo que ha escrito en un número
        print("No comprendo qué has escrito.")
         
 
    # Observa por si tenemos una nueva puntuación más alta
    if puntuacion_actual > puntuacion_mas_alta:
        # Conseguido! Guardamos en disco
        print("Bravo! Nueva puntuación más alta!")
        guardar_puntuacion_mas_alta(puntuacion_actual)
    else:
        print("Mejor suerte la próxima vez.")

# Llamamos a la función principal, empezamos el juego
if __name__ == "__main__":
    main()


#score = open("score.csv","w")
#nombre = str(input("Ingrese su nombre "))
#puntuacion = str(input("Ingrese su puntuación "))

#score.write('Score')
#score.write(";")
#score.write(nombre)
#score.write(";")
#score.write(puntuacion)
#score.close()

# Ejercicio 4 - Promedio seguro con manejo de errores
import os

def safe_average(filename):
    """
    Lee un archivo donde hay UN número por línea y retorna el promedio de
    los números válidos (como float).

    Reglas:
    - Las líneas que no se puedan convertir a float deben ignorarse (usar
      try/except ValueError internamente).
    - Las líneas vacías también se ignoran.
    - Si el archivo no existe, propagar FileNotFoundError.
    - Si el archivo existe pero no contiene ningún número válido, lanzar
      ValueError("no valid numbers").

    Args:
        filename: str - nombre del archivo a leer.

    Returns:
        float - promedio de los números válidos.

    Raises:
        FileNotFoundError: si el archivo no existe.
        ValueError: si no hay números válidos en el archivo.

    Ejemplo:
        # archivo contiene: "10\n20\nno_es_un_numero\n30\n"
        safe_average("numeros.txt") -> 20.0
    """

    if not os.path.exists(filename):
        raise FileNotFoundError

    sumatoria = 0

    with open( file=filename, mode='r' ) as archivo:
        lista = [linea for linea in archivo]
        cantidad_numeros = len(lista)

        for linea in lista:
            while True:
                try:
                    sumatoria += float(linea)
                    break
                except ValueError:
                    cantidad_numeros -= 1                    
                    break

        if cantidad_numeros <= 0:
            raise ValueError("no valid numbers")


    return sumatoria / cantidad_numeros
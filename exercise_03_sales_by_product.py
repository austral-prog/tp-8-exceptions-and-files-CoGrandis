# Ejercicio 3 - Ventas por producto
import os

def read_sales(filename):
    """
    Lee un archivo con ventas en formato "producto:valor;producto:valor;..."
    (todo en una sola línea, los registros separados por ';') y agrupa los
    valores en una lista por producto.

    Reglas:
    - Los valores se convierten a float.
    - El orden de los montos dentro de la lista es el mismo en que aparecen
      en el archivo.
    - Los separadores ';' finales sin contenido se ignoran (es común que
      el archivo termine con ';').
    - Si el archivo no existe, propagar FileNotFoundError.

    Args:
        filename: str - nombre del archivo a leer.

    Returns:
        dict[str, list[float]] - montos de venta agrupados por producto.

    Raises:
        FileNotFoundError: si el archivo no existe.

    Ejemplo:
        # archivo contiene: "producto1:100;producto2:200;producto1:150;"
        read_sales("ventas.txt") -> {
            "producto1": [100.0, 150.0],
            "producto2": [200.0],
        }
    """

    if not os.path.exists(filename):
        raise FileNotFoundError
        

    diccionarios_productos = {}

    with open( file=filename, mode='r' ) as archivo:

        contenido = archivo.read()
        lista_productos = contenido.strip().split(';')

        lista_productos = [ item.split(':') for item in lista_productos if item != '']

        for producto in lista_productos:
            nombre, precio = producto

            if nombre not in diccionarios_productos:
                diccionarios_productos[nombre] = [float(precio)]
            else:
                diccionarios_productos[nombre].append(float(precio))

    return diccionarios_productos



def process_sales(data):
    """
    Para cada producto del diccionario, imprime en el orden natural del dict:

        producto: ventas totales $X.XX, promedio $Y.YY

    Los valores de total y promedio deben mostrarse siempre con DOS
    decimales.

    Args:
        data: dict[str, list[float]] - salida de read_sales.

    Returns:
        None

    Ejemplo:
        process_sales({"producto1": [100.0, 150.0]})
        # imprime: "producto1: ventas totales $250.00, promedio $125.00"
    """

    for clave, valor in data.items():
        ventas_totales = 0
        for item in valor:
            ventas_totales += item

        promedio = ventas_totales / len(valor)


        print(f'{clave}: ventas totales ${ventas_totales:.2f}, promedio ${promedio:.2f}')


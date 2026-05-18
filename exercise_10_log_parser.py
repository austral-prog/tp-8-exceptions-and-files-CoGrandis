# Ejercicio 10 - Parser de archivos de log
import os

def parse_log(filename):
    """
    Lee un archivo de log donde cada línea tiene el formato:

        NIVEL: mensaje

    y retorna un diccionario donde la clave es el nivel y el valor es una
    lista con todos los mensajes de ese nivel, en el orden en que aparecen.

    Reglas:
    - Los niveles no son fijos: cualquier string antes del primer ':'
      cuenta como nivel. El mensaje es todo lo que viene después del
      primer ':'.
    - Aplicar strip al nivel y al mensaje para eliminar espacios sobrantes.
    - Las líneas vacías (o con solo espacios) se ignoran: NO son inválidas.
    - Si alguna línea no vacía NO tiene ':', lanzar
      ValueError("invalid log line").
    - Si el archivo no existe, propagar FileNotFoundError.

    Args:
        filename: str - nombre del archivo a leer.

    Returns:
        dict[str, list[str]] - mensajes agrupados por nivel.

    Raises:
        FileNotFoundError: si el archivo no existe.
        ValueError: si alguna línea no vacía no tiene ':'.

    Ejemplo:
        # archivo contiene:
        # INFO: servidor iniciado
        # ERROR: no se puede conectar
        # INFO: reintentando
        # WARN: lento
        parse_log("server.log") -> {
            "INFO": ["servidor iniciado", "reintentando"],
            "ERROR": ["no se puede conectar"],
            "WARN": ["lento"],
        }
    """

    if not os.path.exists(filename):
        raise FileNotFoundError
    

    log = {}


    with open(file=filename, mode='r') as archivo:
        for linea in archivo:
            if len(linea.strip('\n').strip())  > 0 :                   
                if ':' not in linea:
                    raise ValueError('Invalid log line')

                nivel, mensaje = linea.strip('\n').split(':', 1)

                if nivel not in log.keys():
                    log[nivel.strip()] =  list([mensaje.strip()])
                                        

                else:
                    log[nivel.strip()].append(mensaje.strip())

    return log

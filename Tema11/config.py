# Bloque try-catch para controlar la excepción de tipo "Archivo no encontrado"
""" def main():
    try:
        configuration = open('config.txt')
    except FileNotFoundError:
        print("Couldn't find the config.txt file!") """

# Bloque try-catch para controlar las excepciones en general
""" def main():
    try:
        configuration = open('config.txt')
    except Exception:
        print("Couldn't find the config.txt file!") """

# Bloque try-catch para controlar las excepciones posibles
""" def main():
    try:
        configuration = open('config.txt')
    except FileNotFoundError:
        print("Couldn't find the config.txt file!")
    except IsADirectoryError:
        print("Found config.txt but it is a directory, couldn't read it") """

# Bloque try-catch para controlar excepciones, si son parecidaas se pueden agrupar en una sola
def main():
    try:
        configuration = open('config.txt')
    except FileNotFoundError:
        print("Couldn't find the config.txt file!")
    except IsADirectoryError:
        print("Found config.txt but it is a directory, couldn't read it")
    except (BlockingIOError, TimeoutError):
        print("Filesystem under heavy load, can't complete reading configuration file")

if __name__ == '__main__':
    main()
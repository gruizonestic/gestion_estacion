# Codigo de prueba del backend.
# Escribe el fichero /var/backend/test.txt
# cada vez que se ejecuta un contenedor.

if __name__ == "__main__":
    write = 0
    while True:
        print("Esto sería el código del backend")
        if write == 0:
            f = open("/var/backend/test.txt", "a")
            f.write("He escrito algo\n")
            f.close()
            write = 1

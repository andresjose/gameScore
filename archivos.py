class Archivos:
    @property
    def leerArchivo(self):
        file = open("DBAntecedentes.csv","r")
        return file

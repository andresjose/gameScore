from archivos import Archivos


class Antecedentes:
    def consultaAntecedentesNombre(self, nombre):
        data = Archivos().leerArchivo()
        detalleAntecedente = ""
        for registro in data:
            infoPersona = registro.split(",")
            if (nombre == infoPersona[0]):
                detalleAntecedente = infoPersona[3]
                break
        return detalleAntecedente

    def consultaImagen(self, nombre):
        data = Archivos().leerArchivo()
        imagen = ""
        for registro in data:
            infoPersona = registro.split(",")
            if (nombre == infoPersona[0]):
                imagen = infoPersona[4]
                break
        return imagen

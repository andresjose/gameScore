from html import GeneraHtml
import cherrypy, html
import cherrypy, os
import os


class goodAndDevil(object):
    @cherrypy.expose
    def index(self):
        return """ 
<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" content="width=device-width">
    <title>Selector Genero</title>
    <link href="static/css/style.css" rel="stylesheet" type="text/css"/>
    <script src="static/js/jquery.min.js"></script>
    <script src="static/js/javascript.js"></script>
</head>
<body>
    <div id="contenedor">
        <div class="cajon" id="masculino" <!--onmouseover="cambioImagenM();-->">
            <div class="signo_masculino">
                <img src="static/images/idmasculino.png" alt="MASCULINO" id="cambio">
            </div>
        </div>
        <div class="cajon" id="letra" <!--onmouseover="cambioImagenG();-->">
            <h1>Selecciona<br> tu Genero</h1>
            <br>
            <br>
            <br>
            <br>
            <br>
            <br>
            <br>
            <br>
            <br>
            <form action="genero">
                <input type="text" name="genero">
                <input type="submit" value="Enviar">
            </form>
        </div>
        <div class="cajon" id="femenino" <!--onmouseover="cambioImagenF();-->">
            <div class="signo_femenino">
                <img src="static/images/idfemenino.png" alt="FEMENINO">
            </div>
        </div>
    </div>
</body>
</html>
        """

    """
    @cherrypy.expose
    def traerImagenH(self):
        return open("public/modulo/imagenGenero.html")

    @cherrypy.expose
    def traerImagenM(self):
        return open("public/modulo/imagenHombre.html")

    @cherrypy.expose
    def traerImagenG(self):
        return open("public/modulo/imagenMujer.html")

    """
    @cherrypy.expose
    def traerCsv(self):
        return open('DBAntecedentes.csv')

    @cherrypy.expose
    def traerImagenS(self):
        return "hola"

    @cherrypy.expose
    def genero(self, genero=""):
        if (genero == "hombre"):
            res = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width">
    <title>Avatar Nombre Hombre</title>
    <link href="static/css/hombre.css" rel="stylesheet" type="text/css"/>
    <script src="static/js/jquery.min.js"></script>
    <script src="static/js/javascript.js"></script>
</head>
<body>
    <h1>Genero<br> Masculino</h1>
    <div class="signo_masculino">
        <center>
            <img src="static/images/idmasculino.png" alt="MASCULINO">
        </center>
    </div>
    <div class="signo_femenino">
        <center>
            <img src="static/images/idfemenino.png" alt="FEMENINO">
        </center>
    </div>
    <div>
         <a href="/listaHombres" class="button button1"  >BuscarLista</a>
    </div>
</body>

</html>"""
            return res
        if (genero == "mujer"):
            res = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width">
    <title>Avatar Nombre Mujer</title>
    <link href="static/css/mujer.css" rel="stylesheet" type="text/css"/>
    <script src="static/js/jquery.min.js"></script>
    <script src="static/js/javascript.js"></script>
</head>
<body>
    <h1>Genero<br> Femenino</h1>
    <div class="signo_masculino">
        <center>
    
            <img src="static/images/idmasculino.png" alt="MASCULINO">
        </center>
    </div>
    <div class="signo_femenino">
        <center>
            <img src="static/images/idfemenino.png" alt="FEMENINO">
        </center>
    </div>
    
    <div>
        <a href="/listaMujeres" class="button button1"  >BuscarLista</a>
        
    </div>
</body>
</html>
"""
            return res
        else:
            return "no se encuentra este genero"

    @cherrypy.expose
    def listaHombres(self):
        return """
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width">
    <title>Avatar Nombre Mujer</title>
    <link href="static/css/listahombres.css" rel="stylesheet" type="text/css"/>
    <script src="static/js/jquery.min.js"></script>
    <script src="static/js/javascript.js"></script>
</head>
<body>
    <button onclick="filtrarH();">buscarPersonaH</button>
    <table></table>
</body>
</html>
"""
    @cherrypy.expose
    def pagina(self):
        pagina = "<!DOCTYPE html><html><body><h1>$titulo</h1><p>My first paragraph.</p></body></html>"
        pagina = pagina.replace("$titulo", GeneraHtml().createList())
        return pagina

    @cherrypy.expose
    def listaMujeres(self):
        return """
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width">
    <title>Avatar Nombre Mujer</title>
    <link href="static/css/listamujeres.css" rel="stylesheet" type="text/css"/>
    <script src="static/js/jquery.min.js"></script>
    <script src="static/js/javascript.js"></script>
</head>
<body>
    <button onclick="filtrarM();">buscarPersonaM</button>
    <table></table>
</body>
</html>
"""



if __name__ == '__main__':
    conf = {
        '/': {
            'tools.sessions.on': True,
            'tools.staticdir.root': os.path.abspath(os.getcwd())
        },
        '/static': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': './public'
        }
    }
    cherrypy.config.update({'server.socket_host': '127.0.0.1', })
    cherrypy.config.update({'server.socket_port': int(os.environ.get('PORT', '4000')), })
    cherrypy.quickstart(goodAndDevil(), '/', conf)



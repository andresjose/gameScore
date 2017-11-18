from html import GeneraHtml
import cherrypy, html
import cherrypy, os
import os


class LorenaJudicial:
    @cherrypy.expose
    def index(self):
        return """
        <form action="/info">
        <input type="text" name="nombre">
        <input type="submit" value="consultar">
        </form>        
        """

    @cherrypy.expose
    def info(self, nombre=""):
        res = "<p> {$detalleAntecedente} </p> <img src=\"/static/images/{$imagenConsulta}\">"
        detalleAntecedente = Antecedentes().consultaAntecedentesNombre(nombre)
        imagenConsulta = Antecedentes().consultaImagen(nombre)
        res = res.replace("{$detalleAntecedente}", detalleAntecedente)
        res = res.replace("{$imagenConsulta}", imagenConsulta)
        return res


class goodAndDevil(object):
    @cherrypy.expose
    def index(self):
        return """ 
<!DOCTYPE html>

<html>

<head>

	<meta name="viewport" content="width=device-width">
	<title>Selector Genero</title>
	<link href="static/css/style.css" rel="stylesheet" type="text/css" />
	<script src="static/https://ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js"></script>
	<script src="static/js/javascript.js"> </script>




</head>

<body >
<div id="contenedor">

	<div class="cajon" id="masculino" <!--onmouseover="cambioImagenM();-->">
		<div class="signo_masculino"  >
			<img src="static/images/idmasculino.png" alt="MASCULINO" id="cambio" >
		</div>
	</div>
	<div class="cajon"  id="letra" <!--onmouseover="cambioImagenG();-->">
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
        </form>|
	</div>
	<div class="cajon"  id="<!--femenino" onmouseover="cambioImagenF();-->">
		<div class="signo_femenino">
			<img src="static/images/idfemenino.png" alt="FEMENINO">
		</div>
	</div>
</div>

</body>

</html>






        


        """

    @cherrypy.expose
    def genero(self, genero=""):
        if (genero == "hombre"):
            res = """<!DOCTYPE html>

<html>
  
<head>
    
<meta charset="utf-8">
    
<meta name="viewport" content="width=device-width">
    
<title>Avatar Nombre Hombre</title>
    
<link href="static/css/hombre.css" rel="stylesheet" type="text/css" />
  
</head>
  
<body>
  

<h1>Selecciona<br> tu Genero</h1>


	<div class="signo_masculino" ><center>
  
	<img src="static/images/idmasculino.png" alt="MASCULINO" >
  </center></div>
  

	
	<div class="signo_femenino"><center>
  
	<img src="static/images/idfemenino.png" alt="FEMENINO">
  
	</center></div>

			<form>
  			<label for="fname"><h2><center>Primer Nombre</center></h2></label>
  			<center><input type="text" id="fname" name="fname" value="Andres"></center>
  			<label for="lname"><h2><center>Primer Apellido</center></h2></label>
  			<center><input type="text" id="lname" name="lname" value="Rincon"></center>
			</form>
	
	<div>
	<button class="button button1"><p> Ingresar Nombre </p></button>
	</div>






</body>

</html>"""
        else:
            res = """<!DOCTYPE html>

<html>
  
<head>
    
<meta charset="utf-8">
    
<meta name="viewport" content="width=device-width">
    
<title>Avatar Nombre Mujer</title>
    
<link href="static/css/mujer.css" rel="stylesheet" type="text/css" />
  
</head>
  
<body>
  

<h1>Selecciona<br> tu Genero</h1>



	<div class="signo_masculino" ><center>
  
	<img src="static/images/idmasculino.png" alt="MASCULINO" >
	</center></div>
  
	
	
<div class="signo_femenino"><center>
  
	<img src="static/images/idfemenino.png" alt="FEMENINO">
  
	</center></div>


			<form>
  			<label for="fname"><h2><center>Primer Nombre</center></h2></label>
  			<center><input type="text" id="fname" name="fname" value="Alejandra"></center>
  			<label for="lname"><h2><center>Primer Apellido</center></h2></label>
  			<center><input type="text" id="lname" name="lname" value="Martinez"></center>
			</form>
	<div>	
	<button class="button button1"><p> Ingresar Nombre </p></button>
	</div>

</body>

</html>"""
        return res

    @cherrypy.expose
    def pagina(self):
        pagina = "<!DOCTYPE html><html><body><h1>$titulo</h1><p>My first paragraph.</p></body></html>"
        pagina = pagina.replace("$titulo", GeneraHtml().createList())
        return pagina


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
    cherrypy.config.update({'server.socket_port': int(os.environ.get('PORT', '7000')), })
    cherrypy.quickstart(goodAndDevil(), '/', conf)



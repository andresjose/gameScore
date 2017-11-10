from html import GeneraHtml
import cherrypy, html
import cherrypy, os
import os


class goodAndDevil(object):
    @cherrypy.expose
    def index(self):
        return GeneraHtml().createList()

    @cherrypy.expose
    def gregorio(self):
        return "rece gregorio"

    @cherrypy.expose
    def andres(self, nota=0):
        return """
        <!DOCTYPE html><html><body><div id="demo"><h1>The XMLHttpRequest Object</h1><button type="button" onclick="loadDoc()">Change Content</button></div><script>function loadDoc(){var xhttp=new XMLHttpRequest(); xhttp.onreadystatechange=function(){if (this.readyState==4 && this.status==200){document.getElementById("demo").innerHTML=this.responseText;}}; xhttp.open("GET", "http://127.0.0.1:8000/", true); xhttp.send();}</script></body></html>
        """

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
    cherrypy.config.update({'server.socket_port': int(os.environ.get('PORT', '8000')), })
    cherrypy.quickstart(goodAndDevil(), '/', conf)

















import html

import cherrypy, os
import os


class goodAndDevil(object):
    @cherrypy.expose
    def index(self):
        return self.generaHtml()

    def generaHtml(self):
        html = ""
        for i in range(0,10):
            html += str(i)

        return html



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
    cherrypy.config.update({'server.socket_port': int(os.environ.get('PORT', '5000')), })
    cherrypy.quickstart(goodAndDevil(), '/', conf)


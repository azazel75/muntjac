import webbrowser

from os.path import dirname

from paste.deploy import loadapp
from paste.httpserver import serve


wsgi_app = loadapp('config:conf.ini',
                   relative_to=dirname(__file__))

host = '127.0.0.1'
port = 8080

webbrowser.open('http://%s:%d/SimpleApp' % (host, port), new=0)

serve(wsgi_app, host=host, port=port)

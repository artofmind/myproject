from wsgiref.simple_server import make_server #Импортирует функцию make_server, которая может создать простой веб-сервер при передаче приложения
from jinja2 import Environment, FileSystemLoader, Template #Импортирует шаблоны Environment,FileSystemLoader,Template для настройки jinja2

input1 = '<div class='top'>Middleware TOP</div>\n'#строки, которые необходимо вставить в тело страницы
input2 = '\n<div class='botton'>Middleware BOTTOM</div>'

class Midwr(object):
    def __init__(self, application):
       self.application = application
    def __call__(self, environ, response):  
        page = self.application(environ, response)[0]
        if (html.find('<body>') > 0 and html.find('</body>') > 0):
            first, second = html.split('<body>')
            html = first + '<body>\n' + input1 + second
            first, second = html.split('</body>')
            html = first + input2 + '\n</body>\n'+ second
        return html
        

def application(environ, response)
    status ='404 Not Found'
    template=['File not found.']
    environment=Environment(loader=FileSystemLoader('HTML'))
    resp_head= [('Content-Type', 'text/html')]
    
    resp = environ['PATH_INFO']
    if resp == '/index.html' or resp == '/':
        status="200 OK"
        template=environment.get_template('/index.html').render(link='<a href="/about/aboutme.html">About me</a>',
                                                         title='Index', text='<h1>Index</h1>')
    elif resp == "/about/aboutme.html":
        status="200 OK"
        template = environment.get_template('/about/aboutme.html').render(link='<a href="/index.html">Index</a>',
                                                         title='AboutMe' text='<h1>Aboutme</h1>')
    
    response(status,resp_head)
    return [template.encode('utf-8')]
    
#запустить сервер
make_server(Midwr(application), host='localhost', port=8000).serve_forever()   

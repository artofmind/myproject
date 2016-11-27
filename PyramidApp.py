from wsgiref.simple_server import make_server  # Импортирует функцию make_server, которая может создать простой веб-сервер при передаче приложения
from pyramid.response import Response
from pyramid.config import Configurator
from jinja2 import Environment, FileSystemLoader, Template

environment = Environment(loader=FileSystemLoader('HTML'))
il = '<a href="/index.html">Index</a>'
al = '<a href="/about/aboutme.html">About me</a>'


def Index(request):
    return Response(environment.get_template('/index.html').render(link=al, title='Index', text='<h1>Index</h1>'))


def AboutMe(request):
    return Response(
        environment.get_template('/about/aboutme.html').render(link=il, title='AboutMe', text='<h1>Aboutme</h1>'))


if __name__ == "__main__":
    config = Configurator()
    config.add_view(Index, route_name="index")
    config.add_route("index", "/index.html")
    config.add_view(AboutMe, route_name="about_me")
    config.add_route("about_me", "/about/aboutme.html")
    app = config.make_wsgi_app()

    server = make_server('0.0.0.0', 8000, app).serve_forever()

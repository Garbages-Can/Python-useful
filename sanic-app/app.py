import os

from sanic import Sanic
from sanic.response import html
from sanic.response import HTTPResponse
from jinja2 import Environment, FileSystemLoader

app = Sanic(__name__)
base_dir = os.path.abspath(os.path.dirname(__name__))
templates_dir = os.path.join(base_dir, 'templates')
jinja_env = Environment(loader=FileSystemLoader(templates_dir), autoescape=True)


def render_template(template_name: str, **context) -> str:
    template = jinja_env.get_template(template_name)
    return template.render(**context)


@app.route('/')
async def index(request) -> HTTPResponse:
    return html(render_template('index.html'))

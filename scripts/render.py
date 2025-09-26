from jinja2 import Environment, FileSystemLoader
from pathlib import Path

def render(template, context, out_file):
    env = Environment(loader=FileSystemLoader("templates"))
    tpl = env.get_template(template)
    html = tpl.render(**context)
    Path(out_file).write_text(html, "utf-8")

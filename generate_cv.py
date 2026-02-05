from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML
import os

def create_cv(user_data, template_file):
    # templates folder load karo
    env = Environment(
        loader=FileSystemLoader("templates")
    )

    template = env.get_template(template_file)

    # HTML generate
    html_content = template.render(user_data)

    # output pdf
    output_path = "cv.pdf"

    HTML(string=html_content).write_pdf(output_path)

    return output_path

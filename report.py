from jinja2 import Template

def render_html(data):
    template_str = """
    <!DOCTYPE html>
    <html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>
            table {
                border-collapse: collapse;
                width: 100%;
            }
            th, td {
                border: 1px solid black;
                padding: 8px;
                text-align: left;
            }
            th {
                background-color: #f9f9f9;
            }
        </style>
    </head>
    <body>
        <h1>Relatório de Serviços</h1>
        <table>
            <tr>
                <th>Nome do Serviço</th>
                <th>Endereço</th>
                <th>E-mail</th>
            </tr>
            <tr>
                <td>{{ data['properties']['Nome']['title'][0]['plain_text'] }}</td>
                <td>{{ data['properties']['Endereço']['rich_text'][0]['text']['content'] }}</td>
                <td>{{ data['properties']['E-mail']['email'] }}</td>
            </tr>
        </table>
    </body>
    </html>
    """
    template = Template(template_str)
    html_output = template.render(data=data)
    
    return html_output
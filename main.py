import requests
import logging
from report import render_html
from fastapi import FastAPI
from starlette.responses import HTMLResponse

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

app = FastAPI()

TOKEN = ''
DATABASE_ID = ''
NOTION_API_URL = 'https://api.notion.com/v1'

headers = {
    'Authorization': f'Bearer {TOKEN}',
    'Content-Type': 'application/json',
    'Notion-Version': '2021-05-13'
}

@app.get("/report/{entity_name}")
def main(entity_name: str):
    database_data = get_database_data(entity_name)
    
    if database_data:
        html_content = render_html(database_data)
        with open(f'report/relatorio.html', 'w', encoding='utf-8') as f:
            f.write(html_content)
        logging.info(f'Relatório HTML gerado com sucesso para: {entity_name}')
        return HTMLResponse(content=html_content, status_code=200)
    else:
        logging.info(f'Não foi possível gerar o relatório para: {entity_name}')
        return HTMLResponse(content=f"Erro ao gerar relatório para: {entity_name}", status_code=500)

def get_database_data(entity_name):
    database_url = f'{NOTION_API_URL}/databases/{DATABASE_ID}/query'
    response = requests.post(database_url, headers=headers)
    
    if response.status_code == 200:
        response_json = response.json()

        for item in response_json["results"]:
            nome = item["properties"]["Nome"]["title"][0]["plain_text"]
            if nome == entity_name:

                logging.info("Item encontrado")
                logging.info(item)
                
                return item
        logging.info(f"Nenhum Item encontrado para: {entity_name}")
    else:
        logging.error('Erro ao obter os dados da base de dados do Notion.')
        return None
import requests
from settings import TODO_URL, TODO_TOKEN


def create_project(name: str) -> int:
    url = f'{TODO_URL}/projects'
    headers = {
        'Authorization': f'Bearer {TODO_TOKEN}'
    }
    payload = {'name': name}
    res = requests.post(url, headers=headers, data=payload).json()
    return res['id']

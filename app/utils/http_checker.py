import requests

def check_site(url):
    try:
        response = requests.get(url, timeout=5)
        return response.status_code
    except requests.RequestException:
        return 0  # 0 = Offline / Erro

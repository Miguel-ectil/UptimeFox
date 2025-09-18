# UptimeFox 🦊

UptimeFox é um projeto simples de monitoramento de sites com Flask, Celery e Redis. Ele verifica periodicamente se sites estão online e registra os resultados em um banco de dados.

## Funcionalidades

- ✅ Cadastrar sites para monitoramento
- ✅ Verificar status atual (online/offline)
- ✅ Histórico de uptime
- 🔜 Alertas por e-mail
- 🔜 Painel web com dashboards

## Tecnologias

- Python 3.13
- Flask (API)
- Celery + Redis (tarefas agendadas)
- SQLite (ou PostgreSQL futuramente)
- SQLAlchemy (ORM)
- Flask-Migrate
- python-dotenv
- requests
## Como rodar localmente

```bash
    git clone https://github.com/Miguel-ectil/uptimefox.git
    cd uptimefox
    python -m venv .venv
    source .venv/bin/activate 
```
``` bash
    pip install -r requirements.txt
    flask run
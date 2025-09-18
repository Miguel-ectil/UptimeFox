# UptimeFox 🦊

Sistema de monitoramento de sites com status atual, histórico e alertas.

## Funcionalidades

- ✅ Cadastrar sites para monitoramento
- ✅ Verificar status atual (online/offline)
- ✅ Histórico de uptime
- 🔜 Alertas por e-mail
- 🔜 Painel web com dashboards

## Tecnologias

- Flask (API)
- Celery + Redis (tarefas agendadas)
- SQLite (ou PostgreSQL futuramente)
- SQLAlchemy (ORM)

## Como rodar localmente

```bash
git clone https://github.com/Miguel-ectil/uptimefox.git
cd uptimefox
pip install -r requirements.txt
flask run

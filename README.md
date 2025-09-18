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

1. Clone o repositório
```bash
    git clone https://github.com/Miguel-ectil/uptimefox.git
    cd uptimefox
```

2. Crie e ative um ambiente virtual
```bash
    python -m venv .venv
    source .venv/bin/activate  # Linux/macOS
```

3. Instale as dependências
```bash
    pip install -r requirements.txt
```
## 🛠️ Inicializando o banco de dados

``` bash
    flask db init      # Apenas na primeira vez
    flask db migrate -m "init"
    flask db upgrade
```
## 🧪 Como rodar o sistema

### 🟢 1. Subir a API Flask

``` bash
    flask run
```
### ⏰ 3. Rodar o Celery Beat (agendador)
``` bash
    celery -A celery_worker.celery beat --loglevel=info
```

## 🔁 Executando manualmente a verificação
```bash 
    POST -  http://localhost:5000/verificar
```

## 📬 Endpoints disponíveis
| Método | Rota         | Descrição                                |
| ------ | ------------ | ---------------------------------------- |
| `POST` | `/sites`     | Cadastra um novo site para monitoramento |
| `GET`  | `/sites`     | Lista todos os sites cadastrados         |
| `POST` | `/verificar` | Dispara verificação manual via Celery    |
| `GET`  | `/logs`      | Retorna os últimos logs de verificação   |

## ✅ Exemplo de JSON para cadastrar site

``` bash
POST /sites
{
  "url": "https://meusite.com"
}
```
## 💡 Dicas úteis

- A verificação é executada automaticamente a cada 5 minutos por padrão.
- Os logs são salvos na tabela status_log do banco de dados.
- Para testar a verificação rapidamente, você pode mudar o agendamento no celery_worker.py para timedelta(seconds=30) durante o desenvolvimento.
- Se quiser recomeçar a agenda do Beat, pare os serviços e remova os arquivos:

```bash
  rm celerybeat-schedule*
```

## 📍 Checklist de execução
``` bash 
    # Em três terminais separados:

    # Terminal 1 - API Flask
    flask run

    # Terminal 2 - Celery Worker
    celery -A celery_worker.celery worker --loglevel=info

    # Terminal 3 - Celery Beat
    celery -A celery_worker.celery beat --loglevel=info

```

## 🔒 Requisitos

- Python 3.11+ (você usa 3.13)
- Redis instalado e rodando localmente:

``` bash
    sudo apt install redis-server
    sudo systemctl start redis
```
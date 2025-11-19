# Dockerfile

FROM python:3.13-slim

# Diretório de trabalho
WORKDIR /app

# Copia os arquivos
COPY . /app

# Instala dependências
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

# Expõe a porta padrão do Flask
EXPOSE 5000

# Comando padrão
CMD ["flask", "run", "--host=0.0.0.0"]

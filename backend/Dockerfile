FROM python:3.11-slim

WORKDIR /app

# Instala dependências do sistema necessárias para psycopg2
RUN apt-get update && apt-get install -y \
    gcc \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# Copia o arquivo de requisitos
COPY requirements.txt .

# Instala as dependências Python
RUN pip install --no-cache-dir -r requirements.txt

# Copia o código da aplicação
COPY . .

# Expõe a porta do Flask
EXPOSE 5000

# Comando padrão (pode ser sobrescrito no docker-compose.yml)
CMD ["python", "-m", "flask", "run", "--host=0.0.0.0", "--port=5000"]


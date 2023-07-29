# Use a imagem oficial do Python como base
FROM python:3.9

# Define o diretório de trabalho na imagem
WORKDIR /app

# Copie o arquivo requirements.txt para o contêiner
COPY requirements.txt /app/

# Instale as dependências do projeto a partir do arquivo requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copie o código da aplicação para o contêiner
COPY . /app/

# Expõe a porta 8000 para acesso externo
EXPOSE 8000

# Define o comando para executar a aplicação
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]

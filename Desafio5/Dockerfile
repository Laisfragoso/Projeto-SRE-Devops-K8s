FROM python:3.9-slim
WORKDIR /app
# Instala as dependências necessárias
RUN pip install fastapi uvicorn
# Copia o conteúdo da sua pasta app local para dentro do container
COPY app/ .
EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

FROM agrigorev/zoomcamp-model:mlops-2024-3.10.13-slim

WORKDIR /app

COPY [ "starter.py", "requirements.txt", "./"]

RUN mkdir -p output

RUN pip install -U pip
RUN pip install -r requirements.txt

ENTRYPOINT ["python", "starter.py"]





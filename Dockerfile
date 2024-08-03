FROM python:3.10

WORKDIR bot/

RUN apt-get update && apt-get upgrade
RUN pip install --upgrade pip

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
CMD ["python", "main.py"]

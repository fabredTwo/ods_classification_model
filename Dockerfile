FROM python:3.10-slim

WORKDIR /app

COPY . /app

RUN apt-get update && apt-get install -y libgomp1

RUN pip install --no-cache-dir -r requirements.txt

RUN python -m nltk.downloader punkt stopwords wordnet

EXPOSE 5000

CMD ["python", "app.py"]
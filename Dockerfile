FROM public.ecr.aws/lambda/python:3.11

WORKDIR /var/task

COPY requirements.txt .

RUN pip install --no-cache-dir --only-binary=:all: -r requirements.txt

# descargar corpus NLTK en ruta visible
RUN python -m nltk.downloader -d /usr/share/nltk_data punkt stopwords wordnet

COPY . .

CMD ["app.handler"]
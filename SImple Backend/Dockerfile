FROM huecker.io/tiangolo/uwsgi-nginx-flask:python3.10
RUN apt-get update
RUN apt-get install -y python3-pip
RUN apt update \
    && apt install -y libmariadb-dev \
        gcc\
        python3-dev \
        libcogl-pango-dev \
        libcairo2-dev \
        libtool \
        linux-headers-amd64 \
        musl-dev \
        libffi-dev \
        libssl-dev \
        libjpeg-dev \
        zlib1g-dev
ENV STATIC_URL /static
ENV STATIC_PATH /var/www/app/static
COPY ./requirements.txt /var/www/requirements.txt
RUN pip install -r /var/www/requirements.txt
RUN pip install -U pip setuptools wheel
RUN pip install -U spacy
RUN python -m spacy download ru_core_news_sm
RUN pip install -U scikit-learn
RUN pip install -U nltk
RUN pip install -U pandas
RUN pip install -U pickle-mixin
RUN pip install -U flask-cors

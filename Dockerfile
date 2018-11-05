FROM python:3
ENV PYTHONUNBUFFERED 1
RUN rm -rf /code
RUN mkdir /code

RUN apt-get update && apt-get install -y --no-install-recommends \
    libpq-dev \
    build-essential \
    default-libmysqlclient-dev \
    libssl-dev \
    libffi-dev \
    libcurl4-openssl-dev \
&& rm -rf /var/lib/apt/lists/*


WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/
RUN python3 manage.py makemigrations
RUN python3 manage.py migrate

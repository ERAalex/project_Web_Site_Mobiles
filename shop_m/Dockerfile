FROM python
ENV PYTHONUNBUFFERED 1

WORKDIR /shop_m

ADD . / shop_m

COPY requirements.txt /shop_m

RUN python -m pip install -r requirements.txt

COPY . /shop_m

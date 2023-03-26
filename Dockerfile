FROM python
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/shop_m

ADD . /usr/src/shop_m

COPY requirements.txt /shop_m

RUN python -m pip install -r requirements.txt

COPY . /usr/src/shop_m


# for run dockerfile and create imafe just type=   "docker build . --tag=mobile_shop_app"
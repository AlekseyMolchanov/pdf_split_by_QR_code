FROM python:3.6
MAINTAINER Aleksey Molchanov <molchanov.av@gmail.com>

RUN apt-get update && \
    apt-get install -y build-essential libzbar-dev libcairo2-dev libjpeg-dev libpango1.0-dev libgif-dev libpng-dev imagemagick ghostscript libmagickwand-dev zbar-tools zlib1g-dev libzbar-dev libpython-dev

RUN echo '<policy domain="coder" rights="read|write" pattern="PDF" />' >> /etc/ImageMagick-6/policy.xml

RUN mkdir -p /opt/
ADD requirements.txt /opt/requirements.txt
WORKDIR /opt
RUN pip install -r requirements.txt

ADD . /opt/split_by_QR_code
WORKDIR /opt/split_by_QR_code


ENTRYPOINT [ "pytest" , "-vs", "-x"]
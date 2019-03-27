FROM archlinux/base
MAINTAINER Aleksey Molchanov <molchanov.av@gmail.com>

RUN pacman -Syu --noconfirm
RUN pacman -S git file awk gcc --noconfirm
RUN pacman -S python python-pip --noconfirm
RUN pacman -S base-devel --noconfirm
RUN pacman -S zbar --noconfirm
RUN pacman -S ghostscript --noconfirm
RUN pacman -S python-wand --noconfirm

RUN echo '<policy domain="coder" rights="read|write" pattern="PDF" />' >> /etc/ImageMagick-7/policy.xml

RUN mkdir -p /opt/
ADD requirements.txt /opt/requirements.txt
WORKDIR /opt
RUN pip install -r requirements.txt

ADD . /opt/split_by_QR_code
WORKDIR /opt/split_by_QR_code


ENTRYPOINT [ "pytest" , "-vs", "-x"]